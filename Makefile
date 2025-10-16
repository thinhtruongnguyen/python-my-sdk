.PHONY: test dev

dev:
	python3 src/my_platform_sdk_package/main.py

test:
	PYTHONPATH=src pytest tests/ -v
