# pytran
Python util to transfer repos between GitHub usernames

## Setup
- Switch to the virtual environment included
- Install requirements, i.e.

```
(.venv) allyndawn@Astera pytran % pip install -r requirements.txt
Requirement already satisfied: numpy==1.26.3 in ./.venv/lib/python3.11/site-packages (from -r requirements.txt (line 1)) (1.26.3)
```

- Copy `sampleconfig.json` to `config.json` at the root of the project
- Edit `config.json` to contain the GitHub username and personal access token you want to transfer from and the GitHub username to transfer to

## Running
- python pytran.py

