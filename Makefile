init:
    pip install -r requirements.txt

test:
    pytest --cov-report term-missing --cov=src tests/