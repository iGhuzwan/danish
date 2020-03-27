FROM python:3.6

EXPOSE 3001

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY src/ /usr/src/app
CMD python api.py
