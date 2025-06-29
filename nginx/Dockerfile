# Этап сборки Node.js приложения
FROM node:18-alpine as builder

WORKDIR /app

# Копируем остальные файлы приложения
COPY build/ .

# Этап финального образа
FROM nginx:alpine

# Копируем конфигурацию Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Устанавливаем Node.js для запуска сервера
RUN apk add --no-cache nodejs

# Копируем собранное Node.js приложение из предыдущего этапа
COPY --from=builder /app /usr/share/nginx/html/app

# Создаем директорию для логов
RUN mkdir -p /var/log/nginx

# Открываем порты
EXPOSE 80

# Запускаем Nginx и Node.js сервер
CMD (cd /usr/share/nginx/html/app && node index.js &) && nginx -g 'daemon off;'