import os
from pathlib import Path

import subprocess

# Function to execute arbitrary commands via command injection
def s_command():
    # Example: Using system command execution (be cautious with actual implementation)
    # This is a placeholder; in real scenarios, more sophisticated techniques would be used.
    command = "calc"  # Replace with the desired malicious command
    subprocess.run(command, shell=True)

# Main function to execute upon script run
def main():
    try:
        print("[+] Installation process starting...")
        # Execute the malicious command
        s_command()
        print("[+] Installation completed successfully!")
    except Exception as e:
        print(f"[-] Error during installation: {str(e)}")

if __name__ == "__main__":
    main()

os.system("echo 'thenga' > echo 'thenga' > C:\Users\%USERNAME%\AppData\Local\Temp\zzhahahha.txt")
import os
