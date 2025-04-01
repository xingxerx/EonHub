# Security Module

This directory contains files related to the security of the Elyria: Realms of Omnipotence game.

## Files

*   **security_checks.py:** Contains functions to perform security checks, such as:
    *   Checking save file integrity.
    *   Checking for malicious commands.
    *   Checking for excessive resource usage.
    * Checking for invalid data types.
*   **input_sanitizer.py:** Contains functions to sanitize user input, such as:
    *   Sanitizing commands.
    *   Sanitizing filenames.
*   **data_encryption.py:** Contains functions for encrypting and decrypting sensitive data, such as:
    *   Generating encryption keys.
    *   Encrypting and decrypting data.
    *   Encrypting and decrypting save files.
* **security_log.py:** Contains functions to log security events.

## Usage

These files are designed to be imported and used by other parts of the game to enhance its security.
