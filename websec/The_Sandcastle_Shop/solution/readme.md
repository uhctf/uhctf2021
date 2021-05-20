1. Notice that the search box uses a GET parameter, and its value is reflected on the page
2. Notice that the value has been escaped for all html special characters
3. Notice that the webpage uses AngularJS version 1.3.20
4. In AngularJS and most other frameworks, {{interpolated}} values run in a sandbox in which you cannot run most regular Javascript
5. Sometimes, there is a way to escape those sandboxes. Google the sandbox escape for this version of AngularJS (1.3.20)
6. Find that `?q={{'a'.constructor.prototype.charAt=[].join;$eval('x=alert(1)');}}` is an example of a working attack
