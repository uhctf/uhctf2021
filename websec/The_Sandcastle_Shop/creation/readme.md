You can recreate this challenge by setting up a webpage with AngularJS version 1.3.20 (or any other [vulnerable version](https://portswigger.net/research/xss-without-html-client-side-template-injection-with-angularjs)). To check if the payload is correct, I set up an alternate version of the same vulnerable webpage that has its `alert()` function overwritten. Then, I used a NodeJS server with Nightwatch to test the payload and see if the alert function was called.