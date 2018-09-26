# Penny Backend Service

## About Penny

Penny (http://mypenny.co) is a free tool to help people split complicated group expenses with their friends. The service is launched in 2016 and 
getting more and more popular nowadays because it's so easy to use. Not like other group expense tool, Penny doesn't
require sign up or login. You just need to share the URL to your friends, then everyone can start filling the expense they paid 
from their own device. In the meantime, the settlement will be calculated automatically to guide you how to pay out.

In order to make it not only free for users, but also for developers, I've open sourced this project in 2018. This backend service is running 
on Google Cloud.

## Devlopement

0. Make sure Python 3+ is installed
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

The deployment follows this article
```https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04```

Basically, I use gunicorn and nginx to start a web server on Google Compute Engine

0. Log onto the instance (there's only one)
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
- Continuous Integration
