from machine import Pin
import time
import hid


# 摇杆的端口配置 -> AD采样端口
XdeviationAD = machine.ADC(3)
YdeviationAD = machine.ADC(2)

# A、B按键配置
buttonA = Pin(6, Pin.IN, Pin.PULL_UP)
buttonB = Pin(5, Pin.IN, Pin.PULL_UP)

# usb_hid 配置
mouse = hid.Mouse()

while True:
    
    Xdeviation = int((XdeviationAD.read_u16() - 32768) / 3500)
#     print(Xdeviation)
    Ydeviation = int((YdeviationAD.read_u16() - 32768) / 3500)
#     print(Ydeviation)
#     aValue = buttonA.value()
#     print(aValue)
#     bValue = buttonB.value()
#     print(bValue)
    mouse.move(Xdeviation, Ydeviation)
    time.sleep(0.1)
