# Mines ACM Student Chapter Website

## Setting up your Development Environment

Clone the repo:

    $ git clone https://github.com/ColoradoSchoolOfMines/acm-website.git

Install the application and its dependencies:

    $ pip install -e . --user

If you do not have `gearbox` installed:

    $ pip install --user tg.devtools

Setup the application:

    $ cp development.ini.sample development.ini
    $ gearbox setup-app

Finally, serve the application:

    $ gearbox serve --reload --debug

