From python:3.9.13
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD python app.py