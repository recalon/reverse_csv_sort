FROM python:3 as intermediate

RUN mkdir /tmp/reverse_string_sort /tmp/reverse_string_sort/in /tmp/reverse_string_sort/out

WORKDIR /tmp/reverse_string_sort

ADD src/csv_sort.py .
ADD data/inputs in

RUN chmod -R 755 .
RUN chmod -R 777 out

CMD ["python", "csv_sort.py"]
