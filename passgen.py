# To generate password and overwrite setting manully
from notebook.auth import passwd 
import os,re

config_path = os.path.expanduser('~/.jupyter/jupyter_notebook_config.py')
hashed = passwd(os.environ['jupyter_password'])

with open(config_path,'r') as f:
  content = f.read()

overwite = re.sub(r"^.*c\.NotebookApp\.password .*\n", f"c.NotebookApp.password = u'{hashed}'",content,flags=re.M)
#  print(re.findall(r"^.*c\.NotebookApp\.password .*\n",content,flags=re.M))
with open(config_path,'w') as f:
  f.write(overwite)
