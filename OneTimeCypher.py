import numpy as np

def generate_playfair_matrix(key):
    key = key.replace("J", "I")  # Playfair cipher treats I and J as the same
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = "".join(dict.fromkeys(key + alphabet))  # Remove duplicates, preserve order
    return np.array(list(matrix)).reshape(5, 5)

def find_position(matrix, letter):
    row, col = np.where(matrix == letter)
    return row[0], col[0]

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"
        if a == b:
            result += a + "X"
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2 != 0:
        result += "X"
    return result

def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = prepare_text(text)
    encrypted_text = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return encrypted_text

def playfair_decrypt(text, key):
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return decrypted_text.replace("X", "")  # Remove padding X if any

# Example usage
key = "SECRETKEY"
name = "Looja Manandhar"
encrypted_name = playfair_encrypt(name, key)
decrypted_name = playfair_decrypt(encrypted_name, key)

print(f"Original Name: {name}")
print(f"Encrypted Name: {encrypted_name}")
print(f"Decrypted Name: {decrypted_name}")
