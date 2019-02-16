# anaconda3-jupyter docker-compose
Docker compose file to deploy Anaconda 3 and jupyter notebook instantly, with read-to-use browser access :)  

## Usage  

Make sure docker and docker-compose are installed
```   
git clone https://github.com/ICEFIR/docker-anaconda3-jupyter  
cd docker-anaconda3-jupyter  
echo -n Password: && read -s password && export jupyter_password=$password && echo
# Or an other methods that can set env variable jupyter_password securely
docker-compose up -d
```   
It can take a while to deploy, so please be patient :)  

Note if jupyter_password environment is set to empty string, previous record will be kept (assuming containers were not removed).
To disable and remove password, set env variable disable_password to 1 and restart the image
`export disable_password=1 && docker-compose stop && docker-compose start`


You can modify settings base url, ports in the docker-compose  
Run the following command to apply changes :)  
```docker-compose stop && docker-compose start```     
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
