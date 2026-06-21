.PHONY: install test lint run-frontend run-backend setup

setup:
	@echo "Setting up Python virtual environment with uv..."
	uv venv
	@echo "Virtual environment created. Run 'infra\venv\Scripts\activate' (Windows) to activate."

install:
	@echo "Installing backend dependencies using uv..."
	uv pip install -r infra/requirements.txt
	@echo "Installing frontend dependencies..."
	cd frontend && npm install

test:
	@echo "Running backend tests..."
	uv run pytest backend/

run-frontend:
	@echo "Starting Next.js frontend server..."
	cd frontend && npm run dev

run-backend:
	@echo "Starting FastAPI backend server..."
	uv run uvicorn backend.api.main:app --reload
