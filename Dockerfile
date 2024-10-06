FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc libc-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn


COPY . .

EXPOSE 5000

ENV FLASK_APP=app
ENV FLASK_ENV=development

CMD ["gunicorn", "-m", "4", "-b", "0.0.0.0:5000", "app:create_app()", "--timeout", "300", "--reload"]
#CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]