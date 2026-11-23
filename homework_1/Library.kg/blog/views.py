from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def about_me_view(request):
    if request.method == 'GET':
        return HttpResponse('I am Batman')

def favorite_authors_view(request):
    if request.method == 'GET':
        return HttpResponse('My favorite arthurs are John Ronald Reuel Tolkien and Ray Bradbury')

def show_date_time_view(request):
    if request.method == 'GET':
        local_now = timezone.localtime(timezone.now())
        date_D_M_Y_format = local_now.strftime('%d.%m.%Y')
        time_H_M_S_format = local_now.strftime('%H:%M:%S')
        return HttpResponse(f'Today is {date_D_M_Y_format} and the time is {time_H_M_S_format}')