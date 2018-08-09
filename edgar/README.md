## Running Edgar

`pip install -r requirements.txt`

### Development Server

`GRID=dev python server.py`

### Production Server

`GRID=prod python server.py 2>&1 | tee edgar-requests.log`
