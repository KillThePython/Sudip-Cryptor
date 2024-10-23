from cryptography.fernet import Fernet


class CryptographyManager:
    """
    Class for encrypting and decrypting data.
    """

    def __init__(self, key: str, layers: int = 3):
        self.key = key
        self.layers = layers
        self.fernet = Fernet(self.key)

    def encrypt(self, data: str) -> bytes:
        for i in range(self.layers):
            data = self.fernet.encrypt(data.encode())  # Encode the string to bytes
            data = data.decode()
        return data.encode()

    def decrypt(self, data: bytes) -> str:
        for i in range(self.layers):
            data = self.fernet.decrypt(data)  # No need to encode or decode here
        return data.decode()  # Decode the final decrypted bytes to a string
    

def write_to_file(file_path: str, data: str | bytes):
    try:
        data = data.decode()
    except Exception:
        pass

    with open(file_path, "w") as file:
        file.write(data)


def read_from_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()
    

def generate_key() -> str:
    return Fernet.generate_key().decode()