FROM python:3

WORKDIR /usr/src/app

COPY s.py ./
COPY requirements.txt ./

ENV CHAT_PORT=4444

ENTRYPOINT [ "python3", "s.py" ]