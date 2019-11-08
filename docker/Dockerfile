FROM python:3.7
MAINTAINER "JINHUA"
ENV DEBIAN_FRONTEND noninteractive
ENV TZ Asia/Shanghai
WORKDIR /usr/src/app
RUN git clone https://github.com/15871722713/http_server.git
WORKDIR /usr/src/app/http_server/
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
EXPOSE 6000
