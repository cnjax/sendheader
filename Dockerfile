FROM python:alpine
WORKDIR /app
COPY main.py /app
CMD ["python3", "/app/main.py"]