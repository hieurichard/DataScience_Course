Model serving bằng Fast API và đóng gói bằng docker

yêu cầu cài đặt docker và các thư viện cần thiết

vào terminal (command prompt) hoặc window powershell sau đó vào đường dẫn của thư mục này bằng lệnh cd

buil docker images (tạo docker)

docker build -t hieu/asiaplant:flag .


run the docker (chạy docker)

docker run --rm -p 8000:8000 hieu/asiaplant:flag


truy cập http://localhost:8000/docs và vào post để dự đoán hình ảnh