from os import listdir, path as os_path
from tqdm import tqdm
from subprocess import Popen, PIPE

root_path = r"D:\file\普通话"
exts = ["mp4"]

commands = []
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
for command in tqdm(commands):
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
