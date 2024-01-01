#! /bin/bash

curl -X POST -H "Content-Type: application/json" -d "{\"id\":\"001\",\"name\":\"A\",\"age\":\"10\",\"address\":\"Tokyo\",\"tel\":\"090-1111-1111\"}" $URL
curl -X POST -H "Content-Type: application/json" -d "{\"id\":\"002\",\"name\":\"B\",\"age\":\"20\",\"address\":\"Osaka\",\"tel\":\"090-2222-2222\"}" $URL
curl -X POST -H "Content-Type: application/json" -d "{\"id\":\"003\",\"name\":\"C\",\"age\":\"30\",\"address\":\"Nagoya\",\"tel\":\"090-3333-3333\"}" $URL
