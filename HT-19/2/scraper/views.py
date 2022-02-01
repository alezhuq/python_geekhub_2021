from time import sleep

import requests

from django.shortcuts import render
from .models import Choice, Ask, Show, New, Job
from .forms import MyChoiceForm
# Create your views here.
from django.views.generic import CreateView


class CreateMyChoiceView(CreateView):
    model = Choice
    form_class = MyChoiceForm
    template_name = 'scraper/index.html'
    success_url = 'scraper/success.html'

    def post(self, request):

        form = MyChoiceForm(request.POST)

        if form.is_valid():

            user_category = form.cleaned_data['name']

            id_list = parse_ids(user_category)
            get_items(user_category, id_list)


            # MY CODE HERE

            context = {
                'form': MyChoiceForm(),
                # other context
            }
            return render(request, self.success_url, context)

        # if there were errors in form
        # we have to display same page with errors
        context = {
            'form': form,
            # other context
        }
        return render(request, "scraper/index.html", context)


def parse_ids(category):
    base_url = "https://hacker-news.firebaseio.com/v0/"
    data_format = ".json"
    if category:
        try:
            request = requests.get(base_url + category + data_format)
            request.raise_for_status()
            sleep(0.5)
        except Exception as e:
            print("there was a problem with getting info from your page", e)
            return
    else:
        return

    return request.json()

def get_items(category, id_list):

    data_format = ".json"
    temp_url = "https://hacker-news.firebaseio.com/v0/" + "item/"

    for element in id_list:
        try:
            request = requests.get(temp_url + str(element) + data_format)
            request.raise_for_status()

        except Exception as e:
            print("there was a problem with getting info from your page", e)
            return
        temp_item = request.json()
        if category == "askstories":
            if Ask.objects.filter(item_id = int(temp_item.get("id", "None"))).exists():
                print("already in db")
                continue
            object_to_write = Ask(
                by=temp_item.get("by", "None"),
                descendants=temp_item.get("descendants", "None"),
                item_id=temp_item.get("id", "None"),
                kids=temp_item.get("kids", "None"),
                score=temp_item.get("score", "None"),
                text=temp_item.get("text", "None"),
                time=temp_item.get("time", "None"),
                title=temp_item.get("title", "None"),
                item_type=temp_item.get("type", "None")
            )
        elif category == "showsotires":
            if Show.objects.filter(item_id = int(temp_item.get("id", "None"))).exists():
                print("already in db")
                continue
            object_to_write = Show(
                by=temp_item.get("by", "None"),
                descendants=temp_item.get("descendants", "None"),
                item_id=temp_item.get("id", "None"),
                kids=temp_item.get("kids", "None"),
                score=temp_item.get("score", "None"),
                url=temp_item.get("url", "None"),
                time=temp_item.get("time", "None"),
                title=temp_item.get("title", "None"),
                item_type=temp_item.get("type", "None")
            )
        elif category == "jobstories":
            if Job.objects.filter(item_id = int(temp_item.get("id", "None"))).exists():
                print("already in db")
                continue
            object_to_write = Job(
                by=temp_item.get("by", "None"),
                item_id=temp_item.get("id", "None"),
                score=temp_item.get("score", "None"),
                url=temp_item.get("url", "None"),
                time=temp_item.get("time", "None"),
                title=temp_item.get("title", "None"),
                item_type=temp_item.get("type", "None")
            )
        else:
            if New.objects.filter(item_id = int(temp_item.get("id", "None"))).exists():
                print("already in db")
                continue
            object_to_write = New(
                by=temp_item.get("by", "None"),
                descendants=temp_item.get("descendants", "None"),
                item_id=temp_item.get("id", "None"),
                kids=temp_item.get("kids", "None"),
                score=temp_item.get("score", "None"),
                url=temp_item.get("url", "None"),
                time=temp_item.get("time", "None"),
                title=temp_item.get("title", "None"),
                item_type=temp_item.get("type", "None"),
                text=temp_item.get("text", "None")
            )

        print("current item : ", temp_item)
        object_to_write.save()

