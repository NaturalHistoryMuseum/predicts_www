# Releasing the website

Everything is done via the command prompt.
On Windows, click on the Start menu, select 'Run' and enter `cmd.exe`.

Change the current directory to wherever you cloned the `predicts_www`. This
is probably `c:\projects\predicts_www`, so you will run:

```
cd \projects\predicts_www
```

```
workon predicts_www
git pull
python generate_outputs.py
```

## Adding images
Resize appropriately before adding to the repo! `JPG` for photos and probably
`PNG` for figures.

## Releasing a news newsletter

Compress the `PDF` before adding it to the repo e.g.,

```
Rscript compress_pdf.R content/newsletters/PREDICTSNewsletterWinter2016.pdf
```

# Adding a news item

# Developing
Edit `pelicanconf.py` and set `SITEURL=''`.

```
python generate_outputs.py
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
python generate_outputs.py
rm -rf output && make html
ghp-import output
git push origin gh-pages
```
