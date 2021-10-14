FROM python:3.8-bullseye

RUN apt-get update
RUN apt-get -y install ffmpeg

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]