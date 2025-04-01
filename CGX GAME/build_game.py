import sys
import subprocess
import os

def build_game(output_name="eonnodgame"):
    """Packages the game using PyInstaller."""

    # Check if PyInstaller is installed
    try:
        import PyInstaller.__main__
    except ImportError:
        print("Error: PyInstaller is not installed. Please install it using 'pip install pyinstaller'")
        return

    # Build the command for PyInstaller
    command = [
        "pyinstaller",
        "--onefile",  # Create a single executable file
        "--name", output_name, # Name of the executable
        "GameInterface.py"  # Your main game script
    ]

    # Run PyInstaller
    try:
        subprocess.check_call(command)
        print(f"Game packaged successfully as '{output_name}' in the 'dist' folder.")
    except subprocess.CalledProcessError as e:
        print(f"Error packaging game: {e}")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-c":
        build_game()
    else:
        print("Usage: python build_game.py -c")
        print("This will package the game into an executable.")

if __name__ == "__main__":
    main()
