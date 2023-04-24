FROM python:alpine
WORKDIR /app
COPY main.py /app
EXPOSE 80/tcp
CMD ["python3", "/app/main.py","80"]