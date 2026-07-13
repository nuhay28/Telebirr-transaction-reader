# TeleBirr Transaction Reader

## 📖 Project Description

This project is a Python program that reads TeleBirr transaction records from a text file, calculates the total amount spent by each customer using a dictionary, displays the results sorted by the highest total, and saves the summary to a report file.

It also demonstrates file handling and exception handling in Python.

---

## 📂 Project Structure

```
Telebirr-transaction-reader/
│
├── transaction_report.py
├── transactions.txt
├── report.txt
└── README.md
```

---

## 🚀 Features

- Read transaction data from a text file
- Store customer totals using a Python dictionary
- Sort customers by total spending
- Display results on the console
- Save the summary to `report.txt`
- Handle missing files using `try` and `except`

---

## 📝 Input Format

The `transactions.txt` file contains one transaction per line.

Example:

```
Abebe,250.00
Kalkidan,120.50
Abebe,75.25
```

---

## 📊 Sample Output

```
Selam: 580.00
Kalkidan: 380.49
Abebe: 335.25
Mekdes: 315.75
Yonas: 67.50
```

---

## ▶️ How to Run

1. Make sure Python is installed.
2. Place `transactions.txt` in the project folder.
3. Run the program:

```bash
python transaction_report.py
```

The program will display the transaction summary and generate a `report.txt` file.

---

## 🛠 Technologies Used

- Python 3
- Dictionaries
- File Handling
- Exception Handling

---

## 👤 Author

**Nuhamin**