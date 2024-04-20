# Central server - docs

Polish version below!

## English

### Config

Contains a config option for attachment directory path.

### Logger

Utilities for logging.
The module tries attempts to create `logs/` directory(if not present) when imported.
If it succeeds, the logs will be saved in `<current date in YYYY-mm-dd format>.txt` file. If not - they will only be shown in the console.

#### `log()`

Parameters:

- `message` - a `string` that contains the message to be logged.

Main utility function for logging. Takes a message and adds current time to it, then sends it to the console output and log file if available.

#### `logMemoryHit()`

The utility for logging a memory hit. It automatically counts how many times the server's resources have been accessed.

### Startup

This module takes care of making sure that the attachment directory exists or make a log if it cannot create it.

### Main

The main file of the server. It defines the API endpoints and their logic.

#### `/ping`

A GET endpoint for testing connection. The edge server uses it to check if the central server is available.

#### `/attachment/<attachment name>`

A GET endpoint for retrieving a static file from the server. It can return:
- A response with code 200 OK and the requested file if present on the server,
- A response with code 404 Not Found if the file wasn't found on the server.

## Polish

### Config

W tym pliku można skonfigurować nazwę folderu z przechowywanymi plikami.

### Logger

Narzędzia do rejestrowania logów.
Moduł próbuje stworzyć ścieżkę `logs/` jeśli nie istnieje. Jeśli operacja się powiedzie, logi będą wpisywane do pliku o nazwie `<aktualna data w formacie YYYY-mm-dd>.txt` w tym folderze.
Jeśli folderu nie da się utworzyć - logi będą jedynie wyświetlane w konsoli.

#### `log()`

Parametry:

- `message` - łańcuch znaków zawierający wiadomość logu.

Główna funkcja do rejestrowania logów. Opatruje wiadomość aktualną godziną, po czym wysyła ją do konsoli, i - jeśli to możliwe - do pliku logów.

#### `logMemoryHit()`

Funkcja do logowania użycia zasobów serwera. Automatycznie zlicza ilość zapytań wysłanych do serwera.

### Startup

Ten moduł upewnia się, że folder z załącznkami istnieje oraz że ewentualny brak możliwości utworzenia go jest zapisany w logach.

### Main

Główny kod serwera. Definiuje endpointy API i ich działanie.

#### `/ping`

Endpoint GET służący do testowania połączenia przez serwer brzegowy.

#### `/attachment/<nazwa załącznika>`

Endpoint GET służący do pobierania plików z serwera. Może zwrócić:

- Odpowiedź z kodem 200 OK i zawartością pliku,
- Odpowiedź z kodem 404 Not Found jeśli plik nie został znaleziony na serwerze.