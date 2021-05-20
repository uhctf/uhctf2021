require('dotenv').config()

var http = require('http');
var fs = require('fs');
const { Client } = require('pg');
let client = null;

const response_delay = 500;
const server_port = 8088;
let sessions = {};
let connections = {};
setInterval(function() { sessions = {}; }, 2000);

function parseCookies (request) {
    var list = {},
        rc = request.headers.cookie;

    rc && rc.split(';').forEach(function( cookie ) {
        var parts = cookie.split('=');
        list[parts.shift().trim()] = decodeURI(parts.join('='));
    });

    return list;
}

function generateId(length) {
    var result           = [];
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
      result.push(characters.charAt(Math.floor(Math.random() * charactersLength)));
   }
   return result.join('');
}

function sendResponse(responseObj, code, content, id) {
    responseObj.writeHead(code, { 'Content-Type': 'application/json', 'Set-Cookie': `sessid=${id}` });
    if (typeof(content) === 'string') body = JSON.stringify({'message': content});
    else if (typeof(content) === 'object') body = JSON.stringify(content);
    else body = 'What are you doing?';
    responseObj.end(body);
}

function successResponse(responseObj, content, id) {
    sendResponse(responseObj, 200, content, id);
}

function errorResponse(responseObj, code, content, id) {
    sendResponse(responseObj, code, content, id);
}

http.createServer(function (request, response) {
    try {
        let newUser = false;
        const cookies = parseCookies(request);
        let id = cookies['sessid'];
        if (id === undefined || /[^ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789]/.test(id) || id.length < 8) {
            id = generateId(24);
            while (sessions[id] !== undefined) {
                console.log("ID already used, generating a new one");
                id = generateId(8);
            }
            newUser = true;
        } else if (sessions[id] === undefined) {
            sessions[id] = 0;
        }
        if (request.method === 'GET' && request.url === '/') {
            try {
                const pageHtml = fs.readFileSync("page.html", "utf8");
                response.writeHead(200, { 'Content-Type': 'text/html', 'Set-Cookie': `sessid=${id}` });
                response.end(pageHtml);
            } catch(e) {
                errorResponse(response, 500, "Something is going terribly wrong here. This is NOT part of the CTF. Please contact the organisers.", id);
            }
        }
        else if (request.method === 'GET' && request.url === '/about') {
            try {
                const pageHtml = fs.readFileSync("about.html", "utf8");
                response.writeHead(200, { 'Content-Type': 'text/html', 'Set-Cookie': `sessid=${id}` });
                response.end(pageHtml);
            } catch(e) {
                errorResponse(response, 500, "Something is going terribly wrong here. This is NOT part of the CTF. Please contact the organisers.", id);
            }
        }
        else if (request.method === 'POST' && request.url === '/api') {
            if (!connections[request.socket.remoteAddress] || connections[request.socket.remoteAddress] < 0) {
                connections[request.socket.remoteAddress] = 0;
            }
            if (connections[request.socket.remoteAddress] >= 5) {
                // not more than 5 connections allowed
                errorResponse(response, 429, "Please limit the speed of your requests!", id);
            } else {
                connections[request.socket.remoteAddress]++;
                setTimeout(function(){
                    var data = '';
                    request.on('data', (chunk) => {
                        data += chunk;
                    });
                    request.on('end', async () => {
                        if (newUser) {
                            errorResponse(response, 403, "No anonymous users allowed", id);
                        }
                        let valid = true;
                        if (!typeof(data) === 'string') valid = false;
                        if (!/^(1337|69|420)/.test(data)) valid = false;
                        if (/-|;|\/\*/.test(data)) {
                            errorResponse(response, 400, "No SQL injection please", id);
                        }
                        else if (valid) {
                            sessions[id] += 1;
                            const useInternalDb = sessions[id] > 2;
                            try {
                                if (client === null) {
                                    client = new Client();
                                    client.connect();
                                }
                                let res = null;
                                if (!useInternalDb) {
                                    res = await client.query('SELECT phone FROM numbers WHERE phone=$1 LIMIT 1;', [data]);
                                } else {
                                    res = await client.query(`SELECT phone FROM numbers WHERE phone=${data} LIMIT 1;`);
                                }
                                successResponse(response, {
                                    'data': res.rows,
                                    'source': useInternalDb ? 'internal database' : 'expensive API',
                                }, id);
                            } catch (e) {
                                console.log(e);
                                errorResponse(response, 500, {
                                    'message': "Something went wrong...",
                                    'source': useInternalDb ? 'internal database' : 'expensive API',
                                }, id);
                            }
                        } else {
                            errorResponse(response, 400, "Not a valid phone number", id);
                        }
                    });
                    connections[request.socket.remoteAddress]--;
                }, response_delay);
            }
        } else {
            errorResponse(response, 404, "Nothing to see here", id);
        }
    } catch (e) {
        console.log("Prevented the server from crashing...");
        console.log(e);
    }
}).listen(server_port);
console.log(`Server running at http://127.0.0.1:${server_port}/`);
