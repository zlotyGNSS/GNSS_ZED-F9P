import serial.tools.list_ports

# Pobierz listę otwartych portów szeregowych
open_ports = [port.device for port in serial.tools.list_ports.comports() if port.is_open]

# Zamknij wszystkie otwarte porty
for port in open_ports:
    try:
        ser = serial.Serial(port)
        ser.close()
        print(f"Zamknięto port: {port}")
    except Exception as e:
        print(f"Błąd podczas zamykania portu {port}: {str(e)}")

'''
Ten kod korzysta z modułu serial.tools.list_ports, 
aby uzyskać listę wszystkich otwartych portów szeregowych. 
Następnie przechodzi przez listę i próbuje zamknąć każdy port, 
używając obiektu Serial i metody close(). 
Jeśli zamknięcie portu powiedzie się, wyświetla informację o zamkniętym porcie. 
Jeśli wystąpi błąd podczas zamykania portu, 
wyświetla odpowiedni komunikat z informacją o błędzie.

Pamiętaj, że ten kod zamknie wszystkie otwarte porty szeregowe. 
Upewnij się, że nie zamkniesz niechcący innych istotnych połączeń szeregowych, 
które mogą być używane przez inne urządzenia lub programy na Twoim komputerze. 
Przed uruchomieniem tego kodu upewnij się, że wiesz, 
które porty chcesz zamknąć i czy są one faktycznie otwarte.
'''