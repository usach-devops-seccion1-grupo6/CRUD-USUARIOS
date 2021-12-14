#!/bin/bash

if [ ! -d "migrations" ]
then
    flask db init
    flask db migrate
    flask db upgrade
fi

export APP_SETTINGS=app.config.Production
waitress-serve --port=5000  --call 'entrypoint:create_app'
