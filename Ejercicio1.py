import RPi.GPIO as GPIO
import time

# Definir los pines GPIO
led_pin = 17
button_pin = 2

# Inicializar la configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Leer el estado del botón
        button_state = GPIO.input(button_pin)

        # Encender o apagar el LED según el estado del botón
        if button_state == GPIO.LOW:
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)

except KeyboardInterrupt:
    pass

# Limpiar y apagar el LED
GPIO.cleanup()
