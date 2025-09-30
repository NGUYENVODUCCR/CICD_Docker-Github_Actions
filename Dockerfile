# Sử dụng Python 3.11 slim
FROM python:3.11-slim

# Đặt thư mục làm việc
WORKDIR /app

# Copy requirements trước để tối ưu cache
COPY requirements.txt .

# Cài dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code (bao gồm app.py và templates/)
COPY . .

# Mở cổng 5000 (Flask mặc định)
EXPOSE 5000

# Chạy Flask app
CMD ["python", "app.py"]
