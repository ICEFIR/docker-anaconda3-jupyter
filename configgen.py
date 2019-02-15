# To generate password and overwrite setting manully
from notebook.auth import passwd 
import os,re

config_path = os.path.expanduser('~/.jupyter/jupyter_notebook_config.py')

with open(config_path,'r') as f:
  content = f.read()

if "enable_password" in os.environ and os.environ['enable_password'] == '1':
  if "jupyter_password" in os.environ and os.environ['jupyter_password'] != '':
    hashed = passwd(os.environ['jupyter_password'])
    content = re.sub(r"^.*c\.NotebookApp\.password .*\n", f"c.NotebookApp.password = u'{hashed}'\n",content,flags=re.M)
else:
  content = re.sub(r"^.*c\.NotebookApp\.password .*\n", f"#c.NotebookApp.password = u''\n",content,flags=re.M)

if "base_url" in os.environ:
  base_url = os.environ['base_url']
  content = re.sub(r"^.*c\.NotebookApp\.base_url .*\n", f"c.NotebookApp.base_url = {base_url}\n",content,flags=re.M)

# print(re.findall(r"^.*c\.NotebookApp\.base_url .*\n",content,flags=re.M))
with open(config_path,'w') as f:
  f.write(content)
