FROM python:3.12

RUN apt-get update && \
    apt-get install -y openjdk-17-jre openjdk-17-jdk curl tar && \
    wget https://github.com/allure-framework/allure2/releases/download/2.26.0/allure-2.26.0.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip3 install -r requirements.txt