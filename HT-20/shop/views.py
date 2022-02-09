from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from .models import ShopUser, Item, Category
from .forms import UserForm, ItemForm
from django.views.generic import CreateView, ListView

from django.contrib import admin


class CategoryView(ListView):
    queryset = Category.objects.all()
    template_name = 'shop/category.html'


class ItemView(ListView):
    queryset = Item.objects.all()


class CreateUserForm(CreateView):
    model = ShopUser
    form_class = UserForm
    template_name = "shop/login.html"
    success_url = "shop/main.html"

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():

            uname, passwd = form.cleaned_data["username"], form.cleaned_data["password"]

            login_user = ShopUser.objects.all()


            try:
                is_user = login_user.filter(username=uname, password=passwd).get()
            except ObjectDoesNotExist:
                is_user = None

            if not is_user:
                context = {
                    'form': UserForm(request.POST),
                    'error_message': "There isnt such user",
                }
                return render(request, 'shop/login.html', context)

            else:
                items = ItemView.queryset
                categories = CategoryView.queryset
                context = {
                    "user": is_user,
                    "items": items,
                    "categories": categories
                }
                return render(request, 'shop/main.html', context)

        items = ItemView.queryset
        categories = CategoryView.queryset

        context = {
            "user":None,
            "items": items,
            "categories": categories
        }
        return render(request, 'shop/login.html', context)


def main_page(request):
    items = ItemView()
    categories = CategoryView()

    try :
        user = ShopUser.objects.all().filter(username=request.POST.get("username", None)).get()
    except ObjectDoesNotExist:
        user = None
    context = {
        "user": user,
        "items": items.queryset,
        "categories": categories.queryset
    }

    return render(request, 'shop/main.html', context)


def category(request, category):
    all_categories = Category.objects.all()
    category = all_categories.filter(name=category).get()

    context = {
        "category": category,
        "items": ItemView.queryset
    }
    return render(request, 'shop/category.html', context)


def edit(request):
    return redirect('/admin/shop/item/')