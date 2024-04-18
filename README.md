# Báo cáo bài test:
## Thời gian
Thời gian thực hiện khoảng 24h.
## Hình ảnh trang web

## Các bước build
1. Clone code
2. Copy file env, không cần thay đổi gì
```sh
cp docker-compose.env.example docker-compose.env
```
3. Dùng Docker để build project
```sh
docker compose up -d --build
```
Khi build, database sẽ tự động được migrate, thông tin sản phẩm mẫu tự động được crawl.
4. Nếu build thành công, API docs có thể truy cập qua [localhost:8000/docs](http://localhost:8000/docs), trang frontend có thể truy cập qua [localhost:3000](http://localhost:3000).