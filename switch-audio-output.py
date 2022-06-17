import subprocess

process = subprocess.Popen(["pacmd", "list-sinks"],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
stdout = stdout.decode('utf-8')
stdout = stdout.split('\n')
stdout = [e for e in stdout if "index:" in e]
next = -1
for i, e in enumerate(stdout):
    if "*" in e:
        next = (i+1) % len(stdout)
        
# switch to the next sink
i = stdout[next].find("index: ")
i = int(stdout[next][i+7:])

print(f'switching to sink #{i}')
subprocess.call(["pacmd", "set-default-sink", str(i)])