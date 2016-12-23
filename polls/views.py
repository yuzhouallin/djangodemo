from django.http import HttpResponse
from models import Poll

def index(request):
	poll = Poll.objects.create(
		name="Adam Buzz",
		choice="Trump",
	)
	poll.save()
	return HttpResponse("Hello, world. You're at the polls index. New poll saved.")
