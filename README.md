# 🐾 TestingPets

TestingPets is an automated testing project built using the Page Object Model (POM) design pattern.  
It contains UI tests for a pet-related website using pytest.

---

## 🚀 Tech Stack

- Python  
- Pytest  
- Selenium

---

## 📁 Project Structure

TestingPets/ │ ├── Pages/ │   ├── base_page.py │   ├── login_page.py │   ├── main_page.py │   ├── profile_page.py │   ├── locators.py │   └── init.py │ ├── Tests/ │   ├── test_login_pages.py │   ├── test_profile_pages.py │   ├── test_main_pages.py │   └── init.py │ ├── conftest.py ├── pytest.ini ├── requirements.txt └── README.md

---

## 📄 Pages Description

- base_page.py – contains common methods used across all pages  
- login_page.py – methods for login functionality  
- main_page.py – methods for main page interactions  
- profile_page.py – methods for profile page interactions  
- locators.py – stores all element locators  

---

## 🧪 Tests Description

- test_login_pages.py – tests related to login functionality  
- test_profile_pages.py – tests related to profile page  
- test_main_pages.py – tests related to main page  

---

## ⚙️ Installation

1. Clone the repository:
git clone https://github.com/your-username/TestingPets.git

2. Navigate to the project folder:
cd TestingPets

3. Create and activate virtual environment:
python -m venv venv venv\Scripts\activate   # Windows source venv/bin/activate  # Mac/Linux

4. Install dependencies:
pip install -r requirements.txt

---

## ▶️ Running Tests

Run all tests:
pytest

Run tests with detailed output:
pytest -v

---

## 🏷️ Pytest Configuration

- pytest.ini contains custom markers  
- conftest.py contains shared fixtures  

---

## 📌 Notes

- The venv folder is not included in the repository  
- Make sure all dependencies are installed before running tests  

---

## 👨‍💻 Author

The project was written by Vitali Katruk
