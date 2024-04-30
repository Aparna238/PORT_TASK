import subprocess
import os 

workspace = os.getcwd

with open('bash_script.sh', 'w') as batch_file:
                batch_file.write('#!/bin/bash\n') 
                batch_file.write('echo "Hello World"\n')  
                batch_file.write('echo "Hello World" > log.txt\n')  
subprocess.run(["bash", workspace+"/bash_script.sh"])