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