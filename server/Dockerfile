FROM python:3.6-alpine

RUN adduser -D dan
WORKDIR /home/dan

COPY requirements.txt requirements.txt
RUN apk update && apk add --virtual .build-deps gcc python-dev musl-dev postgresql-dev

RUN python -m venv venv && \
    venv/bin/pip install --upgrade pip && venv/bin/pip install -r requirements.txt && \
    venv/bin/pip install Flask-Script

COPY . .
RUN chmod +x boot.sh && chmod +x cron.sh && chown -R dan:dan ./
USER dan

EXPOSE 5000
CMD ["./boot.sh"]