FROM python:3.7.5-alpine

EXPOSE 5000

ENV USER app
ENV APP_HOME /home/$USER

RUN adduser -D -h $APP_HOME $USER
WORKDIR $APP_HOME

USER $USER

ADD app.tar $APP_HOME

RUN pip3 install -r requirement.txt --user

CMD [ "python3", "app.py" ]
