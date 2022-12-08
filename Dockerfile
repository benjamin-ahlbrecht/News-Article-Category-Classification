FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY models/app.py ./

COPY models/distilbert ./distilbert

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]