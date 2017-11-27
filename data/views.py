import random

from django.http import JsonResponse
from django.shortcuts import render, redirect

from data.models import Data

"""

Content-Type : application/vnd.onem2m-ntfy+xml
Content-Params : {'charset': 'UTF-8'}
User-Agent : Jakarta Commons-HttpClient/3.0.1
Host : 61.250.21.53
Port : 80
Path : /t/
BODY : <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <m2m:cin xmlns:m2m="http://www.onem2m.org/xml/protocols" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <ty>4</ty>
            <ri>CI00000000000084002029</ri>
            <rn>CI00000000000084002029</rn>
            <pi>CT00000000000000006180</pi>
            <ct>2017-06-27T16:08:45+09:00</ct>
            <lt>2017-06-27T16:08:45+09:00</lt>
            <sr>/0000000000000004/v1_0/remoteCSE-00000004702c1ffffe1d8d33/container-LoRa//subscription-test</sr>
            <et>2017-06-28T16:08:45+09:00</et>
            <st>28</st>
            <cr>RC00000000000000383292</cr>
            <cnf>LoRa/Sensor</cnf>
            <cs>6</cs>
            <con>616263</con>
        </m2m:cin>

"""


def make_random_data():
    new_data = Data()
    new_data.dust25 = random.randint(5, 200)
    new_data.dust100 = random.randint(5, 20)
    new_data.discomfort_index = random.randint(20, 60)
    new_data.co2 = random.randint(400, 1200)
    new_data.temp = random.randint(180, 230) / 10
    new_data.humid = random.randint(40, 50)
    new_data.device_id = str(random.randint(100000, 999999)) + "-" \
                         + str(random.randint(100000, 999999)) + "-" + \
                         str(random.randint(100000, 999999))
    new_data.save()


def view_all(request):
    all_data = Data.objects.all().order_by("-created_at")[:30]
    return render(request, "view.html", {"datas": all_data})


def add(request):
    make_random_data()
    return redirect('view_all')


def latest(request):
    data = Data.objects.all().order_by("-created_at").first()
    return JsonResponse({"pk": data.pk, "dust25": data.dust25, "dust100": data.dust100, "co2": data.co2,
                         "temp": data.temp, "humid": data.humid,
                         "created_at": data.created_at.astimezone().strftime("%Y.%m.%d %H:%M:%S"),
                         "discomfort_index": data.discomfort_index})

def test(request):
    data = Data.objects.first()
    json_output = dict()
    json_output["test"] = data.pk
    return JsonResponse(json_output)