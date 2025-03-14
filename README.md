# 🍔 Mealmate - Online Food Ordering System

Mealmate is a Django-based web application that allows users to register as restaurant owners or customers. Restaurant owners can add, edit, and delete restaurants, while customers can browse menus, place orders, and make payments using Razorpay.

## Features

### 🔐 Authentication
- User registration and login (for both restaurant owners and customers)
- Secure authentication using Django's built-in authentication system

### 🏪 Restaurant Management
- Add new restaurants
- Edit and update restaurant details
- Delete restaurants

### 🍽️ Menu & Orders
- Customers can browse menus
- Add items to the cart
- Place orders

### 💳 Payment Integration
- Razorpay integrated for secure online payments

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/mealmate.git
```

### 2️⃣ Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py migrate
```

### 5️⃣ Create a Superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```
Now, open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📂 Directory Structure
```
mealmate/
│── delivery/
│   │── migrations/
│   │── static/
│   │── templates/delivery/
│   │   ├── add_res.html
│   │   ├── base.html
│   │   ├── checkout.html
│   │   ├── cusmenu.html
│   │   ├── customer_home.html
│   │   ├── display_res.html
│   │   ├── failed.html
│   │   ├── index.html
│   │   ├── menu.html
│   │   ├── orders.html
│   │   ├── show_cart.html
│   │   ├── sign_in.html
│   │   ├── sign_up.html
│   │   ├── success.html
│   │   ├── userdata.html
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── forms.py
│   │── models.py
│   │── tests.py
│   │── views.py
│── manage.py
│── requirements.txt
```

## 🔗 API Endpoints (If Using Django REST Framework)

| Method | Endpoint | Description |
|--------|------------------------|-----------------------------|
| GET    | /restaurants/          | List all restaurants       |
| POST   | /restaurants/add/      | Add a new restaurant       |
| PUT    | /restaurants/update/<id>/ | Update restaurant details |
| DELETE | /restaurants/delete/<id>/ | Delete a restaurant       |
| GET    | /menu/                 | Get menu items             |
| POST   | /order/                | Place an order             |

## 💰 Razorpay Payment Integration

1. Sign up at [Razorpay](https://razorpay.com/)
2. Get API keys from Razorpay Dashboard
3. Add API keys to Django settings:

```python
RAZORPAY_KEY_ID = "your_key_id"
RAZORPAY_KEY_SECRET = "your_key_secret"
```

