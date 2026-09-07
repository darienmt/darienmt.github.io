# darienmt.github.io
This is my personal blog.... [darienmt.com](https://darienmt.com)

## Local Hugo development

The site is built with Hugo Extended. Install the pinned version used by
`.github/workflows/hugo.yml`, then run:

```sh
make build     # build public/ with the live URL structure
make validate  # build and check the migration URL manifest
make serve     # run the local Hugo server
```

`migration/url-manifest.txt` records the published URL contract.
