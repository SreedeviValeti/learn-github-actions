FROM python:3.11-slim
WORKDIR /app
COPY  requirements-test.txt .
RUN pip install --no-cache-dir -r requirements-test.txt
COPY src/ ./src/
COPY tests/ ./tests/
ENV PYTHONPATH=.
CMD ["python", "-c", "import src.claims; print('claims module loaded OK')"]
