# Ransomware Simulation Project

This project simulates the behavior of ransomware to help you understand how ransomware attacks operate. The simulation demonstrates file encryption, creation of ransom notes, and command-and-control (C2) server communication. The goal is to understand the basic mechanics of a ransomware attack and develop more robust defenses.

## Features

- **File Encryption**: Files in a specified target directory are encrypted using **Fernet symmetric encryption**, and a `.locked` extension is appended.
- **Ransom Note Creation**: A ransom note (`payransom.txt`) is created with the encryption key and instructions on how to pay for the decryption key.
- **Simulated C2 Communication**: The encryption key is sent to a simulated C2 server (`c2_server.py`), mimicking how real-world ransomware communicates with attackers.
- **Decryption**: Files can be decrypted using a decryption key provided in the ransom note (`decrypt.py`).

## How It Works

### 1. **Server (C2) Listening**:
The C2 server listens for incoming connections from infected machines. When the ransomware script is executed, it connects to the C2 server and sends the encryption key.

### 2. **Running the Ransomware Script**:
The `ransom.py` script does the following:
- Scans the specified target directory.
- Encrypts the files using **Fernet encryption**.
- Creates a ransom note (`payransom.txt`) containing the decryption key and instructions.
- Sends the encryption key to the C2 server.

### 3. **File Encryption**:
Files are encrypted using Fernet encryption. After encryption, the files will have a `.locked` extension, and the original files are deleted.

### 4. **Decryption**:
The `decrypt.py` script can decrypt the encrypted files using the decryption key from the ransom note. The `.locked` extension will be removed, and the original files will be restored.

### 5. **C2 Communication**:
The ransomware communicates with the C2 server by sending the encryption key after encrypting the files. This simulates real-world ransomware sending critical information back to an attacker-controlled server.

## Requirements

- Python 3.x
- `cryptography` library (for Fernet encryption)

To install the necessary dependencies, run:
```bash
pip install cryptography
Usage
1. Run the C2 Server:
Start the C2 server, which listens for incoming connections:

bash

python c2_server.py
2. Run the Ransomware Simulation:
Execute the ransomware simulation script:

bash

python ransom.py
This will:

Encrypt all files in the specified target directory.
Generate a ransom note (payransom.txt) with the encryption key.
Send the encryption key to the C2 server.
3. Decrypt the Files:
To decrypt the files, run the decryption script and provide the decryption key from the ransom note:

bash

python decrypt.py
The decryption will restore the original files by removing the .locked extension.

Important Notes
⚠️ Antivirus/Windows Defender: Running this script on your local machine will likely trigger antivirus software (e.g., Windows Defender) and could flag the files as malicious. To avoid interference, add an exclusion for the files if you're testing in a controlled environment. This is important for testing purposes only!

Ethical Disclaimer:
This project is for educational and testing purposes only. Do not run this script on any system without permission. Unauthorized access and encryption of files are illegal and unethical.

Project Structure
c2_server.py: Simulates the Command-and-Control (C2) server that listens for incoming connections and receives the encryption key.
ransom.py: The ransomware script that encrypts files and creates the ransom note.
decrypt.py: The decryption script that restores the original files using the encryption key.
payransom.txt: The ransom note with the encryption key and decryption instructions.
License
This project is licensed under the MIT License - see the LICENSE file for details.
