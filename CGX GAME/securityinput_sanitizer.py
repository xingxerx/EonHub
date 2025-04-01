import re

def sanitize_command(command):
    """
    Sanitizes a command to remove potentially harmful characters.
    (Basic example - more robust sanitization would be needed)
    """
    # Remove characters that are not alphanumeric, spaces, or certain symbols
    sanitized_command = re.sub(r"[^a-zA-Z0-9\s\"-]", "", command)
    return sanitized_command

def sanitize_filename(filename):
    """
    Sanitizes a filename to prevent path traversal attacks.
    (Basic example - more robust sanitization would be needed)
    """
    # Remove characters that are not alphanumeric, underscores, or periods
    sanitized_filename = re.sub(r"[^a-zA-Z0-9_\.]", "", filename)
    return sanitized_filename
