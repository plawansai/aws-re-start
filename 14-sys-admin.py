print("Using os.system")
import os
os.system("ls")

print("\nUsing subprocess.run")
import subprocess
subprocess.run(["ls"])

print("\nUsing subprocess.run with two arguments")
subprocess.run(["ls","-l"])

print("\nUsing subprocess.run with three arguments")
subprocess.run(["ls","-l","README.md"])

print("\nRetrieving system information")
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])


