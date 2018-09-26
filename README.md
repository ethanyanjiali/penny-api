# Penny Backend Service

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
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04

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
