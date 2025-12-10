import subprocess
import shlex


log_file = "replay_output.txt"


with open("api_requests", "r") as f:
raw = f.read()


# split by blank lines → individual curl blocks
blocks = [b.strip() for b in raw.split("\n\n") if b.strip()]


with open(log_file, "w") as log:
for i, block in enumerate(blocks, 1):
log.write(f"\n===== REQUEST {i} =====\n")
log.write(block + "\n")
log.write("----- RESPONSE -----\n")


cmd = block.replace("$TOKEN", subprocess.getoutput("echo $TOKEN"))
try:
result = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
log.write(result.decode(errors="ignore") + "\n")
except Exception as e:
log.write(str(e) + "\n")


print("Replay complete. See replay_output.txt")
