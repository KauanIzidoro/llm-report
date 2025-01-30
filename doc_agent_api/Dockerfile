FROM python:3.12

WORKDIR /app

COPY requirements.txt ./
COPY src ./src

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app/src


EXPOSE 5459
# Comando para rodar a aplicação
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5459"]
