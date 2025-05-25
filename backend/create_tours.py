
import os
import django
import sys
from decimal import Decimal
from datetime import datetime, timedelta

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourapp.settings')
django.setup()

from apps.tours.models import Tour, Destination

def create_tours():
    # Get destinations
    destinations = Destination.objects.all()
    
    if not destinations:
        print("No destinations found. Please run create_destinations.py first.")
        return
    
    tours_data = [
        {
            'title': 'Tour Hà Nội - Hạ Long 3N2Đ',
            'description': 'Khám phá thủ đô và vịnh Hạ Long tuyệt đẹp',
            'price': Decimal('2500000'),
            'duration': 3,
            'max_participants': 20,
            'destination': 'Hạ Long'
        },
        {
            'title': 'Tour Sapa - Chinh phục Fansipan 4N3Đ',
            'description': 'Khám phá Sapa và chinh phục nóc nhà Đông Dương',
            'price': Decimal('3200000'),
            'duration': 4,
            'max_participants': 15,
            'destination': 'Sapa'
        },
        {
            'title': 'Tour Đà Nẵng - Hội An 5N4Đ',
            'description': 'Trải nghiệm miền Trung đầy nắng và gió',
            'price': Decimal('4500000'),
            'duration': 5,
            'max_participants': 25,
            'destination': 'Đà Nẵng'
        }
    ]
    
    for tour_data in tours_data:
        try:
            destination = destinations.get(name=tour_data['destination'])
            tour, created = Tour.objects.get_or_create(
                title=tour_data['title'],
                defaults={
                    'description': tour_data['description'],
                    'price': tour_data['price'],
                    'duration': tour_data['duration'],
                    'max_participants': tour_data['max_participants'],
                    'destination': destination,
                    'start_date': datetime.now().date() + timedelta(days=30),
                    'end_date': datetime.now().date() + timedelta(days=30 + tour_data['duration'])
                }
            )
            if created:
                print(f"Created tour: {tour.title}")
            else:
                print(f"Tour already exists: {tour.title}")
        except Destination.DoesNotExist:
            print(f"Destination {tour_data['destination']} not found")

if __name__ == '__main__':
    create_tours()
    print("Tours created successfully!")
