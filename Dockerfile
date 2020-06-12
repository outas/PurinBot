# 基于镜像基础
FROM python:3.8.1

# 作者
MAINTAINER outas<937023449@qq.com>

# 环境变量
ENV PATH $PATH:/usr/local/python3/bin/

# 暴露的端口
EXPOSE 8080

# 设置代码文件夹工作目录
WORKDIR /home/PurinBot

# 复制当前代码文件到容器中
ADD . /home/PurinBot
  
# 安装所需的包
RUN pip install -r requirements.txt
  
# bot启动命令
CMD ["python3", "run.py"]