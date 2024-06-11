"# Api-Consumer-Challenge" 





To manually run the docker image and container:

#1: docker build -t  test1app .
#2: docker run -it test1app 


To manually run the pytest:

#1: docker build -t test1app-ci -f Dockerfile.ci .
#2: docker run -it test1app-ci 



To start the kubernetes 


kubectl apply -f manifests/