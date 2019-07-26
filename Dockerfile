FROM python:3-onbuild

ARG port
RUN echo $port
EXPOSE $port

# run the command
CMD ["python3", "./server.py"]