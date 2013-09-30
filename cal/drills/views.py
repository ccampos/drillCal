from django.http import HttpResponse
from drills.models import Day

def home(request):
    day_list = Day.objects.order_by('-exert_percent')[:5]
    output = ', '.join([str(p.exert_percent) for p in day_list])
    return HttpResponse(output)
