# Content-Delivery-Network


## Język polski

### Wstęp

Zasoby statyczne to treści, które mogą zostać dostarczone użytkownikowi bez żadnej modyfikacji lub generowania ich.
Są to na przykład:

- obrazki,
- pliki tekstowe,
- pliki dźwiękowe.

Treści te mogą być dostarczane za pomocą serwera statycznego. Pomimo braku konieczności dynamicznego generowania zawartości, w przypadku dużych zbiorów statycznych zasobów znalezienie i wysłanie tego, którego żąda użytkownik może być czasochłonne.

### Caching

Jednym ze sposobów optymalizacji długich operacji jest zapisywanie ich wyników w pamięci podręcznej. Jeśli operacja ma charakter deterministyczny(tj. takie same dane wejściowe zawsze zostają zamienione na te same dane wyjściowe), to jej wynik można zapisać i kiedy pojawi się potrzeba przeprowadzenia jej jeszcze raz z takimi samymi parametrami - zwrócić gotowy rezultat. Wydajność takiego rozwiązania jest zależna od wielu czynników, takich jak ilość pamięci podręcznej, czas odczytu z tej pamięci oraz czas wykonania operacji, ale jest stosunkowo prosty w implementacji oraz powszechnie używany.

### CDN(Content Delivery Network)

Implementacją metody cachingu w obszarze dostarczania statycznej zawartości jest sieć dostarczania treści(ang. **Content Delivery Network**). Zawiera ona serwery brzegowe będące pamięcią podręczną dla serwera źródłowego. Kiedy użytkownik wysyła zapytanie, serwer brzegowy szuka zasobu w swojej pamięci; możliwe są dwa scenariusze:

- Serwer brzegowy zawiera żądany zasób - wysyła go w odpowiedzi do użytkownika.
- Serwer brzegowy nie zawiera żądanego zasobu - wysyła zapytanie do serwera źródłowego, otrzymuje od niego żądane treści, które:
    1. Zapisuje w swojej pamięci,
    2. Odsyła użytkownikowi.

Serwery brzegowe przechowują znacznie mniejsze ilości plików od serwerów źródłowych, więc ich operacja przeszukiwania jest o wiele szybsza. Usprawnia to dostarczanie statycznej zawartości oraz zmniejsza obciążenie serwera źródłowego.

### Korzystanie z repozytorium

Najszybszym sposobem jest użycie oprogramowania Docker i uruchomienie serwerów brzegowego i źródłowego przez dodatek `docker-compose`.

- Upewnij się, że na Twoim komputerze jest zainstalowany oraz uruchomiony Docker daemon. Otwórz terminal i uruchom poniższe polecenie w terminalu:

```cmd
docker list
```

Jeśli wynikiem polecenia jest lista(może być ona pusta), to znaczy że Docker działa prawidłowo.

- Sklonuj repozytorium, a następnie w terminalu przejdź do jego folderu.

```cmd
cd sciezka/do/folderu/z/repozytorium/Content-Delivery-Network
```

- Po przejściu do folderu repozytorium w terminalu, wykonaj poniższe polecenie:

```cmd
docker-compose up
```

- Zaczekaj na zbudowanie i uruchomienie kontenerów. Jeśli wszystko odbędzie się prawidłowo, informacja o uruchomieniu obydwu serwerów powinna pojawić się w terminalu.

#### Testy wydajności

W folderze `perf_tests/` znajduje się skrypt `performance_test.py`, który pokazuje proste porównanie wydajności przed i po zastosowaniu serwera brzegowego. Plik `requirements.txt` zawiera zależność potrzebną do prawidłowego działania skryptu. Po zainstalowaniu potrzebnego modułu, wystarczy uruchomić skrypt za pomocą Pythona. W razie potrzeby można zmienić konfigurację testu za pomocą pliku `test_config.py`.

#### Uwagi

- Domyślnie porty, na których są uruchomione API serwerów są połączone z portami `8001` i `8002` hosta. Przed uruchomieniem projektu upewnij się, że żaden inny proces nie nasłuchuje na tych portach.

- Ze względu na mały zbiór załączników dostępnych na serwerze źródłowym, serwer centralny symuluje długie wyszukiwanie poprzez odczekiwanie dwóch sekund przed wysłaniem odpowiedzi.