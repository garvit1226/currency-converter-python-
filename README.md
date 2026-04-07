# 💱 Currency Converter CLI (Python)

A simple and efficient **Command Line Currency Converter** built using Python and ExchangeRate API.
It allows users to convert currencies in real-time, view supported currency codes, and track conversion history.

---

## 🚀 Features

* 🌍 Real-time currency conversion
* 📋 Displays all available currencies (2-column formatted layout)
* 🔍 Input validation for currency codes
* 💾 Stores conversion history in a file
* 📖 View past conversions anytime
* 🎯 Clean and user-friendly CLI interface
* 📊 Formatted output with commas and 2 decimal precision

---

## 🛠️ Tech Stack

* Python 🐍
* Requests Library
* ExchangeRate API

---

## 📦 Installation

1. Clone the repository:

```
git clone https://github.com/garvit1226/currency-converter.git
cd currency-converter
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Add your API key:

Create a file named `api.py` and add:

```
api_key = "YOUR_API_KEY"
```

---

## ▶️ Usage

Run the program:

```
python main.py
```

---

## 🎬 Demo



---

## 🖥️ Menu Options

* `1` → Convert Currency
* `2` → View Conversion History
* `3` → Exit

---

## 📌 Example Output

```
USD - United States Dollar        INR - Indian Rupee

Enter base currency: USD  
Enter amount: 100  
Enter target currency: INR  

Converted amount: 8,345.67  
1 USD = 83.45 INR
```

---

## 📂 Project Structure

```
currency-converter/
│── main.py
│── api.py
│── history.txt
│── requirements.txt
│── README.md
│── assets/
│   └── demo.gif
```

---

## 🔮 Future Improvements

* GUI version using Tkinter
* Currency search/filter feature
* Currency symbols (₹, $, €)
* Export history to CSV
* Web version (Flask/Django)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!
