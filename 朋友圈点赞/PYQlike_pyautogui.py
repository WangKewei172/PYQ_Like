# 开发者:wkw
# 开发时间：2022/11/16 8:22
import pyautogui

''' 要求：
    - 微信已在任务栏打开
    
    TODO：
    - [ ] 计算最上方的两点到顶部的距离，直接下拉该距离，精准赞每一个pyq。
'''
pyautogui.FAILSAFE = True # 鼠标移动到0,0坐标点的时候会强行停止，即最左上角
pyautogui.PAUSE = 0.5 # 执行pyautogui命令时，会停顿0.5秒，免得太快。可以设置短一点

# 打开任务栏的微信
wxCenter = pyautogui.center(pyautogui.locateOnScreen('wx.png')) #获取屏幕上微信程序的位置
pyautogui.moveTo(wxCenter)  #把鼠标移过去
pyautogui.click()

#进入朋友圈
pyqIconCenter = pyautogui.locateCenterOnScreen('pyqIcon.png')   #获取位置
pyautogui.moveTo(pyqIconCenter)  #把鼠标移过去
pyautogui.click()
pointCenter = pyautogui.locateCenterOnScreen('2point.png')  #找到2点
pyautogui.moveTo(pointCenter)   #鼠标移过去


times = 0 #用于计算连续几次有点过赞的，达到一定次数就退出
# pyautogui.scroll(-250)

#点击2点后，判断是否需要点赞
def likeThePYQ():
    if (pyautogui.locateCenterOnScreen('unlike.png') != None):  # 对于已经点过赞的，直接下
        print("点赞失败，已点过赞")
        pyautogui.scroll(-250)  # 往下滚
        return 1
    else:  # 没点过赞的，点完往下滑
        likeCenter = pyautogui.locateCenterOnScreen('like.png')
        pyautogui.moveTo(likeCenter)  # 鼠标移过去
        pyautogui.click()  # 鼠标点赞
        print("点赞成功")
        pyautogui.scroll(-250)  # 往下滚
        return 0

while(True):
    pointCenter = pyautogui.locateCenterOnScreen('2point.png') #获取中心点
    if(pointCenter == None):    #有的朋友圈可能太长，所以找不到点赞按钮时就多下拉一点
        pyautogui.scroll(-500)
        print("满屏无2点！") #（debug）
        continue
    pyautogui.moveTo(pointCenter)   #鼠标移过去
    pyautogui.click()   #鼠标点击2点

    if likeThePYQ():    #点赞
        times += 1
    else:
        times = 0

    print(f"times= {times}")

    if(times >= 3): # 有的可能比较长，所以多滚一点
        pyautogui.scroll(-220)

    if(times == 100):    # 如果多个已点赞，说明已经到上次运行开始的地方了，就停下来。设置为非常大表示无限赞下去
        break


