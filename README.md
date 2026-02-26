# agentic_ai_server

### Local setup using anaconda
```
conda create -p ./venv python==3.13.9 --yes
conda activate ./venv
pip install -r ./requirements.txt
```

### Install packages
```
conda activate ./venv
pip install <package_name>
pip list --format=freeze > requirements.txt
```

### Run
`uvicorn src.app:app --reload`
