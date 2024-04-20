# Content-Delivery-Network

Polska wersja poniżej!

## English 

### Introduction

Static resources - content that can be delivered without being modificated or generated, such as:

- images,
- text files,
- sound files.

This content can be available through a static server; despite that looking up requested resource can be lenghty in a case of a large database.

### Caching

Long operations can be optimized by temporarily storing their results. If the same action is requested, the result is simply loaded from cache; if cache read/write operations are fast, the whole system can get a significant performance boost. **Important note**: In order for cache to be useful, the operation *has* to be deterministic(the same inputs = the same outputs every time).

### CDN(Content Delivery Network)

Content Delivery Network is an implementation of a cache in static content delivery. 
It consists of a series of edge servers that act as a cache memory for the central server.
Every user request goes through an edge server; if it has the requested resource, then it sends it back. If the resource isn't present in the edge server's memory, it tries to get it from the origin server. After receiving the file, the edge server:
- sends it to the user,
- saves it in the edge server's memory.

Edge servers store less files than origin servers; that makes their lookups faster, speeding up resolving requests regarding often needed files.

### Using this repository

The fastest way is using Docker and `docker-compose` to run the whole infrastructure.

- Make sure that you have Docker installed and running. Open up the terminal and run:

```cmd
docker list
```
If the result is a list(can be empty), then you're set.

- Clone the repo, then move to its directory in the terminal.

```cmd
cd path/to/repo/Content-Delivery-Network
```

- Run the command:

```cmd
docker-compose up
```

- Wait for the containers to build and run. If everything goes well, logs from both services will fill the terminal.

#### Performance tests

The `perf_tests/` directory contains `performance_test.py` script. It compares connections with and without edge server by response times. `requirements.txt` file contains the name and version of a dependency needed by the script. After installing it, run the servers and then the script. `test_config.py` contains configuration for the tests. If you make changes to the docker compose file or servers' code, make sure to reflect them in test script config.

#### Notes

- The project uses ports `8001` and `8002` by default; make sure that they're free or change them in `compose.yaml` and test config.

- The project has only few attachments available on the central server. To better simulate expensive lookup, it does `time.sleep(2)` on every response.

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

W folderze `perf_tests/` znajduje się skrypt `performance_test.py`, który pokazuje proste porównanie wydajności przed i po zastosowaniu serwera brzegowego. Plik `requirements.txt` zawiera zależność potrzebną do prawidłowego działania skryptu. Po zainstalowaniu potrzebnego modułu, wystarczy uruchomić skrypt za pomocą Pythona. W razie potrzeby można zmienić konfigurację testu za pomocą pliku `test_config.py`. Skrypt testuje infrastrukturę uruchomioną lokalnie - wykonaj instrukcje z całego kroku *Korzystanie z repozytorium* przed uruchomieniem testów.

#### Uwagi

- Domyślnie porty, na których są uruchomione API serwerów są połączone z portami `8001` i `8002` hosta. Przed uruchomieniem projektu upewnij się, że żaden inny proces nie nasłuchuje na tych portach.

- Ze względu na mały zbiór załączników dostępnych na serwerze źródłowym, serwer centralny symuluje długie wyszukiwanie poprzez odczekiwanie dwóch sekund przed wysłaniem odpowiedzi.

