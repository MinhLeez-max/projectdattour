
import os
import django
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourapp.settings')
django.setup()

from apps.tours.models import Destination

def create_destinations():
    destinations = [
        {
            'name': 'Hà Nội',
            'description': 'Thủ đô ngàn năm văn hiến với nhiều di tích lịch sử',
            'image': 'https://images.unsplash.com/photo-1509475826633-fed577a2c71b?w=500&h=300&fit=crop'
        },
        {
            'name': 'Hạ Long',
            'description': 'Vịnh Hạ Long - Di sản thiên nhiên thế giới',
            'image': 'https://images.unsplash.com/photo-1528127269322-539801943592?w=500&h=300&fit=crop'
        },
        {
            'name': 'Sapa',
            'description': 'Vùng đất sương mù với ruộng bậc thang tuyệt đẹp',
            'image': 'https://images.unsplash.com/photo-1566228015668-4c45dbc4e2f5?w=500&h=300&fit=crop'
        },
        {
            'name': 'Đà Nẵng',
            'description': 'Thành phố đáng sống với bãi biển đẹp',
            'image': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=500&h=300&fit=crop'
        },
        {
            'name': 'Hội An',
            'description': 'Phố cổ với kiến trúc độc đáo',
            'image': 'https://images.unsplash.com/photo-1583417319070-4a69db38a482?w=500&h=300&fit=crop'
        }
    ]
    
    for dest_data in destinations:
        destination, created = Destination.objects.get_or_create(
            name=dest_data['name'],
            defaults={
                'description': dest_data['description'],
                'image': dest_data['image']
            }
        )
        if created:
            print(f"Created destination: {destination.name}")
        else:
            print(f"Destination already exists: {destination.name}")

if __name__ == '__main__':
    create_destinations()
    print("Destinations created successfully!")
