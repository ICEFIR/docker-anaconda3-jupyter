# To generate password and overwrite setting manully
from notebook.auth import passwd 
import os,re
print("Generating config")
config_path = os.path.expanduser('~/.jupyter/jupyter_notebook_config.py')

with open(config_path,'r') as f:
  content = f.read()

if "disable_password" in os.environ and os.environ['disable_password'] == '1':
  print("disabling password")
  content = re.sub(r"^.*c\.NotebookApp\.password .*\n", f"#c.NotebookApp.password = u''",content,flags=re.M)
else:
  print("detecting password")
  if "jupyter_password" in os.environ and os.environ['jupyter_password'] != '':
    print("Password found. configurating hashed password with jupyter")
    hashed = passwd(os.environ['jupyter_password'])
    os.environ['jupyter_password'] = "" # Reset password env for security reasons
    content = re.sub(r"^.*c\.NotebookApp\.password .*\n", f"c.NotebookApp.password = u'{hashed}'\n",content,flags=re.M)
  else:
    print("No password is specified. Will run jupyter in token mode")
if "base_url" in os.environ:
  print("Configurating base url")
  base_url = os.environ['base_url']
  content = re.sub(r"^.*c\.NotebookApp\.base_url .*\n", f"c.NotebookApp.base_url = {base_url}\n",content,flags=re.M)

# print(re.findall(r"^.*c\.NotebookApp\.base_url .*\n",content,flags=re.M))
with open(config_path,'w') as f:
  print("Writing changes to config file")
  f.write(content)

# Launch jupyter book from here to prevent a password leak
print("Attempting to launch jupyter")
try:
  os.system("/opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='0.0.0.0' --port=8888 --no-browser --allow-root")
except:
  print("Unexpected error:", sys.exc_info()[0])
  sys.exit("Unable to startup jupyter")
