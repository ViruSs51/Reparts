from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        'page': 'home',
        'category': [
            {
                'title': 'Колёса',
                'url_image': 'main/img/banner.svg',
                'url': 'catalog/wheel',
                'products': [
                    {
                        'title': 'Колёсо от БМВ',
                        'description': 'Данные колёса преднозначены для бмв и также они зимний',
                        'parameters': {
                            'radius': 10
                        },
                        'price': 100,
                        'country_valute': 'USD',
                        'url_image': 'main/img/banner.svg',
                        'url': 'catalog/wheel/2'
                    } for p in range(10)
                ]
            } for c in range(10)
        ]
    }

    return render(request, 'main/home.html', data)