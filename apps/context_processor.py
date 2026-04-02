from apps.models import Category


def custom_context(request):
    return {
        'site_name': 'Falcon1',
        'categories': Category.objects.all()
    }
