# 作者
MAINTAINER outas<937023449@qq.com>
#=============酷Q=============
FROM richardchien/cqhttp:latest

EXPOSE 9000

ENV COOLQ_ACCOUNT 10000
ENV VNC_PASSWD 666666
ENV COOLQ_URL https://dlsec.cqp.me/cqp-full
ENV CQHTTP_SERVE_DATA_FILES no
ENV CQHTTP_USE_HTTP no
ENV CQHTTP_USE_WS_REVERSE yes
ENV CQHTTP_WS_REVERSE_URL ws://127.0.0.1:8080/ws/
ENV CQHTTP_WS_REVERSE_USE_UNIVERSAL_CLIENT yes


#=============bot=============
# 基于镜像基础
FROM python:3.8.1
# 暴露的端口
EXPOSE 8080
# 环境变量
ENV PATH $PATH:/usr/local/python3/bin/
# 设置代码文件夹工作目录
WORKDIR /home/user/PurinBot
# 复制当前代码文件到容器中
ADD . /home/user/PurinBot
# 初始化
RUN cp ./config.example.py config.py
RUN pip install -r requirements.txt
# bot启动命令
CMD ["python3", "run.py"]