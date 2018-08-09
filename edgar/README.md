# EDGAR

This is a python **2** [flask application](http://localhost:5000). We strongly recommend creating a virtual env before performing the steps below.

## Running Edgar

`pip install -r requirements.txt`

### Development Server

`GRID=dev python server.py`

### Production Server

`GRID=prod python server.py 2>&1 | tee edgar-requests.log`
