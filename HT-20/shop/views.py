from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
# Create your views here.
from .models import Item, Category, ShopUser
from django.contrib.auth.models import User


# from django.contrib.auth.models import User



def loginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('/shop/')
    else:
        # Return an 'invalid login' error message.
        context = {
            "form": UserForm(request.POST),
            'error_message': "There isn't such user",
        }
        return render(request, "shop/login.html", context)


def logoutView(request):
    logout(request)
    return redirect("/shop/login/")


class CreateUserForm(CreateView):
    model = User
    form_class = UserForm
    template_name = "shop/login.html"
    success_url = "shop/"

    def post(self, request):
        form = UserForm(request.POST)
        return loginView(request)


def main_page(request):
    items = Item.objects.all()
    categories = Category.objects.all()

    context = {
        "user": request.user,
        "items": items,
        "categories": categories,
    }
    return render(request, 'shop/main.html', context)


def category(request, category):
    all_categories = Category.objects.all()
    try:
        category = all_categories.filter(name=category).get()
    except ObjectDoesNotExist:
        category = None
    context = {
        "username": request.POST.get("username"),
        "all_categories": all_categories,
        "category": category,
        "items": Item.objects.all()
    }

    return render(request, 'shop/category.html', context)


class UpdateItem(UpdateView):
    model = Item
    fields = ["name", "price"]
    template_name = "shop/update.html"
    success_url = "/shop/"

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect("shop/login")
        item = Item.objects.all().filter(pk=pk).get()
        print(item.name, item.price, request.POST['name'])
        item.name = request.POST['name']
        item.price = request.POST['price']
        item.save()
        return main_page(request)
