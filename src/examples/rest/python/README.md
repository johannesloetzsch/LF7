# Python REST example

Der Beispielcode [rest.py](https://github.com/johannesloetzsch/LF7/blob/main/src/examples/rest/python/rest.py) nutzt die Bibliothek [FastAPI](https://fastapi.tiangolo.com/) um eine REST-API mit Swagger UI bereitzustellen.

## Usage

```sh
git clone https://github.com/johannesloetzsch/LF7.git
cd src/examples/rest/python
```

```sh
python -m venv .venv
source .venv/bin/activate

python -m ensurepip
pip install -r requirements.txt
```

```sh
python rest.py
```

[http://localhost:8000/index.html](http://localhost:8000/index.html)

## Development

To run a devserver with automatic reloading when code changed, use:
```sh
uvicorn rest:app --reload
```
