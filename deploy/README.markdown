# Source of adamw523.com Site

A [Hyde](http://hyde.github.com/) powered site.

## Development

All development happens in the 
[`hyde`](https://github.com/adamw523/adamw523.github.com/tree/hyde)
branch. HTML and other content is in the `content` directory.

A clone of the repo on the `master` branch needs to exist at 
`../adamw523.github.com` relative to the clone of the repo
on the `hyde` branch.

## Deployment

```
$ hyde publish -p github
```

## Tools

Serve up site locally on port `8080`:

```
$ hyde serve
```

Generate site from templates:

```
$ hyde gen
```