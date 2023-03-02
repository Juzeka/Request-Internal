from django.shortcuts import render
from django.http import JsonResponse
import requests


def request_internal(request):
    response = requests.get('https://viacep.com.br/ws/64007200/json/')

    return JsonResponse(response.json(), safe=False)