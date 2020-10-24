FROM python:3.7.9-alpine

WORKDIR /app 
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY /app /app

#ENV FLASK_APP main.py

#ENV FLASK_RUN_HOST 0.0.0.0
#EXPOSE 5000

CMD ["python", "main.py"]