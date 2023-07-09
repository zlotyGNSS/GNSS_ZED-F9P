import serial

class GNSSLibrary:
    def __init__(self, port='/dev/ttyUSB0', baudrate=115200):
        self.serial = serial.Serial(port, baudrate, timeout=1)
        
    
    def read_gnss_data(self):
        # Wysyłanie zapytania do odbiornika GNSS
        self.serial.write(b'PUBX,00*33\r\n')
        
        # Odczytywanie odpowiedzi z odbiornika GNSS
        response = self.serial.readline()
        
        # Przetwarzanie odczytanych danych GNSS
        # Tutaj możesz dodać kod do analizy i przetwarzania danych GNSS
        
        return response
    
    def close(self):
        self.serial.close()

if __name__ == '__main__':
                
      # Przykład użycia biblioteki
      gnss = GNSSLibrary()
      
      # Odczytywanie danych GNSS
      data = gnss.read_gnss_data()
      print(data)
      
      # Zamykanie połączenia
      gnss.close()

      