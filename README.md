
# Tour App - Django Project

## Cấu trúc dự án

```
├── backend/                 # Django backend
│   ├── apps/               # Django apps
│   │   ├── accounts/       # Quản lý tài khoản
│   │   ├── bookings/       # Quản lý đặt tour
│   │   ├── core/          # App chính
│   │   └── tours/         # Quản lý tour
│   ├── tourapp/           # Django project settings
│   ├── manage.py          # Django management
│   ├── db.sqlite3         # Database
│   ├── create_destinations.py  # Script tạo điểm đến
│   └── create_tours.py    # Script tạo tour
├── frontend/              # Frontend assets
│   ├── templates/         # Django templates
│   └── static/           # CSS, JS, images
└── README.md

```

## Chạy dự án

1. Chạy server Django:
```bash
cd backend
python manage.py runserver 0.0.0.0:5000
```

2. Hoặc sử dụng nút Run để khởi động server tự động.

## Migration

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

