from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, Http404

from .models import Cart, CartItems
from restaurant.models import Food


@login_required(login_url='login', redirect_field_name='next')
def show_cart(request):
    cart, status = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItems.objects.filter(cart=cart)

    context = {
        'cart_item': cart_item
    }

    return render(request, 'show_cart.html', context)


@login_required(login_url='login', redirect_field_name='next')
def add_cart(request, food_id):
    print("in add cart")
    if request.method == "POST":
        cart = request.cart
        # cart, status = Cart.objects.get_or_create(user=request.user)
        # if status:
        #     CartItems.objects.create(food_id=food_id, cart=cart, qty=1)
        #     return redirect('show_cart')
        food = get_object_or_404(Food, id=food_id)

        if food in cart.food.all():
            cart_item = CartItems.objects.get(food=food, cart=cart)
            cart_item.qty += 1
            cart_item.save()
        else:
            CartItems.objects.create(food_id=food_id, cart=cart, qty=1)

        return redirect(request.GET.get('next', 'show_cart'))
    return HttpResponseNotAllowed("shab bekheir ba anke gtfe budi sobh bekheir")


@login_required(login_url='login', redirect_field_name='next')
def delete_from_cart(request, food_id):
    if request.method == "POST":
        cart = request.cart
        # cart, status = Cart.objects.get_or_create(user=request.user)
        # if status:
        #     CartItems.objects.create(food_id=food_id, cart=cart, qty=1)
        #     return redirect('show_cart')
        food = get_object_or_404(Food, id=food_id)

        if food in cart.food.all():
            cart_item = CartItems.objects.get(food=food, cart=cart)
            cart_item.delete()
        else:
            return Http404()

        return redirect(request.GET.get('next', 'show_cart'))
    return HttpResponseNotAllowed("shab bekheir ba anke gtfe budi sobh bekheir")


@login_required(login_url='login', redirect_field_name='next')
def decrement_cart(request, food_id):
    if request.method == "POST":
        cart = request.cart
        # cart, status = Cart.objects.get_or_create(user=request.user)
        # if status:
        #     CartItems.objects.create(food_id=food_id, cart=cart, qty=1)
        #     return redirect('show_cart')
        food = get_object_or_404(Food, id=food_id)

        if food in cart.food.all():
            cart_item = CartItems.objects.get(food=food, cart=cart)
            if cart_item.qty > 1:
                cart_item.qty -= 1
                cart_item.save()
            else:
                cart_item.delete()
        else:
            return Http404()

        return redirect(request.GET.get('next', 'show_cart'))
    return HttpResponseNotAllowed("shab bekheir ba anke gtfe budi sobh bekheir")
