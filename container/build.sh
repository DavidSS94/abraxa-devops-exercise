#!/bin/bash
tar --exclude ".git/" --exclude "node_modules/" -cvf app.tar ../
docker build -t $1 .
rm -f app.tar
