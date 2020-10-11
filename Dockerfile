FROM python:3.7.9-alpine

COPY /app /app
COPY requirements.txt /app
WORKDIR /app 
RUN pip install -r requirements.txt

ENV FLASK_APP main.py

ENV FLASK_RUN_HOST 0.0.0.0
#EXPOSE 5000

CMD ["python", "main.py"]