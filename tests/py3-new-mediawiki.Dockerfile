FROM python:3

RUN pip install mwclient

COPY plugin .

CMD [ "python", "mwclient_integration_test.py" ]
