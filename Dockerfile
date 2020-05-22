FROM amancevice/pandas

COPY requirements.txt /
RUN pip install -r /requirements.txt

RUN mkdir /myworkdir
WORKDIR /myworkdir
COPY ./ ./

CMD ["python", "app.py"]
