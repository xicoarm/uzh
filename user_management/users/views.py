#users/views.py

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def dashboard(request):
    return render(request, "users/dashboard.html")

@csrf_exempt
def start_charging(request):

    #start script to turn on the Switch
    from users.scripts import switch
    a = switch.switch("user.username")

    #script_response = switch.py --chdir /users/scripts

    #start the script to periodically check the meter values

    #if charging started
    return render(request, "users/index.html")

    #if charging could not be started
    # return render(request, "users/not_charging.html")

@csrf_exempt
def stats(request):

    #if still charging 
    return redirect(start_charging)

    #else charging finished
    # return render(request, "users/stats.html")    