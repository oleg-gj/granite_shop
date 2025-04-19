from django.shortcuts import render
from django.views import generic

from shop.models import GraniteProduct, Category


def index(request):
    """View function for the home page of the site."""
    num_categories = Category.objects.count()
    num_granite_products = GraniteProduct.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_categories": num_categories,
        "num_granite_products": num_granite_products,
        "num_visits": num_visits + 1,
    }

    return render(request, "shop/index.html", context=context)


class CategoryListView(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "shop/category_list.html"
    paginate_by = 5
