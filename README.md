# Virtual Store UAB - Dashboard & Inventory Management System

A comprehensive and powerful administration dashboard and inventory management system designed for **Virtual Store UAB**. Built on top of **Flask-AppBuilder** and powered by **MySQL** and **SQLAlchemy**, this application provides a robust, user-friendly interface to manage business categories, product catalogs, vendor tracking, sales transactions, and visual analytics reports.

---

## 🚀 Key Features

### 🔐 1. Role-Based Security & User Management
* Built-in authentication (DB-based) with strict role-based access control (RBAC).
* Easily create, manage, and assign custom permissions for admins, managers, and public roles.
* Self-registration support and comprehensive login/logout flows.

### 📦 2. Inventory & Catalog Management
* **Categories (Categorías):** Complete CRUD capabilities to structure inventory. Support for references, descriptions, custom status (active/inactive), and image uploads.
* **Products (Productos):** Catalog management featuring customizable pricing in Bolivianos (Bs.), descriptions, images, association with categories, and active stock availability.
* **Vendors (Proveedores):** High-level vendor directory management for tracking company names (razón social), key contacts, phone numbers, emails, addresses, and status.

### 💰 3. Sales Register & Operations
* Real-time logging of individual sale transactions containing:
  * Sold product names.
  * Quantities and individual unit pricing.
  * Automatic calculation of transaction total totals in Bs.
  * Timestamps representing the transaction date.

### 📊 4. Interactive Reporting Dashboard
* Visual analytics interface `/reportes` featuring:
  * **Global Transactions Count:** Live tracker for the total number of processed sales.
  * **Gross Income Revenue:** Total sales revenue calculated dynamically using database summaries.
  * **Product Breakdown Chart:** Sales distribution summary grouping total sold quantities by product.

### 🌐 5. Multilingual Localization
* Dynamic translation support utilizing **Flask-Babel**.
* The application is fully optimized and pre-configured in **Spanish (`es`)** with multi-language flags ready for English, Portuguese, German, Chinese, Russian, and Polish.

---

## 🛠️ Technology Stack

* **Core Framework:** Python 3.12+ & [Flask 3.1.3](https://flask.palletsprojects.com/)
* **Rapid Admin Dev Engine:** [Flask-AppBuilder 5.2.1](https://flask-appbuilder.readthedocs.io/)
* **ORM & DB Engine:** [SQLAlchemy 2.0.49](https://www.sqlalchemy.org/) & [Flask-SQLAlchemy 3.1.1](https://flask-sqlalchemy.palletsprojects.com/)
* **Database Driver:** [PyMySQL 1.1.3](https://pymysql.readthedocs.io/) (for MySQL integrations)
* **Form & Validation Engine:** WTForms 3.2.2 & Flask-WTF 1.3.0
* **Translation Handler:** Flask-Babel 4.0.0

---

## 🏗️ Project Architecture & Structure

```bash
dashboard-app/
│
├── dashboard-app/             # Core Flask application folder
│   ├── app/
│   │   ├── __init__.py        # Application factory & setup
│   │   ├── extensions.py      # Global DB & AppBuilder extensions
│   │   ├── models.py          # SQLAlchemy schemas (Categoria, Producto, Proveedor, Venta)
│   │   ├── views.py           # ModelViews, formatters, and custom reports
│   │   ├── templates/         # Jinja2 templates (custom reportes.html, index, etc.)
│   │   └── translations/      # Multi-language translation compilations
│   │
│   ├── config.py              # Application settings, secrets, and MySQL connection configurations
│   └── run.py                 # Main application runner script
│
├── requirements.txt           # Virtual environment python dependencies
└── README.md                  # System instruction & documentation
```

---

## ⚡ Installation & Quick Start

### 📋 Prerequisites
* Python 3.12 or newer installed on your machine.
* A running instance of a MySQL Database Server (e.g., XAMPP, WampServer, or Docker MySQL).

### 🛠️ Step-by-Step Setup

**1. Clone the project and navigate to the directory:**
```powershell
cd "D:\uab\dashboardapp-main (1)\dashboardapp-main\dashboard-app"
```

**2. Setup a virtual environment:**
```powershell
python -m venv venv
```

**3. Activate the virtual environment:**
* **On Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
* **On Windows (Command Prompt):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```
* **On Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

**4. Install project dependencies:**
```powershell
pip install -r requirements.txt
```

**5. Database Configuration:**
1. Open your MySQL client/server (e.g., phpMyAdmin).
2. Create a new database named `appdashboard`:
   ```sql
   CREATE DATABASE appdashboard CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
3. Make sure the database credentials in `dashboard-app/config.py` match your setup:
   ```python
   SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/appdashboard"
   ```

**6. Generate Admin Credentials:**
Flask-AppBuilder handles DB migrations automatically on startup, but you must register an initial admin account to access the panel. Run:
```powershell
cd dashboard-app
flask fab create-admin
```
*Provide a username, first name, last name, email, and choose a secure password.*

**7. Run the Application:**
Start the development server:
```powershell
python run.py
```

Open your browser and navigate to **[http://localhost:8080](http://localhost:8080)**. Use the credentials created in Step 6 to log in and start using your Virtual Store Dashboard!
