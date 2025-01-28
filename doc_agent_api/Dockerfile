FROM python:3.12-slim

WORKDIR /doc_agent_api

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "doc_agent_api/src/main.py"]