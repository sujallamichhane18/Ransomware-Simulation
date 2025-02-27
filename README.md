Ransomware Simulation Project
This project simulates the behavior of ransomware, focusing on file encryption, the creation of ransom notes, and command-and-control (C2) server communication. The simulation provides insights into how ransomware encrypts files, how keys are sent to C2 servers, and how encrypted files can be decrypted using the provided key.

Overview
The ransomware simulation is written in Python and demonstrates:

File encryption using Fernet symmetric encryption.
Creation of ransom notes with decryption instructions.
Simulated communication with a C2 server, where the encryption key is exfiltrated.
Decryption of encrypted files using the encryption key.
The goal is to understand the basic mechanisms of a ransomware attack and to build more robust defenses against such threats.

How It Works
1. Server Listening
The C2 server listens for incoming connections from infected machines. Once the ransomware script is executed, it connects to the C2 server and sends important data, including the encryption key.

2. Running the Ransomware Script
The script ransom.py is responsible for:

Scanning the specified target directory.
Encrypting files using Fernet encryption, appending a .locked extension to the files.
Creating a ransom note (payransom.txt) containing the decryption key and instructions.
3. File Encryption
All files in the specified target directory are encrypted. After encryption, only the .locked files remain, and the original files are deleted.

4. Decryption Using Key
The decryption script (decrypt.py) can be used to recover the original files by entering the encryption key provided in the ransom note. This will remove the .locked extension and restore the files.

5. C2 Communication
After the encryption, the encryption key is sent to the C2 server, mimicking how real-world ransomware attacks send stolen keys to an attacker-controlled server.

Important Notes
⚠️ Windows Defender / Antivirus Software:
Running this script on your local machine will likely trigger antivirus software (e.g., Windows Defender) and could flag the files as malicious. Make sure to add an exclusion for the files if you're testing in a controlled environment to avoid interference. This is important for testing purposes only!

Project Structure
c2_server.py: Simulates the Command-and-Control (C2) server that listens for incoming connections and receives the encryption key from the ransomware script.
ransom.py: The ransomware script that encrypts files in the target directory and creates the ransom note with the decryption key.
decrypt.py: The decryption script that takes the provided decryption key and restores the encrypted files.
payransom.txt: The ransom note that includes the decryption key and ransom instructions.
Requirements
Python 3.x
cryptography library (for Fernet encryption)
To install the necessary dependencies, run the following:

bash
Copy
Edit
pip install cryptography
Usage
1. Run the C2 Server
First, start the C2 server by running:

bash
Copy
Edit
python c2_server.py
This will start the server, which will listen for incoming connections from the ransomware script.

2. Run the Ransomware Simulation
Execute the ransomware simulation script:

bash
Copy
Edit
python ransom.py
This will:

Encrypt all files in the specified target directory.
Generate a ransom note (payransom.txt) with the encryption key.
Send the encryption key to the C2 server.
3. Decryption
To decrypt the files, run the decryption script and provide the decryption key (from the ransom note):

bash
Copy
Edit
python decrypt.py
The decryption will restore the original files by removing the .locked extension.

Disclaimer
This project is for educational and testing purposes only. Do not run this script on any system without permission. Unauthorized access and encryption of files is illegal and unethical.

License
This project is licensed under the MIT License - see the LICENSE file for details.
