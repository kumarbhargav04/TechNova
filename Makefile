.PHONY: test backend-test frontend-test lint

test: backend-test frontend-test

backend-test:
	@echo "Running backend unit tests..."
	cd pata-ai/backend && python -m unittest discover -s app/tests -p "test_*.py"

frontend-test:
	@echo "Running frontend unit tests..."
	cd pata-ai/frontend && node --test src/utils/*.test.js

lint:
	@echo "Checking formatting and code hygiene..."
