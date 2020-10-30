from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Mall, Store, Comment, Costumer


@csrf_exempt
def show_mall(request):
    if request.method == 'GET':
        malls = Mall.objects.all()

        malls_data = []

        for item in malls:
            temp_data = {
                'name': item.name,
                'address': item.address
            }
            malls_data.append(temp_data)
        return JsonResponse(malls_data, safe=False)

    return JsonResponse({"status": "just get method"})


@csrf_exempt
def comment(request, store_id):
    if request.method == 'GET':
        store_obj = Store.objects.get(id=store_id)
        comment = Comment.objects.filter(store=store_obj)

        comment_data = []

        for item in comment:
            temp_data = {
                'costumer': item.costumer.username,
                'comment': item.comment
            }
            comment_data.append(temp_data)
        return JsonResponse(comment_data, safe=False)

    if request.method == 'POST':
        store_obj = Store.objects.get(id=store_id)
        data = request.body
        data_dic = json.loads(data)
        costumer_username = data_dic['username']
        comment_data = data_dic['comment']
        try:
            costumer_obj = Costumer.objects.get(username=costumer_username)
            Comment.objects.create(costumer=costumer_obj,
                                   store=store_obj, comment=comment_data)
        except:
            raise ValueError("chenin useri nadarim")
        return JsonResponse({"s": "a"})
