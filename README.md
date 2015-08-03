# POPONG API

POPONG API server

## Download
    $ git clone https://github.com/teampopong/popong-api.git
	$ cd popong-api

## Setup

1. Create & modify configuration files

        $ make init
        $ createuser postgres
    - Set password for user "postgres" in PostgreSQL

1. Create & init DB (You should first obtain a `pokrdb.dump` from [here](https://drive.google.com/file/d/0BwxUh0GzMJ4VMXJncHM4Qm1LZDQ/view?usp=sharing))

        $ sudo -u postgres psql -h localhost -U postgres -c 'CREATE DATABASE pokrdb;'
        $ sudo -u postgres psql -d pokrdb -f pokrdb.dump

    - Modify `SQLALCHEMY_URI` in settings.py
	    - set SQLALCHEMY_URI variale as "postgresql://ID_HERE:PASSWD_HERE@HOST_HERE:PORT/DB_NAME"
        - `ID_HERE`: postgres id (ex: postgres)
        - `PASSWD_HERE`: postgres pw
        - `HOST_HERE`: postgres host (ex: localhost)

		$ pip install git+https://github.com/teampopong/popong-models.git

## Run

    $ ./run.py [-d] [--port PORT]
	    -d : enable debug
		--port : port_number
