# 微信32位兼容启动器 (WeChat3.9-32bit-Compatibility-Launcher)

## 📢 项目简介
这是一个简单但实用的工具，**让微信3.9.12 32位版本能够在64位Windows 10+操作系统上正常运行，并且不显示"版本过低"的提示**。

## 🚨 背景情况
- 微信官方已发布**WeChat 4.0 x64**版本，并**禁止所有3.9.x 64位版本登录**。
- **微信3.9.12 32位版本(x86)** 在**32位系统**上仍可正常登录和收发消息，并且没有任何后续更新。
- 但在**64位系统**上运行**微信3.9.12 32位版本时**，会**提示"版本过低"**，无法正常完成登录。

## ✅ 测试环境
- 微信版本：3.9.12.54 (32位)，3.9.12.56 (32位)
- 操作系统：Windows 10 17763 64位 （1809），Windows 10 1904x 64位 （2004-22H2），Windows 11 26x00 64位 （24H2-25H2）
- 状态：**完美运行完美登录，无版本过低提示**

## 🔧 工作原理
本工具通过设置**兼容性环境变量** `__COMPAT_LAYER=~ ARM64WOWONAMD64` 来启动微信，使32位微信能够在64位系统上正常运行而不被识别为过时版本。

## 📥 下载链接

### 微信32位官方安装包
- **官方下载**: [https://dldir1v6.qq.com/weixin/Windows/WeChatSetup_x86.exe](https://dldir1v6.qq.com/weixin/Windows/WeChatSetup_x86.exe)
- **备用链接**: [https://github.com/tom-snow/wechat-windows-versions-x86/releases](https://github.com/tom-snow/wechat-windows-versions-x86/releases)

### 本程序（32位启动器）下载
[点击此处下载启动器](https://github.com/Skyler1n/WeChat3.9-32bit-Compatibility-Launcher/releases)

## 📋 使用方法（三选一）

### 方法一：使用可执行文件（推荐）
1. 下载 `wechat_starter.exe`
2. 将其**复制到微信主程序所在目录**（与 `WeChat.exe` 同目录）
3. 双击运行 `wechat_starter.exe`
4. 微信将自动启动，且不会显示版本过低提示

### 方法二：使用批处理文件
1. 创建一个文本文件，命名为 `启动微信.bat`
2. 编辑内容如下：
   ```batch
   @echo off
   set "__COMPAT_LAYER=~ ARM64WOWONAMD64"
   start "" "WeChat.exe"
   ```
3. 将 `启动微信.bat` 保存到微信主程序所在目录
4. 双击运行此批处理文件

### 方法三：使用注册表（永久生效）
1. 创建一个文本文件，命名为 `微信兼容.reg`
2. 编辑内容如下（**请将路径修改为你的微信安装路径**）：
   ```
   Windows Registry Editor Version 5.00

   [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers]
   "D:\\Tencent\\WeChat\\WeChat.exe"="~ ARM64WOWONAMD64"
   ```
3. 保存文件后双击导入注册表
4. 之后直接运行微信即可，无需其他操作

## ⚠️ 注意事项
- 此工具仅适用于**微信3.9.12 32位版本**
- 对于方法三（注册表），请确保正确修改微信安装路径
- 若微信更新后此方法失效，可能需要寻找其他解决方案
- 本工具不兼容Windows 7和Windows 8.x，理论兼容Windows 10 1809+（17763）

## 🛠️ 构建指南
### 环境要求
- Python 3.12
- Nuitka 2.7.14

### 构建步骤
1. 克隆本仓库
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行构建脚本：
   ```bash
   python build.py
   ```
4. 构建完成后，可执行文件将生成在 `dist` 目录中

## 📁 项目文件说明
- `wechat_starter.py`: 主程序源代码
- `build.py`: 构建脚本
- `requirements.txt`: 依赖列表
- `WeChat.ico`: 程序图标

## 📝 许可证
本项目采用 MIT 许可证 - 详情请查看 LICENSE 文件

## ⚠️ 重要免责声明

**本工具仅供技术研究和学习交流使用，请在下载后24小时内删除。使用者需自行承担所有风险和责任。**

### 法律声明
- 本项目与腾讯公司、微信官方无任何关联
- 微信是腾讯公司的注册商标，相关版权归腾讯所有
- 本工具不涉及任何代码修改、逆向工程或破解行为
- 仅通过系统兼容性设置实现功能，不修改微信核心文件
- 作者不对因使用本工具导致的任何法律问题负责
- 请支持正版软件，遵守软件使用协议

## ❤️ 贡献
欢迎提交 Issue 和 Pull Request！
