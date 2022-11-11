from django.shortcuts import HttpResponse,render
from .forms import TodoForm
from .models  import TodoModel
# Create your views here.
def index(request):
    return render(request,"test.html")
def alltasks(request):
    data = TodoModel.objects.all().order_by('id').reverse()
    return render(request,"alltasks.html",{"tasks":data})

def form(request):
    if request.POST:
        newtask=TodoForm(request.POST)
        if newtask.is_valid():
            newtask.save(commit=False)
            newtask.save()
            return HttpResponse("Saved")
        return HttpResponse("Not Saved")

    #initial = {"task": "MyTask", "description": "Des", "status": 100,"dateoftask":"11-11-2022"}
    return render(request, "form.html", {"form": TodoForm()})
    #return render(request, "todoentry.html")


    #return HttpResponse("Todo apps")

