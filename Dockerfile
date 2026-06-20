FROM python:3.11-slim

# Evita que o Python crie arquivos .pyc e obriga os logs a aparecerem na tela
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala o gerenciador 'uv' sem depender do pip
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin:$PATH"

# Copia os arquivos de dependência
COPY infra/requirements.txt ./infra/requirements.txt

# Instala as dependências usando o uv
RUN uv pip install --system -r infra/requirements.txt

# Instala fastapi e uvicorn explicitamente caso não estejam no requirements.txt
RUN uv pip install --system fastapi uvicorn

# Copia as pastas de backend e scripts
COPY backend/ ./backend/
COPY scripts/ ./scripts/

# Expõe a porta do FastAPI
EXPOSE 8000

# Executa o FastAPI
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
