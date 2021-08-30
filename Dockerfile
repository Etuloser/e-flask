FROM frolvlad/alpine-python3:latest

LABEL maintainer="Eles <1494136313@qq.com>"

COPY ./ /srv/e-flask/

# RUN /bin/sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
#     apk add --no-cache mariadb-dev build-base python3-dev && \
#     rm -rf /var/cache/apk/*

RUN cd /srv/e-flask/ && \
    pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

EXPOSE 2333

WORKDIR /srv/e-flask/

CMD ["gunicorn","manage:app","-b","0.0.0.0:2333"]