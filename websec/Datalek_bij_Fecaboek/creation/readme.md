This is a modified version of [Benikerbij.be](https://benikerbij), a tool I created to easily search if a phone number was breached by the Facebook 500mio+ dataleak which was released to the public free of charge in April 2021.

Ultimately the original tool used the [Haveibeenpwned.com](https://haveibeenpwned.com) API. This has a relatively steep rate limit, so to accomodate usage peaks, the tool still used its own database as a fallback when it hit the rate limit.

The challenge is based on that concept. The "expensive API" is properly coded with prepared SQL statements, but the "internal database" has barely any protection against SQL injection in place. A participant must recognise the different databases used (it's hinted on the /about page and the api responses include the 'source'). Afterwards, they have to find a SQL injection payload which works. The main challenges are blocking of `-`, `;` and `/*`, as well as a `LIMIT 1` statement in the SQL. The latter is also hinted on the /about page.

Once they have dumped the 20 numbers in the database, they should recognise that one is significantly longer than the other and does not follow the 'valid phone number format' (valid ones start with `69`, `420` or `1337`).

The flag is decimal ascii without spaces.