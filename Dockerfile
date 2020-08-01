FROM python:3.6 
COPY /mysite /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
