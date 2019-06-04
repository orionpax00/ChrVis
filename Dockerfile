FROM debian:8

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && \
    apt-get install -y unzip build-essential --no-install-recommends locales python3 python3-pip && \
    wget --quiet --no-check-certificate https://github.com/orionpax00/ChrVis/archive/version1.zip && unzip ChrVis-version1.zip && \
    cd ChrVis-version1 && \
    pip3 install -r requirements.txt && \
    cd chrvis-server && \
    python3 manage.py runserver 9999

CMD [ "/bin/bash" ]
