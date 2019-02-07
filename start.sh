source local.env
export $(cut -d= -f1 local.env)

pipenv run python blockchain_reader/start.py
