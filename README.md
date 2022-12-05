# PYQ_Like
利用pyautogui的非常简单的朋友圈自动点赞（前台）脚本

# 原理
1. 利用pyautogui的图像识别功能，打开电脑微信朋友圈
2. 寻找那两个点，点击后判断是否赞过。没赞过就点赞
3. 自动下滑（目前的功能只能滑动固定的距离）

# 如何使用
1. 克隆本仓库，或者在右上角的`<> Code`处直接下载zip
2. 使用python运行`PYQlike_pyautogui.py`
  - 如何使用python运行，请自行百度/谷歌

# 要求
- python3
- 安装过pyautogui
`pip install pyautogui`
- 图片和py文件在同一个文件夹下，而且不能改名（会修改的可以自己改）
