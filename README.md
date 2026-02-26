# agentic_ai_server

### Local setup using anaconda
```
conda create -p ./venv python==3.13.9 --yes
conda activate ./venv
python --version
pip install -r ./requirements.txt
```

### Run
`uvicorn src.app:app --reload`
