from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView

from .forms import UserForm
# Create your views here.
from .models import Item, Category, ShopUser
from django.contrib.auth.models import User


# from django.contrib.auth.models import User


class CategoryView(ListView):
    queryset = Category.objects.all()
    template_name = 'shop/category.html'


class ItemView(ListView):
    queryset = Item.objects.all()


class CreateUserForm(CreateView):
    model = User
    form_class = UserForm
    template_name = "shop/login.html"
    success_url = "shop/main.html"

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            uname, passwd = form.cleaned_data["username"], form.cleaned_data["password"]

            login_user = User.objects.all()

            print(uname, passwd)

            try:
                is_user = login_user.filter(username=uname, password=passwd).get()
            except ObjectDoesNotExist:
                is_user = None

            if not is_user:
                context = {
                    'form': UserForm(request.POST),
                    'error_message': "There isn't such user",
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
            'form': UserForm(request.POST),
            "user": None,
            "items": items,
            "categories": categories
        }
        return render(request, 'shop/login.html', context)


def main_page(request):
    items = ItemView()
    categories = CategoryView()

    try:
        user = User.objects.all().filter(username=request.POST.get("username", None)).get()
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
    try:
        category = all_categories.filter(name=category).get()
    except ObjectDoesNotExist:
        category = None
    context = {
        "username": request.POST.get("username", None),
        "all_categories": all_categories,
        "category": category,
        "items": ItemView.queryset
    }

    return render(request, 'shop/category.html', context)


class UpdateItem(UpdateView):
    model = Item
    fields = ["name", "price"]
    template_name = "shop/update.html"
    success_url = "/shop/"
