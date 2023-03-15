from machine import Pin
import sys
p0 = Pin(4, Pin.IN, Pin.PULL_DOWN) # Habilita porta GPIO4, porta de entrada e ativa o resistor
def main():
    if p0.value():
        print("Enviar sinal de alerta!")
while True:
    try:
        main()
    except KeyboardInterrupt:
        print("Exit")
        sys.exit(0)