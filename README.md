# anaconda3-jupyter
Instantly deploy jupyter notebook with anaconda3, with read-to-use browser access :)  

## Usage  

Make sure docker and docker-compose are installed
```   
git clone https://github.com/ICEFIR/docker-anaconda3-jupyter  
cd docker-anaconda3-jupyter  
export enable_password=1 && echo -n Password: && read -s password && export jupyter_password=$password && echo
# Or an other methods that can set env variable jupyter_password securely
docker-compose up -d
```   
It can take a while to deploy, so please be patient :)  

Note if jupyter_password environment is set to '', previous record will be kept (assuming containers were not removed).
To disable password and use a token, set enable_password to 0


You can modify settings base url, ports in the docker-compose  
Run the following command to apply changes :)  
```docker-compose stop && docker-compose up -d```     
Example of base url:   
  \- base_url='https://www.example.com/notebook'   
  \- base_url='/notebook'    
  \- base_url='/'



## Note
This is intended to be used behind nginx reverse proxy, thus no SSL is included  
Using SSL is highly recommanded, unless you just want to use it over LAN :)


## Credit
Mostly modified from Anaconda3 official docker image and my friend's work :)  
Official Ananconda Docker  
  https://hub.docker.com/r/continuumio/anaconda3/dockerfile  
My friends walkthrough of installing Jupyter Notebook and Anaconda3 on Docker  
  https://github.com/luojiahai/XAI-Playground  
