# kod przydatny, by na szybko znaleźć, określic pod jakim portem COM jest podłaczony moduł GNSS

import serial.tools.list_ports

# Pobierz listę dostępnych portów
available_ports = serial.tools.list_ports.comports()

if len(available_ports) == 0:
    print("Nie znaleziono dostępnych portów szeregowych.")
else:
    # Wyświetl dostępne porty
    for port in available_ports:
        print(f"Znaleziono port: {port.device} - {port.description}")


'''
Ten kod korzysta z modułu serial.tools.list_ports, 
który dostarcza funkcję comports() do uzyskania listy dostępnych portów szeregowych.
 Jeśli nie zostaną znalezione żadne porty, zostanie wyświetlony odpowiedni komunikat.
   W przeciwnym razie, dla każdego znalezionego portu, 
   zostanie wyświetlona jego nazwa (port.device) oraz opis (port.description).

Po uruchomieniu tego kodu, zobaczysz listę dostępnych portów szeregowych w konsoli. 
Pamiętaj, że przed uruchomieniem tego kodu musisz mieć podłączone urządzenie, 
które jest rozpoznawane jako port szeregowy przez Twój system.
'''

print(serial.VERSION)