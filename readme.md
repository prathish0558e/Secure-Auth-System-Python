# 🛡️ Secure Authentication System (CLI)

A robust, CLI-based User Authentication System engineered in **Python**.  
This project demonstrates core cybersecurity concepts including **SHA-256 Hashing**, **Cryptographic Salting**, and **Secure Data Persistence** without using external databases.

---

## 🚀 Key Features

* **🔒 SHA-256 Hashing:** Passwords are never stored in plaintext. They are converted into a secure hash before storage.
* **🧂 Cryptographic Salting:** Uses `os.urandom(16)` to generate a unique random salt for every user. This makes **Rainbow Table Attacks** impossible.
* **📂 Custom File Database:** Implements a custom CRUD logic to store credentials in a `.txt` file format securely.
* **🚫 Duplicate Prevention:** Logic to check if a username already exists before registration.
* **✅ Zero-Knowledge Verification:** The system verifies passwords by comparing hashes, ensuring the actual password is never exposed during the login process.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Modules:** `hashlib`, `os` (Standard Library - No pip install required)
* **Interface:** Command Line Interface (CLI)

---

## ⚙️ How It Works (Security Logic)

1.  **Registration:**
    * User enters a password.
    * System generates a random 16-byte **Salt**.
    * System combines `Salt + Password` and hashes it using **SHA-256**.
    * Stores `Username | Salt | Hash` in the database.

2.  **Login:**
    * User enters username & password.
    * System retrieves the stored **Salt** for that user.
    * System hashes the input password with the retrieved salt.
    * Compares the **New Hash** vs **Stored Hash**.
    * Access Granted only if they match perfectly.

---

## ⚠️ Disclaimer
This project is developed for **educational purposes** to demonstrate secure authentication flows. It is designed to show the difference between simple coding vs. secure engineering.

---

### 👨‍💻 Developed by [Prathish Kumar S]
*Aspiring Backend & Security Engineer*
