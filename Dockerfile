FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app/app.py .

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["app.py"]