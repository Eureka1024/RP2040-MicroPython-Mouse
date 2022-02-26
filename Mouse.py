from machine import Pin
import time
import hid


# 摇杆的端口配置 -> AD采样端口
deviationX = machine.ADC(3)
deviationY = machine.ADC(2)

# A、B按键配置
buttonA = Pin(6, Pin.IN, Pin.PULL_UP)
buttonB = Pin(5, Pin.IN, Pin.PULL_UP)

# usb_hid 配置
mouse = hid.Mouse()

while True:
    
#     adc1 = deviationX.read_u16() - 32768
#     print(adc1)
#     adc2 = deviationY.read_u16() - 32768
#     print(adc2)
#     aValue = buttonA.value()
#     print(aValue)
#     bValue = buttonB.value()
#     print(bValue)
    mouse.move(50, 0)
    time.sleep(1)
