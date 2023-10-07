import RPi.GPIO as GPIO

# Definir los pines GPIO
led_rojo_pin = 17
led_amarillo_pin = 3
led_verde_pin = 4

# Inicializar la configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_rojo_pin, GPIO.OUT)
GPIO.setup(led_amarillo_pin, GPIO.OUT)
GPIO.setup(led_verde_pin, GPIO.OUT)

def encender_leds(rojo, amarillo, verde):
    GPIO.output(led_rojo_pin, rojo)
    GPIO.output(led_amarillo_pin, amarillo)
    GPIO.output(led_verde_pin, verde)

try:
    while True:
        comando = input("Escribe 'alto', 'siga' o 'precaucion': ").lower()

        if comando == "alto":
            encender_leds(True, False, False)
        elif comando == "siga":
            encender_leds(False, False, True)
        elif comando == "precaucion":
            encender_leds(False, True, False)
        else:
            print("Comando no válido. Usar 'alto', 'siga' o 'precaucion'.")

except KeyboardInterrupt:
    pass

# Apagar los LEDs y limpiar
encender_leds(False, False, False)
GPIO.cleanup()