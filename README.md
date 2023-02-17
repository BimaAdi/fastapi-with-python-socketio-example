# Connect fastapi with python-socketio example
Example how to connect fastapi with python-socketio

## Requirements
- Python 3.11 (tested in python 3.11)
- pip or poetry
- Message queue (redis. kafka, rabbitmq) (not required but recommended for production)

## Instalation using pip
1. Create virtual env `python -m venv env` and activate it `source env/bin/activate`
1. install depedency `pip install -r requirements.txt`
1. Edit core/socket_io.py based on message_queue configuration 
(if you don't want use any message queue just comment line 5)
1. run the server `uvicorn main:app`
1. on browser open http://localhost:8000/static/index.html

## Instalation using poetry
1. install depedency `poetry install`
1. Edit core/socket_io.py based on message_queue configuration 
(if you don't want use any message queue just comment line 5)
1. run the server `poetry run uvicorn main:app`
1. on browser open http://localhost:8000/static/index.html

## References
1. https://www.reddit.com/r/FastAPI/comments/neds9c/integrate_socketio_with_fastapi/
1. https://github.com/tiangolo/fastapi/issues/129
