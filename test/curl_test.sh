curl 'http://127.0.0.1:8000/register' \
  -X 'POST' \
  -H 'content-type: application/json' \
  -d '{"username":"test","password":"123456","email":"test@qq.com"}' \
  --compressed


curl 'http://127.0.0.1:8000/login' \
  -X 'POST' \
  -H 'content-type: application/json' \
  -d '{"username":"test","password":"123456"}' \
  --compressed


  curl 'http://127.0.0.1:8000/hi' \
  -H 'cookie: access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjI1MTE4MjA0LCJqdGkiOiJhMThiNGFlZC0yN2U1LTQ2MDQtYjc1ZS00YmE4NTY5ZDc4MmEiLCJ0eXBlIjoiYWNjZXNzIiwic2lnbmFsIjoxLCJuYmYiOjE2MjUxMTgyMDQsImNzcmYiOiJlNzlkZTI2Yy03MzU4LTQ1M2ItOGRkNS1mZjRiMzRkODgxZmEiLCJleHAiOjE2MjUxMjAwMDR9.qht8A2Q9U9ZLja_1WZeyvwJMQ8zIaVOOpOIHG6ukjq0;refresh_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNTExODIwNCwianRpIjoiOTQxMWM4NmUtNGIwNy00MjlkLWE0NjctY2M2ODU1NTcxYjQxIiwidHlwZSI6InJlZnJlc2giLCJzaWduYWwiOjEsIm5iZiI6MTYyNTExODIwNCwiY3NyZiI6ImQ4M2IzNDMxLWNjYmMtNDI1Mi1iODBlLTI2YmFmZTJjMmVjNyIsImV4cCI6MTYyNTM3NzQwNH0.IZ6qii7FaVnkTu_xBTOBDSMXq9VweAGnAZcrrpoIvxE' \
  --compressed


