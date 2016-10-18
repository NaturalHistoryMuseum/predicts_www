# www_predicts
Website for the PREDICTS project

## Install

If you are using Windows, download the latest release of
[Python](https://www.python.org/) and install to the default location of
`c:\Python35`.

### If you are Lawrence

```
mkvirtualenv predicts_www
pip install -r requirements.pip
git clone git@github.com:quicklizard99/pelican-themes.git ../pelican-themes/
```

### If you are using Windows

1. Download and install the latest release of [Python 3.x](https://www.python.org)
to `C:\'

2. Clone this repo to your `projects` directory; if this is in `C:\'

    ```
    C:
    cd `\projects`
    git clone git@github.com:NaturalHistoryMuseum/predicts_www.git
    ```

3. Install dependencies

    **TODO** LH - use virtualenv here

    ```
    cd predicts_www
    c:\python35\scripts\pip install -r requirements.pip
    ```

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
rm -rf output && make html
ghp-import output
git push origin gh-pages
```

# Adding images
Resize appropriately before adding to the repo! `JPG` for photos and probably
`PNG` for figures.

# Releasing the newsletter

Use `qpdf` to compress.

# Theme
The site uses [Bootswatch readable](http://bootswatch.com/readable/)
for Bootstrap, via the
[pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3)
theme.
