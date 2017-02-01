# Setup for development

## If you use a Mac

* Install Python
* Install git
* Install virtual envrionment stuff

TODO LH - Detailed instructions for doing this stuff on a Mac

```
mkvirtualenv predicts_www
pip install -r requirements.pip
git clone git@github.com:quicklizard99/pelican-themes.git ../pelican-themes/
```

## If you are using Windows

1. Download and install the latest release of [Python 3.x](https://www.python.org)
and install to the default location of `C:\'. Make sure that the option to
add Python to the `PATH` is checked.

2. Install the latest release of [git](https://git-scm.com/).
Make sure that the option to add `git` to the `PATH` is checked.

3. Clone this repo to your `projects` directory; if this is in `C:\'

    ```
    C:
    cd \
    mkdir projects
    cd projects
    git clone git@github.com:NaturalHistoryMuseum/predicts_www.git
    ```

4. Install dependencies

    ```
    python -m pip install -U pip setuptools
    pip install virtualenvwrapper-win
    mkvirtualenv predicts_www
    ```

    ```
    workon predicts_www
    cd \projects\predicts_www
    pip install -r requirements.pip
    ```


Refs
Python
virtualenvwrapper
Pelican
https://spapas.github.io/2013/10/07/pelican-static-windows/
