
# Python GraphQL Spike

### Setup Virtual Python Environment
```
py -m venv venv
python -m pip install --upgrade pip
.\venv\Scripts\activate
```

### Setup Dependencies
[See ariadne docs here](https://ariadnegraphql.org/docs/intro.html)
```
pip install ariadne
pip install uvicorn
```

### Run the uvicorn server
Activate the venv if you haven't already:
```
.\venv\Scripts\activate
```

Then run the server:
```
uvicorn server:app
```
