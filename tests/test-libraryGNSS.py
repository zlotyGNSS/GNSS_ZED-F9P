from GNSSLibrary import GNSSLibrary

#gnss = GNSSLibrary('/dev/ttyUSB0', 115200)  # Dostosuj port i prędkość transmisji do swojego modułu
gnss = GNSSLibrary('COM3', 115200)

try:
    while True:
        data = gnss.read_gnss_data()
        print(data)
        
except KeyboardInterrupt:
    pass

gnss.close()
