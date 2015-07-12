from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geoip import GeoIP

from .models import Thing
from . import GeocodeService

def index(request):
    latitude, longitude = GeocodeService.get_lat_lon(get_client_ip(request))
    things = Thing.objects.all().order_by('-creation_time')[:100]

    return render(request, 'map/index.html', {
        'center_lat': latitude,
        'center_lon': longitude,
        'things': things,
    })

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_exempt
@require_POST
def thing(request):
    lat = request.POST['latitude']
    lon = request.POST['longitude']
    description = request.POST['description']
    thing = Thing(description=description, latitude=lat, longitude=lon)
    thing.save()
    return JsonResponse({'success': True,
        'latitude': lat,
        'longitude': lon,
        'description': description,
    })
