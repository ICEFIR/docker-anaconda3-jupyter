# Code modified from https://hub.docker.com/r/continuumio/anaconda3/dockerfile && https://github.com/luojiahai/XAI-Playground
FROM continuumio/anaconda3

RUN /opt/conda/bin/conda install jupyter -y --quiet && \ 
    mkdir /opt/notebooks && \
    /opt/conda/bin/jupyter notebook --generate-config

COPY configgen.py /root/

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]
 