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