pip_requirements:
	pip install -r pip_requirements.txt

start_api:
	uvicorn unittestapi:app --host 0.0.0.0 --port 8000 --reload

feed:
	curl -S localhost:8000/feed