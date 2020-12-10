from django.utils.text import slugify

from restaurant.models import Element


def run(*args):
    elemets = Element.objects.all()

    for e in elemets:
        if not e.slug:
            e.slug = slugify(e.name, allow_unicode=True)
            e.save()
