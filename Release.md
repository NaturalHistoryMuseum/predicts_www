# Releasing the website

```
./generate_outputs.py > content/pages/outputs.md
```

## Adding images
Resize appropriately before adding to the repo! `JPG` for photos and probably
`PNG` for figures.

## Releasing a news newsletter

Use `qpdf` to compress.

# Adding a news item

# Developing
Edit `pelicanconf.py` and set `SITEURL=''`.

```
rm -rf output && make html
./develop_server.sh start
```

Open http://localhost:8000.

```
# When finished
./develop_server.sh stop
```

# Releasing
Edit `pelicanconf.py` and set `SITEURL = 'http://www.predicts.org.uk'`.

```
./generate_outputs.py > content/pages/outputs.md
rm -rf output && make html
ghp-import output
git push origin gh-pages
```
