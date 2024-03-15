from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reminder
import json

@csrf_exempt
def create_reminder(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            date = data.get('date')
            time = data.get('time')
            message = data.get('message')
            reminder_method = data.get('reminder_method')

            reminder = Reminder.objects.create(date=date, time=time, message=message, reminder_method=reminder_method)
            reminder.save()

            return JsonResponse({'status': 'Reminder saved successfully'})
        except Exception as e:
            return JsonResponse({'status': 'Error occurred', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'Only POST requests are allowed'}, status=405)
