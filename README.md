# TeleBirr Transaction Reader

## 📖 Project Description

The **TeleBirr Transaction Reader** is a Python project that reads TeleBirr transaction records from a text file, calculates the total amount spent by each customer using a dictionary, displays the results sorted by the highest total, and handles missing files gracefully using exception handling.

This project demonstrates the use of Python dictionaries, file handling, sorting, and exception handling.

---

## 📂 Project Structure

```
Telebirr-transaction-reader/
│
├── README.md
├── telebirr_transaction_reader.py
├── transaction_report.py
└── transactions.txt
```

---

## ✨ Features

- Read transaction records from `transactions.txt`.
- Calculate the total amount spent by each customer.
- Store customer totals using a Python dictionary.
- Display the summary sorted from highest to lowest total.
- Handle missing files using `try` and `except FileNotFoundError`.

---

## 📝 Input Format

The `transactions.txt` file contains one transaction per line in the following format:

```
CustomerName,Amount
```

Example:

```
Abebe,250.00
Kalkidan,120.50
Abebe,75.25
Mekdes,300.00
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/nuhay28/Telebirr-transaction-reader.git
```

2. Open the project folder:

```bash
cd Telebirr-transaction-reader
```

3. Run the program:

```bash
python transaction_report.py
```

The program will read the transaction data, display the transaction summary, and generate a report during execution if implemented.

---

## 🛠 Technologies Used

- Python 3
- Dictionaries
- File Handling
- Exception Handling

---

## 👤 Author

**Nuhamin**