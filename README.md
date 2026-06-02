 ## 🔐 Caesar Cipher Implementation (Python)

A simple and educational **Python implementation of the Caesar Cipher encryption algorithm.**
This project demonstrates **left and right shifting encryption and decryption** using basic character manipulation and modular arithmetic.

It is created as a **learning and academic project** to understand how classical cryptography works internally, not as a production-ready security system.

---

## 🧱 Project Structure

```bash
caesar-cipher-python/
│
├── app.py            # Basic CLI version
├── interactive.py    # Rich-powered CLI
├── requirements.txt  # Dependencies
├── LICENSE
└── README.md
```

---

## ✨ Features

### 🔁 Left & Right Shift Support
- User can choose:
  - `L` → Left Shift
  - `R` → Right Shift
- Demonstrates both encryption directions for learning clarity

### 🔒 Encryption
- Encrypts alphabetic characters using a shift key
- Preserves uppercase and lowercase letters
- Keeps spaces and special characters unchanged

### 🔓 Decryption
- Automatically decrypts using the opposite shift direction
- Verifies correctness of the algorithm

### 🧮 Educational Focus
- Clean and readable logic
- Uses modular arithmetic (`% 26`)
- Ideal for beginners in cryptography
- No external dependencies

### 🎨 Rich CLI (Interactive Mode)

- Beautiful colored terminal UI using Rich
- Structured panels for output display
- Interactive prompts with validation
- Enhanced user experience compared to standard CLI

### ⚡ Dual Mode Support

- 🧼 Basic CLI → Lightweight, no dependencies
- 🎨 Rich CLI → Enhanced UI with colors and panels

---

## 🛠 Technologies Used

| **Technology**        | **Role**                        |
|----------------------|----------------------------------|
| **Python 3**         | Core programming language        |
| **ord() / chr()**    | Character-to-ASCII conversion    |
| **Modular Arithmetic** | Circular alphabet shifting     |
| **Rich**             | Styled CLI, colors, panels       |


---

## 📌 Purpose of This Project

This project is built to:
- Understand classical cryptography
- Learn Caesar Cipher encryption & decryption
- Practice modular arithmetic concepts
- Visualize left vs right shifting
- Strengthen Python string manipulation skills

> ⚠️ This project is intended strictly for learning and demonstration purposes.

---
## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ShakalBhau0001/caesar-cipher-python.git
```

### 2️⃣ Navigate to the project folder
```bash
cd caesar-cipher-python
```

### 4️⃣ Install Dependencies

```bash
pip install rich
```

**OR**

```bash
pip install -r requirements.txt
```

### 5️⃣ Running the Project

#### Basic CLI Version

```bash
python app.py
```

#### Rich Interactive Version

```bash
python interactive.py
```

### 6️⃣ Follow the prompts for Basic CLI Version
- Enter a message
- Enter a shift key (integer)
- Choose direction:
  - `L` for Left Shift
  - `R` for Right Shift
- View encrypted and decrypted output

---

## 🔎 Example

```bash
Enter message: HELLO
Enter shift key: 3
Choose direction (L = Left, R = Right): R

Encrypted Message: KHOOR
Decrypted Message: HELLO
```

---

## ⚠️ Limitations

- Not secure for real-world use
- Classical cipher (easily breakable)
- No brute-force protection
- CLI-based interaction only

---

## 🌟 Future Improvements

- Add brute-force mode
- Add English frequency scoring
- Add input validation for shift values
- Add file encryption support
- Create GUI version

---

## ⚠️ Disclaimer

This implementation is created **for educational and learning purposes only.**
The Caesar Cipher is a historically important but insecure encryption method and must not be used to protect real-world sensitive data.

---

## 📸 Preview

![Rich CLI Preview](assets/screenshot.png)

---

## 🪪 Author

> **Developer: Shakal Bhau**

> **GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---
