FROM python:3.9-alpine

WORKDIR /app

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt .

RUN pip install --requirement requirements.txt

COPY counter.py main.py /app/

ENTRYPOINT [ "python", "main.py" ]