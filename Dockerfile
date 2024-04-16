FROM python:alpine3.14

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 4321
CMD ["python", "app.py"]