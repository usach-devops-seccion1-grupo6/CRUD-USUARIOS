#!/bin/bash

RAN=$(echo $RANDOM | md5sum | head -c 20)
echo $RAN
curl -X POST -H "Content-Type: application/json" -d "{
    \"nombre\": \"$(echo $RAN) $(echo $RAN)\",
    \"email\": \"$(echo $RAN)@test.cl\",
    \"clave\": \"$(echo $RAN)_A\"
}" http://localhost:5000/api/v1.0/usuarios