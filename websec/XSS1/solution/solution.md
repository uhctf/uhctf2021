# Insecure Notes

Creator: [Bas Van Assche](https://github.com/basva923)

> We think our note-taking application has a XSS issue, can you take a look?

## Solution

When a new note is created the note is shown below the edit box. The note content is not filterd in any way. This allows us to create a script tag.

A possible solution is:
```html
<script>alert(1)</script>
```

Copy the url in the validator to get the flag.