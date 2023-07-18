FROM python:3.9-slim
WORKDIR /app
COPY /src/script.py .
RUN pip install art
ENTRYPOINT ["python", "script.py"]