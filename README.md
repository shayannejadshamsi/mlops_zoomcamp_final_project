## mlops_zoomcamp_final_project


# Customer Churn Prediction

# Problem statement

The aim of this project is to predict if a customer is leaving or not the bank based on several factors like age, gender, etc. The main focus of this project is to build a model to predict it, log the model artifacts in the register service and deploy it.



# Schematic diagram

![Untitled](C:\Users\s_nejads\OneDrive - Concordia University - Canada\Desktop\project\images\Untitled.jpg)



# Procedure

Follow the steps below to reproduce and build the model.



# Environment

## Create a conda enviroment for the project with python=3.9
```sh
conda create -n mlops python=3.9
```
## Active the enviroment
```sh
conda activate mlops
```
## Install the dependencies
```sh
pip install -r requirements.txt
```


# Model: Classification model to predict customer retention



## Dataset: Customer Churn Dataset

Download dataset [here](https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset)



## Working on [model.ipynb](notebooks/model.ipynb)

### Install ipython kernel
```
conda install -n project_enviroment ipykernel --update-deps --force-reinstall
```



# Tracking Experiment with mlflow

Run the following command in your terminal to track the experiment in your local machine:

```sh
mlflow ui --backend-store-uri sqlite:///mydb.sqlite
```
This command create a database file called mydb.sqlite in the current directory that'll be used to store the experiment data.

```python
mlflow server
mlflow ui
```

and now we can access the mlflow GUI on "127.0.0.1:5000" 



# Orchestration of the project
A [Prefect==2.7.3](https://prefect.io/) is used to orchestrate the project

## Starting prefect

```sh
Prefect server start
```

## Build the deployment

```sh
prefect deployment build .\model.py:applying_model --name mlops-deployment --tag mlops
```


## Apply the deployment

```sh
prefect deployment apply applying-deployment.yaml
```


## Agents

We need to set an agent to run the deployment. Agents pick up work from queues and execute the flows

## Start an agent

```
prefect agent start -t mlops
```

We can check the Prefect GUI in the address "127.0.0.1:4200"



# Monitoring

**Evidently**, **Whylogs** and **Streamlit** are used to monitor the experiment and dashboard respectively.



To run Evidently and Streamlit we run docker-compose and open their GUI there.

`docker-compose -f ./docker-compose.yaml up`

We can access the GUI of Evidently and Streamlit by clicking on their corresponding ports in Docker desktop.



## Evidently
## Dashboard for classification report
This report evaluates the quality of a classification model. It works both for binary and multi-class classification. Using train data and valid data to evaluate the model I've created a dashboard which the results can be seen in the [`dashboard`](dashboards/df_model_performance.html) folder.



## Whylogs

To set up the Whylog, enter the https://whylabs.ai/ create account and then create a "classification" model. In the next step, in the "setting" and then "Access Token" section, we should copy the "API token", "organization id" and "model id" into our model.py code. 




## Streamlit
We can make a Streamlit app using our model. We'll use the last model we trained. This model will be at `models` folder.



# Tests

I'll use Pytest to test the model.

Install pytest with the following command:

```
pip install pytest
```

## Configure Tests

1. Go to `tests` extension in VS Code and select a folder that contains the tests, in this case `tests/`.
2. Select `Pytest` as the test runner.

# Makefiles and Make

Make is a tool which controls the generation of executables and other non-source files of a program from the program's source files. Make gets its knowledge of how to build your program from a file called the makefile, which lists each of the non-source files and how to compute it from other files. When you write a program, you should write a makefile for it, so that it is possible to use Make to build and install the program.

## Install make with the following command:

```
sudo apt install make
```

or if you are using Windows, you can install make with the following command (as a administrator):

```
choco install make
```

where `choco` is the command to install chocolatey packages.

## Example:

```
test:
	echo test

other_thing:
	echo other thing

run: test other_thing
	echo run
```

## Run make with the following command:

```
make run
```

# 

# CI/CD

## Github actions

Github actions is a service that allows us to run our code in a virtual machine. We can use this service to run our code when we push our code to Github. We can also use this service to run our code when we create a pull request.

## [Testing workflow](.github/workflows/testing.yaml)

I've created a workflow to test the code. Basically, this workflow will run the following commands:

1. Install the requirements.
2. Run the tests.

## [Continuous training workflow](.github/workflows/continuous_training.yaml)

This workflow will run the following commands:

1. Install the requirements.
2. Run the model
3. Push the new model to the repository.
4. This workflow will run every day (6 hours after the last run).

