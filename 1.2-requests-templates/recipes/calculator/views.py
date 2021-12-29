from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def home_view(request):
    template_name = 'calculator/home.html'
    pages = {'Рецепт омлета': reverse('omlet'),
             'Рецепт пасты': reverse('pasta'),
             'Рецепт бутера': reverse('buter')}

    context = {'pages': pages}
    return render(request, template_name, context)


def recipe_view(request):
    servings = int(request.GET.get('servings', 1))
    recipe_name = request.resolver_match.url_name
    recipe = {ingredient: round(amount * servings, 2) for ingredient, amount in DATA[recipe_name].items()}
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)
