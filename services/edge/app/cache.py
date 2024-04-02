from fs.memoryfs import MemoryFS
from .logger import logCacheHit


cache = MemoryFS()
cache.makedir("/attachments")

def cacheAttachemnt(attachment, attachment_name, cache_filesystem = cache) -> None:
    """
    Stores passed attachment in server's RAM.
    """
    with cache_filesystem.open(f"/attachments/{attachment_name}", "wb") as destination:
        destination.write(attachment)

def isInCache(attachment_name, cache_filesystem = cache) -> bool:
    """
    Determines if the attachment is already cached.
    """
    return cache_filesystem.exists(f"/attachments/{attachment_name}")

def getFromCache(attachment_name, cache_filesystem = cache) -> bytes:
    """
    Fetches attachment from cache.
    """
    with cache_filesystem.open(f"/attachments/{attachment_name}", "rb") as cached_attachment:
        attachment_contents = cached_attachment.read()
    logCacheHit()
    return attachment_contents