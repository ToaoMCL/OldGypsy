FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY cards.json .
EXPOSE 5003
ENTRYPOINT [ "python3", "app.py" ]