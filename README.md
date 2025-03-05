# 🖼️ Secure Data Hiding in Images Using Steganography

## 🔒 Overview
This project implements **image steganography**, allowing users to hide secret messages inside images securely.  
The message is encrypted before embedding, ensuring data security.

---

## 📌 Features
- ✅ Hide secret messages inside images
- ✅ Uses **XOR encryption** for added security
- ✅ Supports **JPG & PNG** image formats
- ✅ Simple and lightweight implementation using **Python & OpenCV**
- ✅ Works on **Windows, Linux, and macOS**

---

## ⚙️ Technologies Used
- 🐍 **Python** - Core programming language
- 🖼️ **OpenCV (`cv2`)** - Image processing
- 📂 **OS Module (`os`)** - File and system operations
- 🔐 **XOR Encryption** - Encrypting secret messages before embedding

---

## 🚀 Installation & Usage
1. Install Dependencies
   Make sure Python is installed. Then, install OpenCV:
   ```bash
   pip install opencv-python

2. Run the Encoder (Hiding Message)
   ```bash
   python steganography.py
  - Enter your secret message and password.
  - The modified image (mypicencrypted.png) will be saved in the project folder.

3. Run the Decoder (Extracting Message)
   ```bash
   python decrypt.py
  - Enter the correct password to retrieve the hidden message.

---

## 📸 Example Output

- 🏞 Original Image →
  ![mypic](https://github.com/user-attachments/assets/d272534d-13f0-4238-a45e-00b74577d083)

- 🖼 Encrypted Image →
  ![mypicencrypted](https://github.com/user-attachments/assets/546a3b4c-8721-43d6-857e-f15325f0faa2)

- 🔐 **Hidden Message Extracted Successfully!**

