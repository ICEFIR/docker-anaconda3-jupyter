# To generate password and overwrite setting manully
from notebook.auth import passwd 
import os,re

config_path = os.path.expanduser('~/.jupyter/jupyter_notebook_config.py')
hashed = passwd(os.environ['jupyter_password'])
base_url = os.environ['base_url']
with open(config_path,'r') as f:
  content = f.read()
overwite = re.sub(r"^.*c\.NotebookApp\.baseurl .*\n", f"c.NotebookApp.baseurl = '{base_url}'",content,flags=re.M)
overwite = re.sub(r"^.*c\.NotebookApp\.password .*\n", f"c.NotebookApp.password = u'{hashed}'",content,flags=re.M)

#  print(re.findall(r"^.*c\.NotebookApp\.password .*\n",content,flags=re.M))
with open(config_path,'w') as f:
  f.write(overwite)
