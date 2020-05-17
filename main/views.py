from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Write
from datetime import datetime
def write(request):
	now = datetime.now()
	time = now.strftime("%H:%M:%S")
	time_writed = time
	text_to_write = request.POST['write']
	obj = Write(text=text_to_write)
	obj.save()
	return HttpResponseRedirect('/',
						 {'time': time})
# Create your views here.
def main(request):
	
	all_objects = Write.objects.all()
	return render(request,'main.html',
					  {'objs': all_objects,
					  }
				  )

def delete(request, get_id):
	item = Write.objects.get(id=get_id)
	item.delete()
	return HttpResponseRedirect('/')