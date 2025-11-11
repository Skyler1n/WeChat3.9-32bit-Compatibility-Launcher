import os
import subprocess
import sys

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# 构建微信可执行文件的完整路径
wechat_exe_path = os.path.join(script_dir, "WeChat.exe")

# 设置兼容性环境变量
env = os.environ.copy()
env["__COMPAT_LAYER"] = "~ ARM64WOWONAMD64"

# 启动微信，使用CREATE_NO_WINDOW标志隐藏命令窗口
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

# 启动微信进程
subprocess.Popen(
    [wechat_exe_path],
    env=env,
    startupinfo=startupinfo,
    shell=False
)

# 程序自动退出