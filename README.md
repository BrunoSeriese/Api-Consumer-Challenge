# coding-Challenge-API 

## Interpretation

I'm assuming that for every function I will have a list of hosts that i will have to loop over. So in my implementation i use a for loop over the amount of hosts.
I assumed that a rollback would only be neccesary on create and delete actions, and so I have not implemented this for the getGroup()
Since i do not have access to the API i assumed that i should mock the API for the testing with pytest.

I wasn't sure what to do with the main execution of main.py since there isnt an actual API, so for now i just let it print something to showcase that it can run. The testing should showcase that the functions actually work.


I assumed it would be good to add docstrings to clarify my functions so that it is easy to understand, and to use a formatter to make it in line with pep8


## Requirements

For running without Docker/Kubernetes:
- Python 3.x
- requests
- pytest
- pytest-mock
- httpx

For running the module with Docker/Kubernetes:
- Docker
- Kubernetes

## Installation

Clone the repository:
```
git clone https://github.com/BrunoSeriese/Api-Consumer-Challenge.git
```

## Manual Docker Image and Container Execution

To manually run the Docker image and container:

1. Build the Docker image:
```
docker build -t  test1app .
```

2. Run the Docker container:
```
docker run -it test1app
```

## Manual Pytest Execution

To manually run pytest:

1. Build the Docker image for pytest:
```
docker build -t test1app-ci -f Dockerfile.ci .
```

2. Run the Docker container for pytest:
```
docker run -it test1app-ci
```

## Kubernetes Service Deployment


To start the Kubernetes service:

1. Apply the Kubernetes manifests:
```
kubectl apply -f manifests/
```

2. Check the service status:
```
kubectl get service code-challenge
```

---
