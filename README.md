# anaconda3-jupyter
Instantly deploy jupyter notebook with anaconda3  

## Usage  

Make sure docker and docker-compose are installed
```git clone https://github.com/ICEFIR/docker-anaconda3-jupyter  
cd docker-anaconda3-jupyter  
docker-compose up -d
```

Default password - password  
You can modify the docker-compose file to change it, along with other settings such as ports, etc  

## Credit
Mostly modified from Anaconda3 official docker image and my friend's work :)  
Official Ananconda Docker  
  https://hub.docker.com/r/continuumio/anaconda3/dockerfile 
My friends walkthrough of installing Jupyter Notebook and Anaconda3 on Docker  
  https://github.com/luojiahai/XAI-Playground
