FROM alpine:3.11

RUN apk --update upgrade
RUN apk update && apk add --no-cache inotify-tools
RUN apk update && apk add --no-cache supervisor
RUN pip3 install watchdog

RUN mkdir /reverse_csv_sort /reverse_csv_sort/in /reverse_csv_sort/out /reverse_csv_sort/log /reverse_csv_sort/supervisord

WORKDIR /reverse_csv_sort

ADD src/supervisord_reverse_csv_sort.conf supervisord
ADD src/csv_sort.py .
RUN chmod 750 csv_sort.py

CMD ./run.sh
