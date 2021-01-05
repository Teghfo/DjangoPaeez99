from order.models import Cart
from django.utils.deprecation import MiddlewareMixin


class CartMiddleware(MiddlewareMixin):
    def process_request(self, request, *args, **kwargs):
        assert hasattr(request, 'user'), "shalgham man bad az Auth middleweram"
        if request.user.is_authenticated:
            cart, status = Cart.objects.get_or_create(user=request.user)
            request.cart = cart

    def process_view(self, request, view_func, view_args, view_kwargs):
        pass

    # def process_response(self, request, response):
    #     print(response)

    def process_exception(self, request, exception):
        print('hellllllo')
        return None
