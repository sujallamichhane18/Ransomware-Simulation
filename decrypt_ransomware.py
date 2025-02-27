# decrypt.py
from cryptography.fernet import Fernet
import os

TARGET_DIR = r"" #Ransomware attack file location
RANSOM_NOTE = "payransom.txt"
ENCRYPTED_EXTENSION = ".locked"

key = input("Enter the decryption key from payransom.txt: ").encode()
decipher = Fernet(key)

for root, dirs, files in os.walk(TARGET_DIR):
    for file in files:
        if file == RANSOM_NOTE:
            continue
        if file.endswith(ENCRYPTED_EXTENSION):
            encrypted_path = os.path.join(root, file)
            original_path = encrypted_path[:-len(ENCRYPTED_EXTENSION)]  # Remove .locked
            with open(encrypted_path, "rb") as f:
                encrypted_data = f.read()
            decrypted_data = decipher.decrypt(encrypted_data)
            with open(original_path, "wb") as f:
                f.write(decrypted_data)
            os.remove(encrypted_path)
            print(f"Decrypted: {original_path}")
os.remove(os.path.join(TARGET_DIR, RANSOM_NOTE))
print("Decryption complete.")