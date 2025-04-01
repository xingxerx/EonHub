import random
import pickle
import os

class EoniaAI:
    def __init__(self):
        self.cosmic_energy = 0
        self.universe_state = "idle"
        self.universes = {}
        self.multiverse = {}
        self.omnipotence_points = 0
        self.realms = {}
        self.love_essence = 0
        self.universe_counter = 0

    def processInput(self, input_string):
        input_string = input_string.strip()
        parts = input_string.split()
        if not parts:
            return "Unknown command"
        command = parts[0].upper()
        
        # Using a dictionary for command dispatch
        command_map = {
            "CREATE": self.handle_create,
            "CHANNEL": self.handle_channel,
            "CHECK": self.handle_check,
            "LIST": self.handle_list,
            "GET": self.handle_get,
            "ENTER": self.handle_enter,
            "GAIN": self.handle_gain,
            "HELP": self.help,
            "EXIT": lambda: "exit",
            "RESET": self.reset,
            "BUILD": self.handle_build,
            "DESTROY": self.handle_destroy,
            "EXPLORE": self.handle_explore,
            "CONQUER": self.handle_conquer,
            "SCAN": self.scan_multiverse,
            "SAVE": self.handle_save,
            "LOAD": self.handle_load,
        }

        handler = command_map.get(command)
        if handler:
            return handler(parts) if command not in ["HELP", "EXIT", "RESET", "SCAN"] else handler()
        else:
            return "Unknown command"

    def handle_create(self, parts):
        if len(parts) >= 4 and parts[1].upper() == "UNIVERSE":
            return self.create_universe(parts[2], parts[3])
        elif len(parts) >= 4 and parts[1].upper() == "REALM":
            return self.create_realm(parts[2], parts[3])
        else:
            return "Error: Invalid 'create' command."

    def handle_channel(self, parts):
        if len(parts) >= 2 and parts[1].upper() == "ENERGY":
            return self.channel_energy()
        elif len(parts) >= 2 and parts[1].upper() == "LOVE":
            return self.channel_love()
        else:
            return "Error: Invalid 'channel' command."

    def handle_check(self, parts):
        if len(parts) >= 2 and parts[1].upper() == "ENERGY":
            return self.check_energy()
        elif len(parts) >= 2 and parts[1].upper() == "OMNIPOTENCE":
            return self.check_omnipotence()
        elif len(parts) >= 2 and parts[1].upper() == "LOVE":
            return self.check_love()
        else:
            return "Error: Invalid 'check' command."

    def handle_list(self, parts):
        if len(parts) >= 2 and parts[1].upper() == "UNIVERSES":
            return self.list_universes()
        elif len(parts) >= 2 and parts[1].upper() == "REALM":
            return self.list_realms()
        else:
            return "Error: Invalid 'list' command."

    def handle_get(self, parts):
        if len(parts) >= 3 and parts[1].upper() == "UNIVERSE" and parts[2].upper() == "INFO":
            return self.get_universe_info()
        else:
            return "Error: Invalid 'get' command."

    def handle_enter(self, parts):
        if len(parts) >= 3 and parts[1].upper() == "MULTIVERSE" and parts[2].upper() == "UNIVERSE":
            return self.enter_multiverse_universe(parts[3])
        else:
            return "Error: Invalid 'enter' command."

    def handle_gain(self, parts):
        if len(parts) >= 3 and parts[1].upper() == "OMNIPOTENCE" and parts[2].upper() == "POINTS":
            return self.gain_omnipotence_points(int(parts[3]))
        else:
            return "Error: Invalid 'gain' command."

    def handle_build(self, parts):
        if len(parts) >= 3 and parts[1].upper() == "REALM":
            realm_name = self.extract_realm_name(parts)
            if not realm_name:
                return "Error: Invalid 'build' command."
            return self.create_realm(realm_name, "custom")
        else:
            return "Error: Invalid 'build' command."

    def handle_destroy(self, parts):
        if len(parts) >= 3 and parts[1].upper() == "REALM":
            return self.destroy_realm(parts[2])
        else:
            return "Error: Invalid 'destroy' command."

    def handle_explore(self, parts):
        if len(parts) >= 3 and parts[1].upper() == "UNIVERSE":
            return self.explore_universe(parts[2])
        else:
            return "Error: Invalid 'explore' command."

    def handle_conquer(self, parts):
        if len(parts) >= 3 and parts[1].upper() == "UNIVERSE":
            return self.conquer_universe(parts[2])
        else:
            return "Error: Invalid 'conquer' command."
    
    def handle_save(self, parts):
        if len(parts) >= 2:
            return self.save_game(parts[1])
        else:
            return "Error: Invalid 'save' command. Usage: SAVE <filename>"

    def handle_load(self, parts):
        if len(parts) >= 2:
            return self.load_game(parts[1])
        else:
            return "Error: Invalid 'load' command. Usage: LOAD <filename>"

    def extract_realm_name(self, parts):
        if parts[2].startswith('"'):
            realm_name_parts = []
            for i in range(2, len(parts)):
                realm_name_parts.append(parts[i])
                if parts[i].endswith('"'):
                    return " ".join(realm_name_parts).replace('"', '')
        else:
            return parts[2]
        return ""

    def create_universe(self, universe_name, universe_size):
        if universe_name in self.universes:
            return f"Error: Universe '{universe_name}' already exists."
        self.universe_counter += 1
        self.universes[universe_name] = {"size": universe_size, "state": "created", "number": self.universe_counter}
        self.universe_state = "creating"
        return f"Universe '{universe_name}' of size '{universe_size}' creation initiated."

    def create_realm(self, realm_name, realm_size):
        if realm_name in self.realms:
            return f"Error: Realm '{realm_name}' already exists."
        self.realms[realm_name] = {"size": realm_size, "state": "created"}
        return f"Realm '{realm_name}' of size '{realm_size}' creation initiated."

    def destroy_realm(self, realm_name):
        if realm_name in self.realms:
            del self.realms[realm_name]
            return f"Realm '{realm_name}' destroyed."
        else:
            return f"Error: Realm '{realm_name}' not found."

    def channel_energy(self):
        self.cosmic_energy += 1000
        return "Cosmic energy channeled"

    def channel_love(self):
        self.love_essence += 500
        return "Love essence channeled"

    def check_energy(self):
        return f"Current cosmic energy: {self.cosmic_energy}"

    def check_omnipotence(self):
        return f"Current omnipotence points: {self.omnipotence_points}"

    def check_love(self):
        return f"Current love essence: {self.love_essence}"

    def list_universes(self):
        if not self.universes:
            return "No universes created yet."
        universe_list = "\n".join([f"- {name} (size: {details['size']}, state: {details['state']}, number: {details['number']})" for name, details in self.universes.items()])
        return f"Created universes:\n{universe_list}"

    def list_realms(self):
        if not self.realms:
            return "No realms created yet."
        realm_list = "\n".join([f"- {name} (size: {details['size']}, state: {details['state']})" for name, details in self.realms.items()])
        return f"Created realms:\n{realm_list}"

    def get_universe_info(self):
        if self.universe_state == "idle":
            return "No universe selected."
        else:
            return f"Current universe: {self.universe_state}"

    def enter_multiverse_universe(self, universe_name):
        if universe_name in self.universes:
            self.multiverse[universe_name] = self.universes[universe_name]
            return f"Entered multiverse universe: {universe_name}"
        else:
            return f"Error: Universe '{universe_name}' not found."

    def gain_omnipotence_points(self, points):
        self.omnipotence_points += points
        return f"Gained {points} omnipotence points. Total: {self.omnipotence_points}"

    def help(self):
        help_text = """
*GENERAL COMMANDS*
- HELP (you should have tried this first ;) )
- EXIT - quit Elyria: Realms of Omnipotence
- RESET - restart game with fresh multiverse
- SAVE <filename> - save the current game state
- LOAD <filename> - load a saved game state
*REALM COMMANDS*
- BUILD REALM "NAME" - create custom realm
- DESTROY REALM "NAME" - delete existing realm
- LIST REALM - show all created realms
*MULTIVERSE COMMANDS*
- EXPLORE UNIVERSE "NUMBER" - visit parallel universe
- CONQUER UNIVERSE "NUMBER" - claim universe as ours
- SCAN MULTIVERSE - reveal hidden universe properties
        """
        return help_text

    def reset(self):
        self.cosmic_energy = 0
        self.universe_state = "idle"
        self.universes = {}
        self.multiverse = {}
        self.omnipotence_points = 0
        self.realms = {}
        self.love_essence = 0
        self.universe_counter = 0
        return "Game reset to a fresh multiverse."

    def explore_universe(self, universe_number):
        try:
            universe_number = int(universe_number)
        except ValueError:
            return "Error: Universe number must be an integer."

        found_universe = next((name for name, details in self.universes.items() if details["number"] == universe_number), None)

        if found_universe:
            return f"Exploring universe: {found_universe} (number: {universe_number})"
        else:
            return f"Error: Universe with number '{universe_number}' not found."

    def conquer_universe(self, universe_number):
        try:
            universe_number = int(universe_number)
        except ValueError:
            return "Error: Universe number must be an integer."

        found_universe = next((name for name, details in self.universes.items() if details["number"] == universe_number), None)

        if found_universe:
            self.universes[found_universe]["state"] = "conquered"
            return f"Universe '{found_universe}' (number: {universe_number}) conquered!"
        else:
            return f"Error: Universe with number '{universe_number}' not found."

    def scan_multiverse(self):
        if not self.universes:
            return "No universes to scan."

        scan_results = ""
        for universe_name, details in self.universes.items():
            scan_results += f"- Universe: {universe_name} (number: {details['number']})\n"
            scan_results += f"  - Size: {details['size']}\n"
            scan_results += f"  - State: {details['state']}\n"
            scan_results += f"  - Hidden Property: {random.choice(['Abundant Resources', 'Mystical Energies', 'Ancient Artifacts', 'Cosmic Anomalies'])} \n"
        return scan_results
    
    def save_game(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.__dict__, file)
            return f"Game saved to '{filename}'."
        except Exception as e:
            return f"Error saving game: {e}"

    def load_game(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.__dict__.update(pickle.load(file))
            return f"Game loaded from '{filename}'."
        except FileNotFoundError:
            return f"Error: Save file '{filename}' not found."
        except Exception as e:
            return f"Error loading game: {e}"
