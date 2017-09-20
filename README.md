# Mines ACM Student Chapter Website

## Setting up your Development Environment

Clone the repo:

    $ git clone https://github.com/ColoradoSchoolOfMines/acm-website.git

### To install in user's personal path (~/.local)

Install the application and its dependencies:

    $ pip install -e . --user

If you do not have `gearbox` installed:

    $ pip install --user tg.devtools

Setup the application:

    $ cp development.ini.sample development.ini
    $ gearbox setup-app

Finally, serve the application:

    $ gearbox serve --reload --debug

### To use a virtual environment

Make sure you have `virtualenvwrapper` installed

On Arch Linux:

    $ sudo pacman -S python-virtualenvwrapper

Make a virtual environment:

    $ mkvirtualenv acm-website

Activate the virtual environment:

    $ workon acm-website

Install the application and its dependencies:

    $ pip install -e .

If you do not have `gearbox` installed:

    $ pip install tg.devtools

Setup the application:

    $ cp development.ini.sample development.ini
    $ gearbox setup-app

Finally, serve the application:

    $ gearbox serve --reload --debug

When you're finished working on the project and want to exit the virtual environment:

    $ deactivate
