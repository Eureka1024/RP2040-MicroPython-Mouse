from machine import Pin,Timer
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
# print(uos.uname())
spi_sck=machine.Pin(2)#SCK
spi_tx=machine.Pin(3) #TX
spi0=machine.SPI(0,baudrate=4000000, phase=1, polarity=1, sck=spi_sck, mosi=spi_tx)
# print(spi0)

# 屏幕显示
display = st7789.ST7789(spi0, disp_width, disp_width,
                          reset=machine.Pin(st7789_res, machine.Pin.OUT),
                          dc=machine.Pin(st7789_dc, machine.Pin.OUT),
                          xstart=0, ystart=0, rotation=0)
display.fill(st7789.WHITE)
display.text(font2, "Menu", 90, 10, color=st7789.BLACK, background=st7789.WHITE)
display.text(font2, "Connect PC", 10, 50, color=st7789.BLACK, background=st7789.WHITE)
display.text(font2, "Sensitivity", 10, 100, color=st7789.BLACK, background=st7789.WHITE)
display.text(font2, "Other", 10, 150, color=st7789.BLACK, background=st7789.WHITE)
currentX = 200
currentY = 200
f_image = open("/mouse_pic.bin", 'rb')
mouse_move(currentX, currentY)


# 按键扫描
# tim = Timer()
# def key_scan(timer):
# 
#     
#     
# tim.init(period=100, mode=Timer.PERIODIC, callback=key_scan)#100ms调用一次

status_mode = 0

while True:
    Xdeviation = XdeviationAD.read_u16()
    Ydeviation = YdeviationAD.read_u16()
    if (Xdeviation > 25000) and (Xdeviation < 35000):
        Xdeviation = 32500
    if (Ydeviation > 25000) and (Ydeviation < 35000):
        Ydeviation = 32500
    
    if (Xdeviation == 32500) and (Ydeviation == 32500):
        continue
    
    Xdeviation = Xdeviation - 32500
    Ydeviation = Ydeviation - 32500
    
    
#     print(Xdeviation)
#     print(Ydeviation)
#     if (Xdeviation != 0) or (Ydeviation != 0):
#         mouse.move(Xdeviation, Ydeviation)
#     
#     if buttonA.value() == 0:
#         mouse.click(mouse.BUTTON_RIGHT)
#     if buttonB.value() == 0:
#         mouse.click(mouse.BUTTON_LEFT)

#     f_image = open(image_file0, 'rb')
#     mouse_move(Xdeviation*10, Ydeviation*10)
#     time.sleep(0.1)
    
    if (status_mode == 0): #主菜单
        display.fill_rect(currentX, currentY, 15, 21, st7789.WHITE)
        display.text(font2, "Menu", 90, 10, color=st7789.BLACK, background=st7789.WHITE)
        display.text(font2, "Connect PC", 10, 50, color=st7789.BLACK, background=st7789.WHITE)
        display.text(font2, "Sensitivity", 10, 100, color=st7789.BLACK, background=st7789.WHITE)
        display.text(font2, "Other", 10, 150, color=st7789.BLACK, background=st7789.WHITE)

        currentX = currentX + int(Xdeviation/800)
        if (currentX < 0):
            currentX = 0
        if (currentX > 239):
            currentX = 239            
        currentY = currentY + int(Ydeviation/800)
        if (currentY < 0):
            currentY = 0
        if (currentY > 239):
            currentY = 239
            
        f_image = open("/mouse_pic.bin", 'rb')
        mouse_move(currentX, currentY)

        
        
        
    # display.text(font2, "www.eetree.cn", 30, 200)
#     elif (status_mode == 1)
#     
#     elif (status_mode == 2)
    
