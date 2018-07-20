# fog_computing
This is a project to implement Fog computing using the Cisco IR829 router
This repository contains  two major files:
Django Rest API based server, to which the end devices can send data to and a processing file, which processes the data on the router and send useful status reports to Firebase.
Both the server and the Processing file need to be Dockerized and a deployable package.tar file needs to be built, for which relevant Dockerfiles and package.yaml files are also written.
