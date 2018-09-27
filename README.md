# Penny API [![CircleCI](https://circleci.com/gh/ethanyanjiali/penny-api/tree/master.svg?style=svg)](https://circleci.com/gh/ethanyanjiali/penny-api/tree/master)

Penny (http://mypenny.co) is a free tool to help people split complicated group expenses with their friends. The service is launched in 2016 and 
getting more and more popular nowadays because it's so easy to use. Not like other group expense tool, Penny doesn't
require sign up or login. You just need to share the URL to your friends, then everyone can start filling the expense they paid 
from their own device. In the meantime, the settlement will be calculated automatically to guide you how to pay out.

In order to make it not only free for users, but also for developers, I've open sourced this project in 2018. This backend service is running 
on Google Cloud.

## Devlopement

1. Make sure Python 3.7.0 is installed
0. Setup virtualenv
    ```bash
    python3 -m venv env
    ```
0. Activate virtual env
    ```bash
    source ./env/bin/activate
    ```
0. Download dependencies
    ```bash
    pip install -r requirements.txt
    ```
0. Start server
    ```bash
    ./scripts/debug.sh
    ```
0. Deactivate after development
    ```bash
    deactivate
    ```

## Deployment

This project use Circle CI to build and publish the docker image, and then update the Google Compute
Engine with the new container image. 

I built a custom image which contains both gcloud-sdk and python3.7 here
```
https://hub.docker.com/r/liyanjia92/gcloudpython/
```
Circle CI will pull this image, authenticate through gcloud with the JSON key of the service account, then 
download the instance config for the app. Next, docker will build a new image for the project, login with GCP JSON 
key, then push to gcr.io (Google Container Registry) 

If you need to deploy manually
1. Make sure Docker is installed
0. Make sure `gcloud` is also installed
0. Build the image
    ```bash
    docker build -t penny-api:$(git log -1 --pretty=%h) .
    ```
0. Run a container with this image for testing
    ```bash
    docker run -p 80:8000 penny-api:$(git log -1 --pretty=%h)
    ```
0. GET `http://localhost/common/lang` to ensure the container runs correctly
0. Push the image to gcr.io
    ```bash
    docker push gci.io/mypennyco/penny-api:$(git log -1 --pretty=%h)
    ```

Basically, I use gunicorn and nginx to start a web server on Google Compute Engine

1. Log onto the instance (there's only one)
0. Pull master
0. Stop previous service 
    ```bash
    ./scripts/stop.sh
    ```
0. Start the new service again
    ```bash
    ./scripts/start.sh
    ```
0. If you need to restart Nginx
    ```bash
    sudo service nginx restart
    ```
    
## TODO

- Dockerize