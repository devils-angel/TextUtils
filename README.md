# TextUtils 📝🔧

**TextUtils** is a Django-based web application that allows users to perform fast and effective text processing tasks directly from the browser. Whether you're a student, developer, writer, or anyone working with raw text, TextUtils helps clean, analyze, and transform text in seconds.

Built with simplicity and learning in mind, this was created as a personal Django project to explore backend routing, form handling, and text manipulation using Python.

## 🚀 Features

- ✅ Remove Punctuation — Strip out symbols and clean your text  
- 🔠 Convert to UPPERCASE — Capitalize all letters  
- ↩️ Remove Newlines — Make your paragraphs continuous   
- 🔢 Count Characters — See how many characters your input has  
- 🧰 Chain Multiple Operations — Combine actions for faster cleanup

## 🛠️ Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML/CSS (via Django templates)  
- **Language:** Python 3.x

## ▶️ How to Run the Project

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

```bash
git clone https://github.com/devils-angel/TextUtils.git
cd TextUtils
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install django
python manage.py runserver
