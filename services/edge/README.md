# Edge server - docs

Polish version below!

## English

### Config

Contains a config option for central server address.

### Logger

Utilities for logging.
The module tries attempts to create `logs/` directory(if not present) when imported.
If it succeeds, the logs will be saved in `<current date in YYYY-mm-dd format>.txt` file. If not - they will only be shown in the console.

#### `log()`

Parameters:

- `message` - a `string` that contains the message to be logged.

Main utility function for logging. Takes a message and adds current time to it, then sends it to the console output and log file if available.

#### `logCentralServerHit()`

The utility for logging a request to central server. It also counts the total amount of central server requests sent. 

#### `logCacheHit()`

The utility for logging a cache hit. It automatically counts how many times the server's cache have been accessed.

### Central_server_connection

This module checks if the central server is available and defines a utility for fetching files from it.

#### `fetchFromCentralServer()`

Parameters:

- `attachment_name` - name(with an extension) of the file to be fetched.


A utility for fetching files from central server. It can return:

- Content from the request sent to the edge server,
- `FileNotFoundError` if the server returned code 404.

### Cache

A module that defines the edge server's cache and utilites used to interact with it.

#### `cacheAttachemnt()`

Parameters:

- `attachment` - contents of the file to be cached,
- `attachment_name` - a `string` that contains the attachment name and extension.
- (Optional) `cache_filesystem` - a cache to save the file in. The default is the cache created by the module.

A functon to save the file to cache.

#### `isInCache()`

Parameters:

- `attachment_name` - a `string` that contains the attachment name and extension.
- (Optional) `cache_filesystem` - a cache to look through. The default is the cache created by the module.

A function that checks if the file is in the specified cache.

#### `getFromCache()`

Parameters:

- `attachment_name` - a name(with extension) of the file to fetch,
- `cache_filesystem` - a cache to fetch the file from. The default is the cache created by the module.

A function for retrieving a resource from cache.

### Main

A main module that defines all API endpoints.

#### `/ping`

A GET endpoint useful to check if the server is up.

#### `/attachment/<attachment name>`

A GET endpoint used for fetching the attachment. It first attempts to find it in the cache and if it's not present, it tries to fetch it from the server. It can return:

- A response with code 200 OK and the file contents,
- A response with code 404 Not Found.


## Polish

### Config

Contains a config option for central server address.

Moduł, w którym można skonfigurować adres do serwera centralnego.

### Logger

Narzędzia do rejestrowania logów.
Moduł próbuje stworzyć ścieżkę `logs/` jeśli nie istnieje. Jeśli operacja się powiedzie, logi będą wpisywane do pliku o nazwie `<aktualna data w formacie YYYY-mm-dd>.txt` w tym folderze.
Jeśli folderu nie da się utworzyć - logi będą jedynie wyświetlane w konsoli.

#### `log()`

Parametry:

- `message` - łańcuch znaków zawierający wiadomość logu.

Główna funkcja do rejestrowania logów. Opatruje wiadomość aktualną godziną, po czym wysyła ją do konsoli, i - jeśli to możliwe - do pliku logów.

#### `logCentralServerHit()`

Funkcja służąca do rejestrowania w logach zapytań do serwera głównego. Automatycznie zlicza ilość takich zapytań.

#### `logCacheHit()`

Funkcja służąca do rejestrowania w logach odczytów z pamięci podręcznej. Automatycznie zlicza ilość takich odczytów.

### Central_server_connection

Ten moduł sprawdza łączność z serwerem centralnym i definiuje funkcję służącą do łączenia się z nim.

#### `fetchFromCentralServer()`

Parametry:

- `attachment_name` - nazwa(z rozszerzeniem) pliku do pobrania.

Funkcja służąca do pobierania plików z serwera centralnego. Może zwrócić:

- Zawartość odpowiedzi serwera głównego,
- `FileNotFoundError`, jeśli serwer zwrócił kod 404.

### Cache

Moduł definiujący pamięć podręczną i funkcje pozwalające na interakcję z nią.

#### `cacheAttachemnt()`

Parametry:

- `attachment` - zawartość pliku do przechowania,
- `attachment_name` - nazwa(z rozszerzeniem), pod jaką ma być przechowany plik,
- (opcjonalne) `cache_filesystem` - pamięć, w której plik ma być przechowany. Domyślnie jest to pamięć utworzona przez moduł.

Funkcja, którą można zapisać plik do pamięci podręcznej.

#### `isInCache()`

Parametry:

- `attachment_name` - nazwa(z rozszerzeniem) pliku do wyszukania.
- (opcjonalne) `cache_filesystem` - pamięć do przeszukania. Domyślnie jest to pamięć utworzona przez moduł.

Funkcja do sprawdzania, czy dany plik znajduje się w pamięci podręcznej.

#### `getFromCache()`

Parametry:

- `attachment_name` - nazwa(z rozszerzeniem) pliku do pobrania z pamięci,\
- (opcjonalne) `cache_filesystem` - pamięć, z której plik ma być pobrany. Domyślnie jest to pamięć utworzona przez moduł.

Funkcja do pobrania pliku z pamięci podręcznej.

### Main

Główny moduł definiujący wszystkie endpointy API.

#### `/ping`

Endpoint GET służący do sprawdzania łączności.

#### `/attachment/<nazwa załącznika>`

A GET endpoint used for fetching the attachment. It first attempts to find it in the cache and if it's not present, it tries to fetch it from the server. It can return:

- A response with code 200 OK and the file contents,
- A response with code 404 Not Found.

Endpoint GET służący do pobierania załącznika. Najpierw sprawdzana jest pamięć podręczna; jeśli załącznik się w niej znajduje, jest on z niej pobierany i odsyłany; w przeciwnym wypadku odpytywany jest serwer główny. Możliwe odpowiedzi:

- Z kodem 200 OK i zawartością pliku,
- Z kodem 404 Not Found.