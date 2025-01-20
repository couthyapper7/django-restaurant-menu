# 🍽️ Django Digital Menu System

A robust, scalable digital menu management system built with Django that enables businesses to create and manage their digital menus with ease. This full-stack application showcases modern web development practices, secure user management, and responsive design.

## 🚀 Key Features

- **Multi-tenant Architecture**: Each business gets its own customizable space with unique URL identifiers
- **Dynamic Menu Management**: Hierarchical category-based menu organization
- **Image Processing**: Automatic WebP conversion and optimization
- **Responsive Design**: Mobile-first approach using Bootstrap
- **Role-Based Access Control**: Secure multi-user environment
- **Dietary Preference Filtering**: Support for various dietary restrictions (Vegan, Sin TACC)
- **Custom Admin Interface**: Intuitive management dashboard

## 🛠️ Technologies Used

- **Backend**: Django 5.0.7
- **Frontend**: HTML5, CSS3, Bootstrap 4.5
- **Database**: SQLite (development) / PostgreSQL (production-ready)
- **Image Processing**: Pillow 10.2.0
- **Authentication**: Django Auth System
- **Version Control**: Git
- **Other Tools**: JWT, REST Framework (API-ready)

## 📦 Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/django-menu-system.git
cd django-menu-system
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run migrations
```bash
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Start development server
```bash
python manage.py runserver
```

## 🏗️ Project Structure

```
django-menu-system/
│
├── main/                   # Main application directory
│   ├── models.py          # Data models
│   ├── views.py           # View logic
│   ├── admin.py           # Admin interface customization
│   ├── forms.py           # Form definitions
│   └── urls.py            # URL routing
│
├── templates/             # HTML templates
│   ├── business_detail.html
│   ├── category_items.html
│   └── item_detail.html
│
├── static/               # Static files (CSS, JS, Images)
│
├── media/               # User-uploaded content
│
└── menu/               # Project configuration
    ├── settings.py
    └── urls.py
```

## 💡 Technical Highlights

### Secure File Upload System
```python
def business_image_upload_path(instance, filename, folder):
    ext = filename.split('.')[-1]
    filename = f"{instance.name}-{folder}.{ext}"
    return os.path.join('business', instance.url_identifier, folder, filename)
```

### Automatic Image Optimization
```python
def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    if self.image:
        img = Image.open(self.image.path)
        webp_image_path = os.path.splitext(self.image.path)[0] + '.webp'
        img.save(webp_image_path, 'WEBP')
```

### Role-Based Access Control
```python
def get_queryset(self, request):
    qs = super().get_queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(business__owner=request.user)
```

## 🔒 Security Features

- CSRF Protection
- User Authentication
- Permission-based Access Control
- Secure File Upload Handling
- XSS Prevention
- SQL Injection Protection

## 📱 Responsive Design

The application implements a mobile-first approach using Bootstrap, ensuring a seamless experience across all devices:

- Fluid grid system
- Responsive images
- Collapsible navigation
- Touch-friendly interfaces

## 🔄 Business Logic

### Models
- **Business**: Core entity representing restaurant/shop
- **Category**: Menu sections (e.g., Appetizers, Main Course)
- **Item**: Individual menu items with details
- **User**: Extended Django user model

### Key Workflows
1. Business Registration
2. Menu Creation and Management
3. Category Organization
4. Item Management
5. Image Processing and Optimization

## 🧪 Testing

```bash
python manage.py test
```

The application includes tests for:
- Model validation
- View responses
- Form processing
- User authentication
- File uploads

## 📈 Future Enhancements

- [ ] RESTful API Implementation
- [ ] OAuth Integration
- [ ] Real-time Updates
- [ ] Advanced Analytics
- [ ] Payment Gateway Integration
- [ ] Multi-language Support
- [ ] PWA Features

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 👤 Author

fausto caminiti
- GitHub: [couthyapper7](https://github.com/couthyapper7)
- LinkedIn: [fausto caminiti](https://www.linkedin.com/in/fausto-caminiti-8774072b7/)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Python Community
