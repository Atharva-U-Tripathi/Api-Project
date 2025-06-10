from django.shortcuts import render
import math
import requests
# Create your views here.

# def indexpage(request):
#     response = requests.get("https://dummyjson.com/recipes").json()
#     tagres = requests.get("https://dummyjson.com/recipes/tags").json()
#     context = {
#         "data":response["recipes"],
#         "tags":tagres
#     }
#     return render(request, 'index.html', context)

def indexpage(request):
    page = int(request.GET.get("page", 1))  # Default to page 1
    limit = 12
    skip = (page - 1) * limit

    api_url = f"https://dummyjson.com/recipes?limit={limit}&skip={skip}"
    response = requests.get(api_url).json()
    tagres = requests.get("https://dummyjson.com/recipes/tags").json()

    total = response["total"]
    total_pages = math.ceil(total / limit)
    page_range = list(range(1, total_pages + 1))

    context = {
        "data": response["recipes"],
        "tags": tagres,
        "total": total,
        "limit": limit,
        "current_page": page,
        "page_range": page_range
    }
    return render(request, 'index.html', context)

def recipiespage(request,id):
    response = requests.get(f"https://dummyjson.com/recipes/{id}").json()
    context={
        "data":response
    }
    return render(request, 'receipes.html', context)

def mealtype(request, meal):
    response = requests.get(f"https://dummyjson.com/recipes/meal-type/{meal}").json()
    tagres = requests.get("https://dummyjson.com/recipes/tags").json()
    context = {
        "data": response["recipes"],
        "tags": tagres
    }
    return render(request, 'index.html', context)

def databytags(request, tag):
    response = requests.get(f"https://dummyjson.com/recipes/tag/{tag}").json()
    tagres = requests.get("https://dummyjson.com/recipes/tags").json()
    print(response)
    context={
        "data":response["recipes"],
        "tags":tagres
    }
    return render(request, 'index.html', context)

def search(request):

    query = request.POST.get("query")
    responce = requests.get(f"https://dummyjson.com/recipes/search?q={query}").json()
    tagres = requests.get('https://dummyjson.com/recipes/tags').json()

    context = {
        "data": responce["recipes"],
        "tags": tagres
    }

    return render(request, 'index.html', context)