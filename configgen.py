# To generate password and overwrite setting manully
from notebook.auth import passwd 
import os,re

config_path = os.path.expanduser('~/.jupyter/jupyter_notebook_config.py')
hashed = passwd(os.environ['jupyter_password'])
base_url = os.environ['base_url']
with open(config_path,'r') as f:
  content = f.read()
overwrite_base_url = re.sub(r"^.*c\.NotebookApp\.base_url .*\n", f"c.NotebookApp.base_url = '{base_url}'",content,flags=re.M)
overwrite_password = re.sub(r"^.*c\.NotebookApp\.password .*\n", f"c.NotebookApp.password = u'{hashed}'",overwrite_base_url,flags=re.M)

#  print (overwrite_password)
#  print(re.findall(r"^.*c\.NotebookApp\.password .*\n",content,flags=re.M))
with open(config_path,'w') as f:
  f.write(overwrite_base_url)
