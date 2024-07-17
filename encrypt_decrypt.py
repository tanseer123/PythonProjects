def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file_in:
        with open(output_file, 'wb') as file_out:
            while True:
                data = file_in.read(1024)
                if not data:
                    break
                encrypted_data = bytes([byte ^ key for byte in data])
                file_out.write(encrypted_data)
    print("File encrypted successfully.")
def decrypt_file(input_file, output_file, key):
    encrypt_file(input_file, output_file, key)  # For simplicity, decryption is same as encryption
if __name__ == "__main__":
    input_file_path = "input_file.txt"
    encrypted_file_path = "encrypted_file.txt"
    decrypted_file_path = "decrypted_file.txt"
    encryption_key = 5
    encrypt_file(input_file_path, encrypted_file_path, encryption_key)
    decrypt_file(encrypted_file_path, decrypted_file_path, encryption_key)