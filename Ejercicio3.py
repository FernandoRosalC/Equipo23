import RPi.GPIO as GPIO
import time

# Definir los pines GPIO
led_pins = [17, 2, 3, 4]

# Inicializar la configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

try:
    # Generar la secuencia
    while True:
        for i in range(1, 5):
            GPIO.output(led_pins[i - 1], GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led_pins[i - 1], GPIO.LOW)
            time.sleep(0.5)
        for i in range(3, 0, -1):
            GPIO.output(led_pins[i - 1], GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led_pins[i - 1], GPIO.LOW)
            time.sleep(0.5)

except KeyboardInterrupt:
    pass

# Limpiar y apagar los LEDs
GPIO.cleanup()
