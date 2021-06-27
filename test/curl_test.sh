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
  -H 'cookie: access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNDcyNTg1OCwianRpIjoiZjAxNjdiZWItMzI0Ny00YjJmLWFkMzctOTQ4MmQ4MmE4MDYxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6bnVsbCwibmJmIjoxNjI0NzI1ODU4LCJjc3JmIjoiMjExYjBjOGItYWViNi00NDVlLTlhYWItODgxMGUyZWU2MjE4IiwiZXhwIjoxNjI0NzI5NDU4fQ.axJjJJIUfsh3TGJ21T9OIPzpbWqSESFLJelZi1cyiyw' \
  --compressed


