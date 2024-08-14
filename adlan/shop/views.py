from datetime import datetime

from django.shortcuts import render

def main_index(request):
    return render(request,'shop/main.html',context)
