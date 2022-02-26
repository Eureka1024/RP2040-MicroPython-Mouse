from machine import Pin
import time
import hid
import st7789 as st7789
from fonts import vga2_8x8 as font1
from fonts import vga1_16x32 as font2
import framebuf
import uos

def mouse_move(x, y):
    for column in range(y+0,y+21):
        buf = f_image.read(30)
        display.blit_buffer(buf, x, column, 15, 1)
        
# 摇杆的端口配置 -> AD采样端口
XdeviationAD = machine.ADC(3)
YdeviationAD = machine.ADC(2)

# A、B按键配置
buttonA = Pin(6, Pin.IN, Pin.PULL_UP)
buttonB = Pin(5, Pin.IN, Pin.PULL_UP)

# usb_hid 配置
mouse = hid.Mouse()

image_file0 = "/mouse2.bin" #图片文件地址                                                                                                                                                                                                         .bin" #图片文件地
st7789_res = 0 #复位引脚
st7789_dc  = 1 #D/C引脚
disp_width = 240 #屏幕宽度
disp_height = 240 #屏幕高度
CENTER_Y = int(disp_width/2) #Y轴中心点
CENTER_X = int(disp_height/2)#X轴中心点
print(uos.uname())
spi_sck=machine.Pin(2)#SCK
spi_tx=machine.Pin(3) #TX
spi0=machine.SPI(0,baudrate=4000000, phase=1, polarity=1, sck=spi_sck, mosi=spi_tx)
print(spi0)
display = st7789.ST7789(spi0, disp_width, disp_width,
                          reset=machine.Pin(st7789_res, machine.Pin.OUT),
                          dc=machine.Pin(st7789_dc, machine.Pin.OUT),
                          xstart=0, ystart=0, rotation=0)
display.fill(st7789.WHITE)
# display.text(font2, "Hello!", 10, 10)
# display.text(font2, "RPi Pico", 10, 40)
# display.text(font2, "MicroPython", 35, 100)
# display.text(font2, "EETREE", 35, 150)
# display.text(font2, "www.eetree.cn", 30, 200)
f_image = open(image_file0, 'rb')
# mouse_move(CENTER_X, CENTER_Y)

while True:
    
    Xdeviation = XdeviationAD.read_u16()
    Ydeviation = YdeviationAD.read_u16()
       
#     Xdeviation = int((XdeviationAD.read_u16() - 32768) / 3500)
#     Ydeviation = int((YdeviationAD.read_u16() - 32768) / 3500)
#     print(Xdeviation)
#     if (Xdeviation != 0) or (Ydeviation != 0):
#         mouse.move(Xdeviation, Ydeviation)
#     
#     if buttonA.value() == 0:
#         mouse.click(mouse.BUTTON_RIGHT)
#     if buttonB.value() == 0:
#         mouse.click(mouse.BUTTON_LEFT)

    f_image = open(image_file0, 'rb')
    mouse_move(Xdeviation*10, Ydeviation*10)
    time.sleep(0.1)
    
