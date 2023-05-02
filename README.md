# uno
An uno game created for the final project of CS 333 (Testing and DevOps) at UNR in Spring 2023. This project contains an uno game built in python, with automated unit and integration testing upon commit as well as automated building and deployment of a docker image.
***
## **Automated Testing**
This project has been unit and integration tested using the unittest module in Python. Those unit and integration tests have then been integrated into a GitHub actions workflow to automatically be run everytime a commit is made to this repository.

### **Testing in GitHub**
Instructions for Testing the Code on GitHub:

1. Make a commit to this repository. There is a GitHub actions workflow setup that will run all of the unit and integration tests. The results of the tests can be found by going to the Actions tab in this repository, which is [also linked here.](https://github.com/bertauchekurtis/uno/actions/workflows/autoTestingScript.yml)
2. To see the results in detail, click on the most recent commit, and then click on any of the "test" jobs in the "Jobs" list. You can then view any of the individual steps and see the commands run within the GitHub runner and the output from the testing.
3. After ***successfull*** completion of all tests, the workflow will then build and push a docker image to docker hub, [see the section on deployment](#automated-deployment) for more information.

### **Testing Locally**
Instructions for Testing the Code Locally:

1. Download/clone the repository.
2. Ensure you have Python 3, the unittest module, and the [coverage module](https://coverage.readthedocs.io/en/7.2.5/) installed.
3. Run the following command to run all of the unit and integration tests:
```
coverage run -m unittest discover
```
4. After running this command, you will see the results of running the tests. There are 44 tests, and you will see "OK" if they all completed succesfully.
5. You can also view more detailed information about the coverage of individual modules by using the following command:
```
coverage report
```
6. This coverage report is stored in the .coverage file that is already contained in this repository, so it can be viewed without having to re-run the tests
***
## **Automated Deployment**

This repository is setup to automatically deploy the application upon commit and successful testing. In more detail, the process looks like this:

1. A commit is made to this repository
2. The [GitHub actions workflow](https://github.com/bertauchekurtis/uno/actions/workflows/autoTestingScript.yml) automatically runs a suite of unit and integration tests.
3. Upon ***succesfull*** completion of ***all*** of the unit and integration tests, the GitHub actions workflow will execute a job that will build and deploy the app.
4. The GitHub actions workflow will build a docker image using the Dockerfile found in the repository.
5. After building the Dockerfile, it will be automatically pushed to a repository on docker hub where the application, ready to run in a docker container, is hosted. You can [find it here.](https://hub.docker.com/repository/docker/bertauchekurtis/uno/general)

***
## **Running the Application**

### **Using Docker**
Instructions for how to run the app with Docker:
1. Ensure that you have Docker installed
2. Pull the Docker image from Docker Hub with the following command:
```
docker pull bertauchekurtis/uno
```
3. Run the Docker image with the following command (the -ti flag is required to run the image in interactive mode to allow you to interact with the program and play uno):
```
docker run -ti bertauchekurtis/uno
```
### **With Python**
Instructions for how to run the app with Python:
1. Ensure that you have Python 3 installed.
2. Download/clone this repository.
3. Run the application with the following command:
```
python main.py
```