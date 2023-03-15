## IP deste dispositivo é: 192.169.0.113
import network
import machine
import esp
esp.osdebug(None)    
machine.freq(240000000) # set the CPU frequency to 240 MHz
print('Frequencia da CPU: ', machine.freq())
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('conectando na rede local...')
    # Dados de conexão rede sem fio
    wlan.connect('Prosperidade_V', 'GD100451@2020!') # connect to an AP
    while not wlan.isconnected():
        pass
    print('Rede: ', wlan.ifconfig())

print('conectado na rede local.')
print('Rede: ', wlan.ifconfig())