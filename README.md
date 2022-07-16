
## PROJECT SETUP
Copy `.env.example` to `.env` file, update proper credentials

```
pip3 install virtualenv
virtualenv venv
pip3 install "fastapi[all]"
pip install "uvicorn[standard]"
```

## STARTING YOUR PROJECT
start your virtual environment with: `source venv/bin/activate`

start your server with: `uvicorn main:app --reload`