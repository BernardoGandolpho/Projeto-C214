FROM python:3.8-alpine
WORKDIR /usr/src/poke_api

COPY ./requirements.txt /usr/src/poke_api/requirements.txt

RUN pip install --upgrade pip setuptools wheel \
&& pip install -r /usr/src/poke_api/requirements.txt \
&& rm -rf /root/.cache/pip

COPY . /usr/src/poke_api
