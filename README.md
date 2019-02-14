# anaconda3-jupyter
Instantly deploy jupyter notebook with anaconda3, with read-to-use browser access :)  

## Usage  

Make sure docker and docker-compose are installed
```   
git clone https://github.com/ICEFIR/docker-anaconda3-jupyter  
cd docker-anaconda3-jupyter  
docker-compose up -d
```   

Default password - password  
You can modify it in docker-compose file, along with other settings such as ports, etc  
Run the following command to apply changes :)  
```docker-compose down && docker-compose up -d```  

## Note
This is intended to be used behind nginx reverse proxy, thus no SSL is included  
Using SSL is highly recommanded, unless you just want to use it over LAN :)


## Credit
Mostly modified from Anaconda3 official docker image and my friend's work :)  
Official Ananconda Docker  
  https://hub.docker.com/r/continuumio/anaconda3/dockerfile  
My friends walkthrough of installing Jupyter Notebook and Anaconda3 on Docker  
  https://github.com/luojiahai/XAI-Playground  
