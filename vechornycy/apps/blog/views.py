from django.shortcuts import HttpResponse, render

def main_page(request):
    return HttpResponse("You are currently visiting main page!")


