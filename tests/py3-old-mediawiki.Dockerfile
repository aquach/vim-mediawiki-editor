FROM python:3

RUN pip install mwclient==0.9.3

COPY plugin .

CMD [ "python", "mwclient_integration_test.py" ]
