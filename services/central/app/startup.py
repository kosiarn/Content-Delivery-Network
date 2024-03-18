import os
import config
from logger import log

attachmentDirExists = os.path.exists(config.attachment_directory)

if not attachmentDirExists:
    log(f"Directory {config.attachment_directory} not existing; creating directory...")
    try:
        os.makedirs(config.attachment_directory)
    except Exception as error:
        log(f"An error occured when attempting to create directory: {error}")
