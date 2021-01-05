from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, Http404, HttpResponse
from django.db.models import Prefetch

from .models import Cart, CartItems
from restaurant.models import Food


@login_required(login_url='login', redirect_field_name='next')
def show_cart(request):
    cart, status = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItems.objects.filter(cart=cart)

    context = {
        'cart_item': cart_item,
    }

    return render(request, 'show_cart.html', context)


@login_required(login_url='login', redirect_field_name='next')
def add_cart(request, food_id):
    if request.method == "POST":
        cart = request.cart

        cart_items = Cart.objects.prefetch_related(Prefetch(
            'food', queryset=CartItems.objects.select_related('food'))).get(user=request.user)

        try:
            cart_item = cart_items.food.get(food_id=food_id)
            cart_item.qty += 1
            cart_item.save()
        except:
            CartItems.objects.create(food_id=food_id, cart=cart, qty=1)

        return redirect(request.GET.get('next', 'show_cart'))
    return HttpResponseNotAllowed("shab bekheir ba anke gtfe budi sobh bekheir")


@login_required(login_url='login', redirect_field_name='next')
def delete_from_cart(request, food_id):
    if request.method == "POST":
        cart = request.cart
        cart_items = Cart.objects.prefetch_related(Prefetch(
            'food', queryset=CartItems.objects.select_related('food'))).get(user=request.user)

        try:
            cart_item = cart_items.food.get(food_id=food_id)
            cart_item.delete()
        except:
            return Http404()

        return redirect(request.GET.get('next', 'show_cart'))
    return HttpResponseNotAllowed("shab bekheir ba anke gtfe budi sobh bekheir")


@login_required(login_url='login', redirect_field_name='next')
def decrement_cart(request, food_id):
    if request.method == "POST":
        cart = request.cart
        cart_items = Cart.objects.prefetch_related(Prefetch(
            'food', queryset=CartItems.objects.select_related('food'))).get(user=request.user)

        try:
            cart_item = cart_items.food.get(food_id=food_id)
            if cart_item.qty > 1:
                cart_item.qty -= 1
                cart_item.save()
            else:
                cart_item.delete()
        except:
            return Http404()

        return redirect(request.GET.get('next', 'show_cart'))
    return HttpResponseNotAllowed("shab bekheir ba anke gtfe budi sobh bekheir")


def add_cart_anounymous(request):

    if request.session.get('cart', ''):
        print(request.session['cart'])
        return HttpResponse("porteghal forush")

    request.session['cart'] = {
        "porteghal": 3
    }
    return HttpResponse("porteghal andakhtam tu sabad")
