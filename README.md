# 🗂️ Django CRM Web Application

A fully functional CRM (Customer Relationship Management) system built using Django and MySQL.  
This project demonstrates my ability to develop **full-stack Django web apps** with custom templates, dynamic forms, user authentication, and real business logic — not just APIs.

---

## 🎯 Project Highlights

🔹 Full-stack Django app using MVT architecture  
🔹 Session-based user authentication system  
🔹 Bootstrap-integrated frontend with Django templates  
🔹 Secure login, logout, and protected views  
🔹 Create, update, and delete leads/clients  
🔹 Admin dashboard with extended model control  
🔹 Custom models, forms, and relational data handling  
🔹 Database integration using MySQL  
🔹 Version control with Git and GitHub

---

## 🛠️ Tech Stack

- **Backend:** Python, Django (MVT)
- **Frontend:** HTML, CSS, Bootstrap (via Django Templates)
- **Database:** MySQL
- **Authentication:** Session-based
- **Tools:** Git, GitHub, Django Admin

---

## 🚀 How to Run the Project Locally

Follow these steps to run the project on your local machine:

1. **Clone the Repository**
   ```bash
     git clone https://github.com/Alii0319/dcrm.git
     cd your-crm-repo

2. **Create and Activate Virtual Environment**
  python -m venv env
  source env/bin/activate  # For Linux/Mac
  env\Scripts\activate     # For Windows

3. **Install Dependencies**
  pip install -r requirements.txt

4. **Configure MySQL Database**

Open settings.py
Add your MySQL config:
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5.  **Run Migrations**

   python manage.py makemigrations
   python manage.py migrate

**6. Create Superuser (optional)**
    
    python manage.py createsuperuser
    
**7. Start Development Server**
    python manage.py runserver

📁 Folder Structuredcrm/                               # Main project root
│
├── dcrm/                           # Django project settings folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── website/                        # Main Django app
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/                  # HTML templates
│   │   ├── add_record.html
│   │   ├── customer_record.html
│   │   ├── home.html
│   │   ├── layout.html
│   │   ├── register.html
│   │   └── update_record.html
│   └── static/                     # Static files (CSS, JS)
│
├── manage.py                      # Django CLI entry point
├── mydb.py                        # Custom database script 
├── requirements.txt              # Project dependencies
├── venv/                         # Virtual environment (excluded from version control)
└── .vscode/                      # VS Code settings 


🙋‍♂️ Author
Developed by Ali Raza
🔗 Upwork Profile: https://www.upwork.com/freelancers/~01b104d4be9f7ef9e5?s=1110580748673863680
