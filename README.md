# page-me

Page-me is a simple REST API for netpage + CCG server.

## Quickstart
Make sure you have python and [pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv) installed
```
pip install --user pipenv
```

Get the software and run it
```
# clone this repo
git clone https://github.com/yannhowe/page-me.git

# Start Django server
cd page-me
pipenv run python manage.py runserver
```

Navigate to http://127.0.0.1:8000/test/netpage/