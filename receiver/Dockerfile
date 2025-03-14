FROM python:3.11-alpine

WORKDIR /app

COPY ./receiver/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./receiver/src /app/src
CMD ["fastapi", "run", "src/api.py", "--port", "3001"]
