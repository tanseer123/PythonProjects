import hashlib


def hash_password(password):
# Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def store_password(self, username, password):
        hashed_password = hash_password(password)
        self.passwords[username] = hashed_password

    def verify_password(self, username, password):
        if username in self.passwords:
            hashed_password = self.passwords[username]
            return hashed_password == hash_password(password)
        else:
            return False
if __name__ == "__main__":
    manager = PasswordManager()
    manager.store_password("user1", "pa$$w0rd123")
    manager.store_password("user2", "qwerty456")
    # Example usage:
    print(manager.verify_password("user1", "password123"))  #False
    print(manager.verify_password("user2", "qwerty456"))  #True