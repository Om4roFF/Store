from django.http import Http404
from django.shortcuts import render

from main.models import Car


def index(request):
    cars_list = Car.objects.order_by('engine_volume')
    return render(request,'main/index.html', {'cars_list': cars_list})


def car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except:
        raise Http404("Статья не найдена")

    images = car.images.order_by('id')
    return render(request, 'main/car.html', {'car': car, 'images': images})


def search(request):
    count = 0
    if request.method == 'POST':
        search_by_fuel = str(request.POST['fuel'])
        search_by_body = str(request.POST['body_car'])
        search_by_unit = str(request.POST['unit'])
        print("------------------------------------------------------------------------" + search_by_fuel)
        if search_by_fuel == 'none1' and search_by_unit == 'none1':
            my_car = Car.objects.filter(body=search_by_body).order_by('id')
            return render(request, 'main/searched.html', {'my_car': my_car})

        if search_by_fuel == 'none1' and search_by_body == 'none1':
            my_car_unit = Car.objects.filter(drive_unit=search_by_unit).order_by('id')
            return render(request, 'main/searched.html', {'my_car': my_car_unit})

        if search_by_unit == 'none1' and search_by_body == 'none1':
            my_car_fuel = Car.objects.filter(fuel=search_by_fuel).order_by('id')
            return render(request, 'main/searched.html', {'my_car': my_car_fuel})

        if search_by_fuel == 'none1':
            my_car_unit = Car.objects.filter(drive_unit=search_by_unit).order_by('id')
            my_car = Car.objects.filter(body=search_by_body).order_by('id')
            return render(request, 'main/searched.html', {'my_car': my_car,'my_car_unit':my_car_unit})

        if search_by_unit == 'none1':
            my_car_fuel = Car.objects.filter(fuel=search_by_unit).order_by('id')
            my_car = Car.objects.filter(body=search_by_body).order_by('id')
            return render(request, 'main/searched.html', {'my_car': my_car, 'my_car_fuel': my_car_fuel})

        if search_by_body == 'none1':
            my_car_fuel = Car.objects.filter(fuel=search_by_unit).order_by('id')
            my_car_unit = Car.objects.filter(drive_unit=search_by_unit).order_by('id')
            return render(request, 'main/searched.html', {'my_car_fuel': my_car_fuel,'my_car_unit':my_car_unit})

        if search_by_fuel != 'none1' and search_by_unit != 'none1' and search_by_fuel != 'none1':
            my_car = Car.objects.filter(body=search_by_body).order_by('id')
            my_car_fuel = Car.objects.filter(fuel=search_by_unit).order_by('id')
            my_car_unit = Car.objects.filter(drive_unit=search_by_unit).order_by('id')
            arr = []
            for i in Car.objects.all():
                if my_car.filter(id=i.id):
                    count += 1
                if my_car_unit.filter(id=i.id):
                    count += 1
                if my_car_fuel.filter(id=i.id):
                    count += 1
                if count == 3:
                    arr.append(i)
                count = 0

            return render(request, 'main/searched.html', {'my_car': arr})

        if search_by_fuel == 'none1' and search_by_unit == 'none1' and search_by_fuel == 'none1':
            print("------------------------------------------------------------------------"+search_by_fuel)
            cars_list = Car.objects.order_by('engine_volume')
            return render(request, 'main/index.html', {'searched_list': cars_list})
