# uno
An uno game created for the final project of CS 333 (Testing and DevOps) at UNR in Spring 2023. This project contains an uno game built in python, with automated unit and integration testing upon commit as well as automated building and deployment of a docker image.

## Automated Testing
This repository is setup to automatically run a suite of unit and integration tests upon commit. The results of the tests can be viewed by clicking the "Actions" tab and then viewing the "Automated Testing" workflow. Or, you can just click [this link.](https://github.com/bertauchekurtis/uno/actions/workflows/autoTestingScript.yml)

A .coverage file is also hosted in this repository with the results of running:
```
coverage run -m unittest discover
```
The .coverage file results can be viewed by downloading/cloning this repository onto an environment that has both Python 3 and the Coverage module and then running the following command:
```
coverage report
```
## Automated Deployment
After a commit to this repository the automated test suite is run. Upon succesful completion of all of the tests, a new docker image is created and pushed to docker hub. You can see the image on docker hub at [this link.](https://hub.docker.com/repository/docker/bertauchekurtis/uno/general)

## Running the Application
### With Python
Requirements: Python 3 - unittest and coverage libraries also if you want to run the tests.

Download/Clone this repository and run the game with the following command:
```
python main.py
````
### With Docker
Requirements: Docker is downloaded and installed.

Download/Pull the uno image from DockerHub with the following command:
```
docker pull bertauchekurtis/uno
```
Run the docker image with the following command:
```
docker run -ti uno
```
Having issues with the docker image not being found locally? Try this one instead:
```
docker run -ti bertauchekurtis/uno
```
