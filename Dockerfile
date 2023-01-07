FROM python:3.8.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry==1.3.1 && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-cache --without dev && \
    pip uninstall --yes poetry

CMD [ "python", "pipeline.py", "/censo.csv", "/rouanet.csv" ]
