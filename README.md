# Django Restaurant Menu

A proprietary, dynamic restaurant menu system built with Django. This application allows restaurant owners to create and manage their digital menus with ease, featuring multiple themes and user-specific business management.

## Important Notice

This is a private repository containing proprietary code. Viewing is permitted, but any use, modification, or distribution of this code is strictly prohibited without explicit written permission from the owner

## Features

- User authentication for restaurant owners
- Customizable menu categories and items
- Multiple theme options for menu display
- Responsive design for various devices
- Image upload and processing for menu items
- URL-based access to individual restaurant menus

## Technology Stack

- Python 3.8+
- Django 5.0.7
- Pillow 10.2.0
- python-dotenv 1.0.0
- gunicorn 20.1.0
- whitenoise 6.5.0
- django-storages 1.13.2
- boto3 1.28.3

## Project Structure

```
django-restaurant-menu/
├── menu/                   # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                   # Main application
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── themes/
│           ├── default_1/
│           ├── default_2/
│           ├── dropdown/
│           └── dropdown_2/
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User-uploaded files
├── manage.py
├── requirements.txt
└── .env                    # Environment variables (not in version control)
```

## Key Components

### Models (models.py)

1. `Business`: Represents a restaurant with its details and theme.
2. `Category`: Represents a menu category (e.g., "Appetizers", "Main Courses").
3. `Item`: Represents a menu item with details like name, description, and price.

### Views (views.py)

1. `BusinessDetailView`: Displays the main page for a restaurant's menu.
2. `CategoryItemsView`: Shows items for a specific category.
3. `item_detail`: Displays details for a specific menu item.

### Admin (admin.py)

Custom admin classes for each model, ensuring that restaurant owners can only manage their own businesses, categories, and items.

## Deployment

This project is configured to use AWS S3 for static and media file storage. Ensure you have set up an S3 bucket and configured the necessary environment variables before deploying.

For production deployment:
1. Set `DEBUG=False` in your environment variables.
2. Use a production-ready database like PostgreSQL.
3. Set up a reverse proxy server like Nginx.
4. Use Gunicorn as the application server.

## License

This project is proprietary software. All rights are reserved. No use, modification, or distribution is permitted without explicit written permission from the owner, Fausto Caminiti.

© Fausto Caminiti, 2024

For inquiries about licensing or usage, please contact couthyapper79@gmail.com.
