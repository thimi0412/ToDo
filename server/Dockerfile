FROM python:3
RUN pip3 install flask mysql-connector-python-rf
RUN mkdir /src
WORKDIR /src
ADD db_connect.py /src/
ADD server.py /src/
ADD Task.py /src/
CMD /usr/local/bin/python /src/server.py
