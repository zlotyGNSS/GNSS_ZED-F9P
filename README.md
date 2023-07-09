# Projekt GNSS

Projekt GNSS to program do obsługi systemu nawigacji satelitarnej GNSS (Global Navigation Satellite System). Projekt umożliwia łączenie się z odbiornikiem GNSS, odczyt danych satelitarnych, przetwarzanie sygnałów GNSS oraz prezentację wyników na interfejsie użytkownika.

## Funkcje

- Łączenie się z odbiornikiem GNSS i odczyt danych satelitarnych.
- Przetwarzanie sygnałów GNSS w celu obliczania pozycji, prędkości, czasu i innych parametrów.
- Wyświetlanie odczytanych danych na interfejsie użytkownika w czytelnej formie.
- Integracja z mapami, umożliwiająca wizualizację lokalizacji na mapie.
- Eksport danych do plików w różnych formatach (np. CSV, KML) dla dalszej analizy.
- Możliwość dostosowania ustawień i konfiguracji odbiornika GNSS.

## Wymagania

- Python 3.7 lub nowszy
- Moduł serial (można zainstalować za pomocą `pip install pyserial`)

## Instalacja

1. Sklonuj repozytorium projektu GNSS.
2. Zainstaluj wymagane zależności, wykonując `pip install -r requirements.txt`.
3. Uruchom projekt, wykonując `python main.py`.

## Instrukcje użycia

1. Uruchom plik `main.py` w swoim środowisku Python.
2. Wpisz port szeregowy, do którego jest podłączony odbiornik GNSS.
3. Wybierz żądane opcje, takie jak odczyt danych satelitarnych, przetwarzanie sygnałów itp.
4. Otrzymane dane będą wyświetlane na interfejsie użytkownika lub można je eksportować do pliku.
5. Aby zakończyć działanie programu, naciśnij kombinację klawiszy Ctrl+C.

## Status projektu

Aktualnie projekt GNSS jest w fazie wczesnego rozwoju. Planowane funkcje i udoskonalenia obejmują:

- Dodanie obsługi innych systemów nawigacji satelitarnej, takich jak GPS, GLONASS, Galileo itp.
- Udoskonalenie interfejsu użytkownika i funkcjonalności wizualizacji.
- Implementacja dodatkowych algorytmów przetwarzania sygnałów GNSS.
- Rozbudowa dokumentacji i testów jednostkowych.

Więcej informacji można znaleźć w [repozytorium projektu GNSS](https://github.com/twoj-projekt-gnss).

