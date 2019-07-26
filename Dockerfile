FROM python:3

WORKDIR /usr/src/app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG port
RUN echo $port
EXPOSE $port

# run the command
CMD ["python3", "./server.py"]