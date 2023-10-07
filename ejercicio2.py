import RPi.GPIO as GPIO
import time

# Configura el modo de los pines GPIO
GPIO.setmode(GPIO.BCM)

# Define el número del pin GPIO al que está conectado el LED
led_pin = 17

# Configura el pin GPIO como salida
GPIO.setup(led_pin, GPIO.OUT)

try:
    # Solicita al usuario que ingrese el tiempo en segundos
    tiempo = int(input("Ingrese el tiempo en segundos: "))

    # Enciende el LED durante el tiempo especificado
    GPIO.output(led_pin, GPIO.HIGH)
    print(f"LED encendido durante {tiempo} segundos...")
    time.sleep(tiempo)
    
    # Apaga el LED
    GPIO.output(led_pin, GPIO.LOW)
    print("LED apagado.")
except KeyboardInterrupt:
    # Captura una interrupción de teclado (Ctrl+C) para detener el programa
    pass
finally:
    # Limpia los pines GPIO y apaga el LED antes de salir
    GPIO.cleanup()
