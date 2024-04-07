FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn

COPY . ./

EXPOSE 8001

CMD ["sh", "-c", "python manage.py makemigrations && \
                 python manage.py migrate && \
                 python manage.py collectstatic --noinput && \
                 gunicorn --bind 0.0.0.0:8001 couponbackup.wsgi:application"]
