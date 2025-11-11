import os
import subprocess
import sys

# 确保dist目录存在
dist_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
os.makedirs(dist_dir, exist_ok=True)

# Nuitka编译命令
cmd = [
    sys.executable,
    "-m", "nuitka",
    "--onefile",
    f"--output-dir={dist_dir}",
    "--windows-console-mode=disable",
    "--windows-icon-from-ico=WeChat.ico",
    "--windows-file-description=WeChat",
    "--windows-file-version=3.9.12.56",
    "--windows-product-name=微信启动器",
    "--windows-product-version=3.9.12.1000",
    "wechat_starter.py"
]

print("开始编译程序...")
try:
    # 运行编译命令
    subprocess.run(cmd, check=True)
    print(f"编译完成！可执行文件位于：{dist_dir}")
except subprocess.CalledProcessError as e:
    print(f"编译失败：{e}")
    sys.exit(1)