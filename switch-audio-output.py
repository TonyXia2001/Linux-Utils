import subprocess

process = subprocess.Popen(["pacmd", "list-sinks"],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
stdout = stdout.decode('utf-8')
stdout = stdout.split('\n')
stdout = [e for e in stdout if "index:" in e]
i = -1
for e in stdout:
    if "*" in e:
        i = int(e.split(':')[1])
        break
# switch to the next sink
i -= 1
i = (i + 1) % len(stdout)
i += 1

print(f'switching to sink #{i}')
subprocess.call(["pacmd", "set-default-sink", str(i)])