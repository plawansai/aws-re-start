printf("Using os.system")
import os
os.system("ls")

printf("\nUsing subprocess.run")
import subprocess
subprocess.run(["ls"])

# Using subprocess.run with two arguments
subprocess.run(["ls","-l"])

# Using subprocess.run with three arguments
subprocess.run(["ls","-l","README.md"])

# Retrieving system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# 
