# 微信32位兼容启动器 (WeChat3.9-32bit-Compatibility-Launcher)

## 📢 项目简介
这是一个简单但实用的工具，**让微信3.9.12 32位版本能够在64位Windows操作系统上正常运行，并且不显示"版本过低"的提示**。

## 🚨 背景情况
- 微信官方已发布4.0 x64版本，并**禁止所有3.9.x 64位版本登录**
- 但**微信3.9.12 32位版本(x86)** 在32位系统上仍可正常登录
- 当在64位系统上运行微信3.9.12 32位版本时，会**提示"版本过低"**

## ✅ 测试环境
- 微信版本：3.9.12.56 (32位)
- 操作系统：Windows 10 1904x 64位
- 状态：**完美运行，无版本过低提示**

## 🔧 工作原理
本工具通过设置**兼容性环境变量** `__COMPAT_LAYER=~ ARM64WOWONAMD64` 来启动微信，使32位微信能够在64位系统上正常运行而不被识别为过时版本。

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

## ❤️ 贡献
欢迎提交 Issue 和 Pull Request！