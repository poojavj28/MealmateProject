# Mealmate - Online Food Ordering System

Mealmate is a Django-based web application that allows users to register as restaurant owners or customers. Restaurant owners can add, edit, and delete restaurants, while customers can browse menus, place orders, and make payments using Razorpay.

## Features

### Authentication
- User registration and login (for both restaurant owners and customers)
- Secure authentication using Django's built-in authentication system

![Authentication](assets/authentication.png)

### Restaurant Management
- Add new restaurants
- Edit and update restaurant details
- Delete restaurants

![Restaurant Management](assets/restaurant_management.png)

### Menu & Orders
- Customers can browse menus
- Add items to the cart
- Place orders

![Menu & Orders](assets/menu_orders.png)

### Payment Integration
- Razorpay integrated for secure online payments

![Payment Integration](assets/payment_integration.png)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/mealmate.git
cd mealmate
```

![Clone Repository](assets/clone_repo.png)

### 2. Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
```

![Virtual Environment](assets/venv_setup.png)

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

![Install Dependencies](assets/install_dependencies.png)

### 4. Apply Migrations
```bash
python manage.py migrate
```

![Apply Migrations](assets/migrations.png)

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```

![Create Superuser](assets/create_superuser.png)

### 6. Run the Development Server
```bash
python manage.py runserver
```
Now, open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

![Run Server](assets/run_server.png)

## Directory Structure
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

![Directory Structure](assets/directory_structure.png)

## API Endpoints (If Using Django REST Framework)

| Method | Endpoint | Description |
|--------|------------------------|-----------------------------|
| GET    | /restaurants/          | List all restaurants       |
| POST   | /restaurants/add/      | Add a new restaurant       |
| PUT    | /restaurants/update/<id>/ | Update restaurant details |
| DELETE | /restaurants/delete/<id>/ | Delete a restaurant       |
| GET    | /menu/                 | Get menu items             |
| POST   | /order/                | Place an order             |

![API Endpoints](assets/api_endpoints.png)

## Razorpay Payment Integration

1. Sign up at [Razorpay](https://razorpay.com/)
2. Get API keys from Razorpay Dashboard
3. Add API keys to Django settings:

```python
RAZORPAY_KEY_ID = "your_key_id"
RAZORPAY_KEY_SECRET = "your_key_secret"
```

![Razorpay Integration](assets/razorpay_setup.png)

---

This guide provides all the necessary steps to set up and run the Mealmate project efficiently. Happy coding! 🚀

