FROM alpine:3.5
RUN apk add --update py2-pip
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY run.py /usr/src/app/
COPY templates /usr/src/app/templates
COPY static /usr/src/app/static

EXPOSE 5000

CMD ["python", "/usr/src/app/run.py"]