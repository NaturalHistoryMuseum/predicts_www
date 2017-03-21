# Releasing the website

Everything is done via the command prompt.
On Windows, click on the Start menu, select 'Run' and enter `cmd.exe`.

Change the current directory to wherever you cloned the `predicts_www`. This
is probably `c:\projects\predicts_www`. You must also pull the repo
so that you have changes made my other people. Simply copy/paste the following
block into your command prompt:

```
C:
cd \projects\predicts_www
workon predicts_www
git pull
python generate_outputs.py
```

## Adding a new member of the team

1. Open `content\pages\team.md`

2. Copy / paste the block for an existing team member

3. Edit the name, description, image path, image alt text and id

4. Resize the image to 250 pixels in width and save to `content/images/team`

## Releasing a newsletter

Compress the `PDF` before adding it to the repo e.g.,

```
Rscript compress_pdf.R content/newsletters/PREDICTSNewsletterWinter2016.pdf
```

## Adding a news item

## Adding images
Resize appropriately before adding to the repo! `JPG` for photos and probably
`PNG` for figures.


# Testing your changes
Edit `pelicanconf.py` and set `SITEURL=''`.

## On a Mac
```
python generate_outputs.py
rm -rf output && make html
./develop_server.sh start
```

Open http://localhost:8000.

When you have finished testing
```
./develop_server.sh stop
```

## On Windows

```
python generate_outputs.py
generate.bat
serve.bat
```

Open http://localhost:8000.

When you have finished testing `CTRL+C`.

# Commit your changes to git and release the website!

See a list of which files have been changed, which are new and which have been
deleted

```
git status
```

Double-check your changes

```
git diff
```

Stage the files that you have changed. **Do not stage `pelicanconf.py`**.
```
git add <files you have changed>    <- do not change pelicanconf.py
```

Commit your the staged files and push to github.com
```
git commit -m "A description of your changes"
git push origin
```

At this point, your changes are in the github.com repo but they are not yet
on www.predicts.org.uk. We will do this next.

Edit `pelicanconf.py` and set `SITEURL = 'http://www.predicts.org.uk'`.
Copy/paste one of the following

### On a Mac

```
python generate_outputs.py
rm -rf output && make html
ghp-import output
git push origin gh-pages
```

### On Windows

Copy/paste the following

```
python generate_outputs.py
rmdir /Q /S output
generate
ghp-import output
git push origin gh-pages
```
