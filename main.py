import subprocess
from os import listdir, path as os_path


root_path = r"D:\file\普通话1"
exts = ["mp4"]

commands = [f"cd {root_path}"]
for i in listdir(root_path):
    dir = os_path.join(root_path, i)
    if not os_path.isfile(dir):
        continue
    ext = dir.rsplit(".", 1)[1]
    if ext not in exts:
        continue
    commands.append(
        f'whisper "{dir}" --model medium --language Chinese --initial_prompt "以下是普通话的句子。" --output_dir {root_path} --output_format txt'
    )


# 执行多条命令行指令
for command in commands:
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, error = process.communicate()
