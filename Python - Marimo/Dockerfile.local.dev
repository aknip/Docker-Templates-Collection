FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src ./src

EXPOSE 8080

CMD ["marimo", "edit", "--host", "0.0.0.0", "--port", "8080", "--no-token"]
# CMD [ "marimo", "run", "./src/myapp.py", "--host", "0.0.0.0", "--port", "8080", "--no-token" ]



