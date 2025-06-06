# Generated by Django 5.2 on 2025-05-06 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên loại tour')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug URL')),
                ('description', models.TextField(blank=True, verbose_name='Mô tả')),
                ('icon', models.CharField(blank=True, max_length=50, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Loại tour',
                'verbose_name_plural': 'Loại tour',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tên tour')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug URL')),
                ('short_description', models.TextField(verbose_name='Mô tả ngắn')),
                ('description', models.TextField(verbose_name='Mô tả chi tiết')),
                ('duration', models.PositiveSmallIntegerField(verbose_name='Số ngày')),
                ('price', models.DecimalField(decimal_places=0, max_digits=12, verbose_name='Giá tour')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True, verbose_name='Giá khuyến mãi')),
                ('main_image', models.CharField(max_length=255, verbose_name='Ảnh chính')),
                ('itinerary', models.TextField(verbose_name='Lịch trình')),
                ('includes', models.TextField(verbose_name='Bao gồm')),
                ('excludes', models.TextField(verbose_name='Không bao gồm')),
                ('terms', models.TextField(verbose_name='Điều khoản')),
                ('transport', models.CharField(choices=[('car', 'Ô tô'), ('plane', 'Máy bay'), ('train', 'Tàu hỏa'), ('ship', 'Tàu thủy'), ('mixed', 'Kết hợp')], default='car', max_length=20, verbose_name='Phương tiện')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Nổi bật')),
                ('is_active', models.BooleanField(default=True, verbose_name='Đang hoạt động')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Cập nhật lần cuối')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.destination', verbose_name='Điểm đến')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tourcategory', verbose_name='Loại tour')),
            ],
            options={
                'verbose_name': 'Tour du lịch',
                'verbose_name_plural': 'Tour du lịch',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Họ tên')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('rating', models.PositiveSmallIntegerField(verbose_name='Đánh giá (1-5)')),
                ('comment', models.TextField(verbose_name='Nhận xét')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Đã duyệt')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tours.tour', verbose_name='Tour')),
            ],
            options={
                'verbose_name': 'Đánh giá',
                'verbose_name_plural': 'Đánh giá',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TourDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Ngày khởi hành')),
                ('end_date', models.DateField(verbose_name='Ngày kết thúc')),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True, verbose_name='Giá riêng')),
                ('available_seats', models.PositiveSmallIntegerField(default=20, verbose_name='Số chỗ còn lại')),
                ('is_active', models.BooleanField(default=True, verbose_name='Đang hoạt động')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='tours.tour', verbose_name='Tour')),
            ],
            options={
                'verbose_name': 'Ngày khởi hành',
                'verbose_name_plural': 'Ngày khởi hành',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=255, verbose_name='Đường dẫn hình ảnh')),
                ('caption', models.CharField(blank=True, max_length=200, verbose_name='Chú thích')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Thứ tự')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tours.tour', verbose_name='Tour')),
            ],
            options={
                'verbose_name': 'Hình ảnh tour',
                'verbose_name_plural': 'Hình ảnh tour',
                'ordering': ['order'],
            },
        ),
    ]
