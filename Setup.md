# Setup for development

## If you use a Mac

Install Python
Install virtual envrionment stuff
Install git

```
mkvirtualenv predicts_www
pip install -r requirements.pip
git clone git@github.com:quicklizard99/pelican-themes.git ../pelican-themes/
```

## If you are using Windows

1. Download and install the latest release of [Python 3.x](https://www.python.org)
and install to the default location of `C:\'

2. Install the latest release of [git](). Make sure that the option to add `git`
to the `PATH` is checked.

3. Clone this repo to your `projects` directory; if this is in `C:\'

    ```
    C:
    cd `\projects`
    git clone git@github.com:NaturalHistoryMuseum/predicts_www.git
    ```

4. Install dependencies

    **TODO** LH - use virtualenv here

    ```
    mkvirtualenv predicts_www
    cd predicts_www
    c:\python35\scripts\pip install -r requirements.pip
    ```
