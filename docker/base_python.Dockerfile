FROM python:3.12-slim
WORKDIR /app
COPY code.py /app/code.py
CMD ["python3", "/app/code.py"]
