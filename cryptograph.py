# cryptograph.py
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os, base64


class CryptographyManager:
    """
    Enhanced class for encrypting and decrypting files using AES-GCM.
    Features:
    - Uses AES-GCM for authenticated encryption
    - Supports any file type (binary safe)
    - Key derivation using PBKDF2
    - Random nonce generation for each encryption
    """

    def __init__(self, key: str, iterations: int = 3):
        self.iterations = iterations
        # Convert the string key to a proper encryption key using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'static_salt',  # In production, use a random salt per key
            iterations=100000,
        )
        self.key = kdf.derive(key.encode())
        self.aesgcm = AESGCM(self.key)

    def encrypt(self, data: bytes) -> bytes:
        """
        Encrypt data using AES-GCM with multiple iterations
        Returns: base64 encoded encrypted data with nonce
        """
        encrypted_data = data
        for _ in range(self.iterations):
            nonce = os.urandom(12)  # Generate a new nonce for each iteration
            encrypted_data = self.aesgcm.encrypt(nonce, encrypted_data, None)
            encrypted_data = nonce + encrypted_data  # Prepend nonce to encrypted data

        return base64.b64encode(encrypted_data)

    def decrypt(self, encrypted_data: bytes) -> bytes:
        """
        Decrypt data using AES-GCM with multiple iterations
        """
        data = base64.b64decode(encrypted_data)

        for _ in range(self.iterations):
            nonce = data[:12]  # Extract nonce
            data = data[12:]  # Get encrypted data
            data = self.aesgcm.decrypt(nonce, data, None)

        return data


def generate_key() -> str:
    """Generate a random key and return it as a base64 encoded string"""
    return base64.b64encode(os.urandom(32)).decode('utf-8')


def read_file(file_path: str) -> bytes:
    """Read file in binary mode"""
    with open(file_path, 'rb') as file:
        return file.read()


def write_file(file_path: str, data: bytes):
    """Write data to file in binary mode"""
    with open(file_path, 'wb') as file:
        file.write(data)
