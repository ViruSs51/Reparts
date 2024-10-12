from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        'category': [
            {
                'title': 'Колёса',
                'description': 'Список колёс для разных машин',
                'url_image': 'main/img/banner.svg',
                'url': 'catalog/wheel/2'
            },
            {
                'title': 'Колёса',
                'description': 'Список колёс для разных машин',
                'url_image': 'main/img/banner.svg',
                'url': 'catalog/wheel/2'
            },
            {
                'title': 'Колёса',
                'description': 'Список колёс для разных машин',
                'url_image': 'main/img/banner.svg',
                'url': 'catalog/wheel/2'
            },
            {
                'title': 'Колёса',
                'description': 'Список колёс для разных машин',
                'url_image': 'main/img/banner.svg',
                'url': 'catalog/wheel/2'
            },
            {
                'title': 'Колёса',
                'description': 'Список колёс для разных машин',
                'url_image': 'main/img/banner.svg',
                'url': 'catalog/wheel/2'
            },
            {
                'title': 'Колёса',
                'description': 'Список колёс для разных машин',
                'url_image': 'main/img/banner.svg',
                'url': 'catalog/wheel/2'
            },
            {
                'title': 'Колёса',
                'description': 'Список колёс для разных машин',
                'url_image': 'main/img/banner.svg',
                'url': 'catalog/wheel/2'
            },
            {
                'title': 'Колёса',
                'description': 'Список колёс для разных машин',
                'url_image': 'main/img/banner.svg',
                'url': 'catalog/wheel/2'
            }
        ]
    }

    return render(request, 'main/home.html', data)