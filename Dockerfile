FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
VOLUME /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.doubanio.com/simple/

EXPOSE 5001

CMD [ "python", "manage.py" ]
