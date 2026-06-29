FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirenments.txt

EXPOSE 5000

ENV APP_ENV=production

CMD ["python", "app.py"]