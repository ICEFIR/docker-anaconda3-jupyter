# anaconda3-jupyter
Instantly deploy jupyter notebook with anaconda3, with read-to-use browser access :)  

## Usage  

Make sure docker and docker-compose are installed
```   
git clone https://github.com/ICEFIR/docker-anaconda3-jupyter  
cd docker-anaconda3-jupyter  
docker-compose up -d
```   
It can take a while to deploy, so please be patient :)   

Default password - password  
You can modify it in docker-compose file, along with other settings such as ports,base url etc  
Run the following command to apply changes :)  
```docker-compose down && docker-compose up -d```     

Example of base url:   
  - base_url='https://www.example.com/notebook'
or  
  - base_url='/notebook'   

## Note
This is intended to be used behind nginx reverse proxy, thus no SSL is included  
Using SSL is highly recommanded, unless you just want to use it over LAN :)


## Credit
Mostly modified from Anaconda3 official docker image and my friend's work :)  
Official Ananconda Docker  
  https://hub.docker.com/r/continuumio/anaconda3/dockerfile  
My friends walkthrough of installing Jupyter Notebook and Anaconda3 on Docker  
  https://github.com/luojiahai/XAI-Playground  
