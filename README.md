# POPONG API

POPONG API server

## Download
    $ git clone https://github.com/teampopong/popong-api.git
	$ cd popong-api

## Setup

    $ make init
    $ vi settings.py
	    set SQLALCHEMY_URI variale as "postgresql://ID@IP:PORT/DB_NAME"
	    ex) SQLALCHEMY_URI = "postgresql://postgres@localhost:5432/pokrdb"
    $ pip install git+https://github.com/teampopong/popong-models.git

## Run

    $ ./run.py [-d] [--port PORT]
	    -d : enable debug
		--port : port_number
