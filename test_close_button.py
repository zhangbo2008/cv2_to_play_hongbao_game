#===============close button周围有一堆的图片,如何识别???????????
#测试一下




import os
#========================上来获取图片
os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
# 把模拟器里面的文件或文件夹传到电脑上
os.system('adb pull /sdcard/screencap.png screencap.png')#这时手机的屏幕就保存到了项目的根目录下.

import utils
aaa=utils.pipei('screencap.png','close_button2.png',0.8)
if aaa:
    point=(aaa[0]+aaa[2])/2,(aaa[1]+aaa[3])/2
print(f"点击坐标{point}")