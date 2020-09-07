FROM frolvlad/alpine-python3:latest

LABEL maintainer="yi.zeng@ez-cloud.com.cn"

COPY ./ /srv/e-flask/

RUN cd /srv/e-flask/ && \
    pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

EXPOSE 2333

WORKDIR /srv/e-flask/

CMD ["gunicorn","manage:app","-b","0.0.0.0:2333"]
