import serial
from modules.GNSSLibrary import GNSSLibrary 

# połaczenie z GNSS jako instancja klasy GNSSLibrary
gnss = GNSSLibrary('COM3', 115200)

# próba odebrania danych, dla testów
try:
    while True:
        data = gnss.read_gnss_data()
        print(data)
except KeyboardInterrupt:
    ...

#zamknięcie połaczenia z GNSS
gnss.close()

#!to na początek, program bedzie się rozwijał 