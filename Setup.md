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

1. Download and install the latest release of Python 3.x

    * From https://www.python.org
    * Make sure you get the 64 bit version
    * Install to the default location of `C:\`
    * Check the option 'Add Python to environment variables'

2. Install the latest release of [git](https://git-scm.com/).
Make sure that `Use Git from the Windows Command Prompt` is check

3. Start a Command prompt - click on the Start menu, select 'Run' and enter
`cmd.exe`

    ```
    git config --global user.name "Your Name"
    git config --global user.email "your@email.address"
    ```

    See https://help.github.com/articles/setting-your-email-in-git/ and
    https://help.github.com/articles/setting-your-email-in-git/ for more
    information.

4. Clone this repo to your `projects` directory; if this is in `C:\`

    ```
    C:
    cd \
    mkdir projects
    cd projects
    git clone https://github.com/NaturalHistoryMuseum/predicts_www.git
    cd predicts_www
    ```


git clone https://github.com/NaturalHistoryMuseum/pelican-themes.git c:\projects\pelican-themes


5. Install dependencies

    ```
    python -m pip install -U pip setuptools
    pip install virtualenvwrapper-win
    mkvirtualenv predicts_www
    workon predicts_www
    cd \projects\predicts_www
    pip install -r requirements.pip
    ```


Refs
Python
virtualenvwrapper
Pelican
https://spapas.github.io/2013/10/07/pelican-static-windows/
