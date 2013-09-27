from django.http import HttpResponse
from drills.models import Day

def home(request):
    day_list = Day.objects.order_by('-exercise_type')[:5]
    output = ', '.join([p.exercise_type for p in day_list])
    return HttpResponse(output)
