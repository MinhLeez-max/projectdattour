
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
            'image_url': '/static/images/hanoi.jpg'
        },
        {
            'name': 'Hạ Long',
            'description': 'Vịnh Hạ Long - Di sản thiên nhiên thế giới',
            'image_url': '/static/images/halong.jpg'
        },
        {
            'name': 'Sapa',
            'description': 'Vùng đất sương mù với ruộng bậc thang tuyệt đẹp',
            'image_url': '/static/images/sapa.jpg'
        },
        {
            'name': 'Đà Nẵng',
            'description': 'Thành phố đáng sống với bãi biển đẹp',
            'image_url': '/static/images/danang.jpg'
        },
        {
            'name': 'Hội An',
            'description': 'Phố cổ với kiến trúc độc đáo',
            'image_url': '/static/images/hoian.jpg'
        }
    ]
    
    for dest_data in destinations:
        destination, created = Destination.objects.get_or_create(
            name=dest_data['name'],
            defaults={
                'description': dest_data['description'],
                'image_url': dest_data['image_url']
            }
        )
        if created:
            print(f"Created destination: {destination.name}")
        else:
            print(f"Destination already exists: {destination.name}")

if __name__ == '__main__':
    create_destinations()
    print("Destinations created successfully!")
