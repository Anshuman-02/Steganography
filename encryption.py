import cv2
import os

def xor_encrypt(text, key):
    """Encrypts the text using XOR with a key."""
    return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

# Load cover image
img = cv2.imread("mypic.jpg")  # Ensure this image exists in your working directory
if img is None:
    print("Error: Cover image not found!")
    exit()

# Input secret message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Encrypt the message using XOR
enc_msg = xor_encrypt(msg, password)

# Save the password securely (for demonstration, not recommended in real scenarios)
with open("pass.txt", "w") as f:
    f.write(password)

# Embed the encrypted message into the image
index = 0
msg_len = len(enc_msg)
height, width, _ = img.shape

for i in range(height):
    for j in range(width):
        if index < msg_len:
            img[i, j, 0] = ord(enc_msg[index])  # Store in the blue channel
            index += 1
        else:
            break
    if index >= msg_len:
        break
s
# Save the modified image
cv2.imwrite("mypicencrypted.png", img)
print("Secret message securely embedded into image!")

# Open the encrypted image
os.system("start mypicencrypted.png")  # For Windows; use 'open' for macOS and 'xdg-open' for Linux
