const express = require('express');

const app = express();

app.use((req, res, next) => {
    if (req.path.endsWith('.cgi')) {
        res.setHeader('Content-Type', 'text/html');
    }

    next();
});

app.use(express.static('public'));

const server = app.listen(8000);

for (const interruptSignal of ['SIGINT', 'SIGTERM']) {
    process.on(interruptSignal, () => { server.close(() => { process.exit(143); }); });
}