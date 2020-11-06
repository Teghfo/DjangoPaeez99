from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

import json

from .models import Mall, Store, Comment, Costumer


@csrf_exempt
def show_mall(request):
    if request.method == 'GET':
        # url query params   http://localhost:8000/show_mall?channel=fs&client=ubuntu&q=mapsa
        search = request.GET.get('q', None)
        if not search:
            malls = Mall.objects.all()
        else:
            malls = Mall.objects.filter(name__contains=search)
        malls_data = []

        for item in malls:
            temp_data = {
                'name': item.name,
                'address': item.address
            }
            malls_data.append(temp_data)
        return JsonResponse(malls_data, safe=False)

    return JsonResponse({"status": "just get method"})


# Customer CRUD service

@csrf_exempt
def customer_create(request):
    if request.method == 'POST':
        data_body = request.body
        data = json.loads(data_body)
        try:
            username = data('username', None)
            user_obj = Costume(username=username)
            user_obj.save()
            # Costumer.objects.create(username=username)
        except Exception as e:
            return JsonResponse({'status': str(e)})

        return JsonResponse({'status': f'user {user_obj.username} ba khoshi ijad shod'})
    return JsonResponse({'status': 'bad request!'})


@csrf_exempt
def customer_edit(request, username):
    # if request.method == 'PUT' or request.method == 'PATCH':
    #     data_body = request.body
    #     data = json.loads(data_body)
    #     try:
    #         username = data.get('username', None)
    #         if username:
    #             user_obj = get_object_or_404(Costumer, username=username)
    #             new_username = data.get('newuser', None)
    #             if new_username:
    #                 user_obj.username = new_username
    #                 user_obj.save()
    #                 return JsonResponse({'status': 'esmet avaz shod azizam'})
    #             else:
    #                 return JsonResponse({'status': 'new username required'})
    #         else:
    #             return JsonResponse({'status': 'username required'})
    #     except Exception as e:
    #         return JsonResponse({'status': str(e)})
    # return JsonResponse({'status': 'bad request!'})
    if request.method == 'PUT' or request.method == 'PATCH':
        user_obj = get_object_or_404(Costumer, username=username)
        esm_shab = json.loads(request.body).get('esm_shab', None)
        if esm_shab == user_obj.esm_shab:
            new_user = json.loads(request.body).get('newuser', None)
            if new_user:
                user_obj.username = new_user
                user_obj.save()
                return JsonResponse({'status': 'esmet avaz shod azizam'})
            else:
                return JsonResponse({'status': 'new username required'})
        else:
            return JsonResponse({'status': 'bache zerang. esm shab nemiduni'})
    return JsonResponse({'status': 'bad request!'})


@csrf_exempt
def customer_delete(request, username):
    if request.method == 'DELETE':
        user_obj = get_object_or_404(Costumer, username=username)
        esm_shab = json.loads(request.body).get('esm_shab', None)
        if esm_shab == user_obj.esm_shab:
            user_obj.delete()
            return JsonResponse({'status': 'khodahafez hamin hala!'})
        else:
            return JsonResponse({'status': 'bache zerang. esm shab nemiduni'})
    return JsonResponse({'status': 'bad request!'})


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
