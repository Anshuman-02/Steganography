import cv2

def xor_decrypt(encrypted_text, key):
    """Decrypts the text using XOR with a key."""
    return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(encrypted_text))

# Load the encrypted image
img = cv2.imread("mypicencrypted.png")  # Ensure this image exists in your working directory
if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Ask user for the password
password = input("Enter the passcode to decrypt the message: ")

# Extract the hidden message
height, width, _ = img.shape
extracted_chars = []

for i in range(height):
    for j in range(width):
        char_ascii = img[i, j, 0]  # Extract from the blue channel
        if char_ascii == 0:
            break  # Stop if we reach an empty pixel
        extracted_chars.append(chr(char_ascii))
    if char_ascii == 0:
        break

# Convert ASCII values to text
enc_msg = "".join(extracted_chars)

# Decrypt the message using XOR
dec_msg = xor_decrypt(enc_msg, password)

# Display the hidden message
print("\n🔓 Decrypted Message:", dec_msg)
