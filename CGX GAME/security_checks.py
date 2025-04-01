import os
import pickle

def check_save_file_integrity(filename):
    """
    Checks the integrity of a save file to detect tampering.
    (Basic example - more robust methods would be needed in a real-world scenario)
    """
    if not os.path.exists(filename):
        return False, "Save file does not exist."

    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            # Basic integrity check: Check if required keys are present
            if not all(key in data for key in ["cosmic_energy", "universe_state", "universes"]):
                return False, "Save file is corrupted or tampered with."
            return True, "Save file integrity check passed."
    except Exception as e:
        return False, f"Error during save file integrity check: {e}"

def check_for_malicious_commands(command):
    """
    Checks if a command contains potentially malicious content.
    (Basic example - more comprehensive checks would be needed)
    """
    blacklist = ["rm -rf", "shutdown", "format", "delete"]  # Example blacklist
    for item in blacklist:
        if item in command.lower():
            return False, f"Command contains potentially malicious content: '{item}'"
    return True, "Command is safe."

def check_for_excessive_resource_usage(ai_instance):
    """
    Checks if the game is using an excessive amount of resources.
    (Basic example - more advanced monitoring would be needed)
    """
    if ai_instance.cosmic_energy > 1000000:
        return False, "Excessive cosmic energy detected."
    return True, "Resource usage is within normal limits."

def check_for_invalid_data_types(data):
    """
    Checks if the data contains invalid data types.
    (Basic example - more advanced checks would be needed)
    """
    if not isinstance(data, dict):
        return False, "Data is not a dictionary."
    return True, "Data types are valid."
