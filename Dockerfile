# 使用Python官方镜像作为基础镜像
FROM python:3.11.9

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件到容器中
COPY . .

# 暴露端口
EXPOSE 8081

# 启动命令
CMD ["gunicorn", "--bind", "0.0.0.0:8081", "main:app"]