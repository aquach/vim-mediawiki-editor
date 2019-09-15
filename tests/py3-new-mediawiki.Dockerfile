FROM python:2

RUN pip install mwclient

COPY plugin .

CMD [ "python", "mwclient_integration_test.py" ]
