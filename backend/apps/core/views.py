from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from apps.tours.models import Tour, TourCategory
from .models import Destination

def home(request):
    """Trang chủ"""
    featured_tours = Tour.objects.filter(is_featured=True, is_active=True)[:6]
    popular_destinations = Destination.objects.filter(is_active=True)[:6]
    tour_categories = TourCategory.objects.all()[:4]

    context = {
        'featured_tours': featured_tours,
        'popular_destinations': popular_destinations,
        'tour_categories': tour_categories,
    }
    return render(request, 'home.html', context)

def about(request):
    """Trang giới thiệu"""
    return render(request, 'about.html')

def contact(request):
    """Trang liên hệ"""
    return render(request, 'contact.html')

def destinations(request):
    """Danh sách tất cả điểm đến"""
    destinations_list = Destination.objects.filter(is_active=True).order_by('name')

    # Phân trang
    paginator = Paginator(destinations_list, 12)  # 12 điểm đến mỗi trang
    page_number = request.GET.get('page', 1)
    destinations_page = paginator.get_page(page_number)

    context = {
        'destinations': destinations_page,
    }
    return render(request, 'destinations.html', context)

def destination_detail(request, slug):
    """Chi tiết điểm đến"""
    destination = get_object_or_404(Destination, slug=slug, is_active=True)
    tours = Tour.objects.filter(destination=destination, is_active=True)[:6]

    context = {
        'destination': destination,
        'tours': tours,
    }
    return render(request, 'destination_detail.html', context)