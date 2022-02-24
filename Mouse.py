import machine
import time

deviationX = machine.ADC(3)
deviationY = machine.ADC(2)

while True:
    
    adc1 = deviationX.read_u16() - 32768
    print(adc1)
    adc2 = deviationY.read_u16() - 32768
    print(adc2)
    time.sleep(0.5)