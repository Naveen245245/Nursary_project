from django.shortcuts import render, redirect

# Create your views here.
from .models import Nursary, Owner, Order, Bed
from .forms import NursaryForm, OrderForm
from .utils import convert_to_rows_cols


def home(request):
    return render(request, 'base.html')


def nursaryList(request):
    nursaryList = Nursary.objects.all()
    return render(request, 'n_app/index.html', {"nursaries": nursaryList})


def createNursary(request):
    if request.method == "POST":
        nursaryForm = NursaryForm(request.POST)
        if nursaryForm.is_valid():
            nursaryForm.save() 
            return redirect("nursary-list")
    nursaryForm = NursaryForm()

    return render(request, "n_app/createNursary.html", {"nursaryForm": nursaryForm})


def updateNursary(request, pk):
    nursary = Nursary.objects.get(id=pk)
    form = NursaryForm(instance=nursary)
    if request.method == 'POST':
        print("B4 form val")
        form = NursaryForm(request.POST, instance=nursary)
        if form.is_valid():
            print("inside form val")
            form.save()
            return redirect("/viewNursary/"+str(pk))
    return render(request, "n_app/updateNursary.html", {"nursary": form})


def delNursary(request, pk):
    # nursary = Nursary.objects.get(id=pk)
    # if request.method == "POST":
    #     nursary.delete()
    #     return redirect("/nursaries")
    # return render(request, "n_app/delNursary.html", {"nursary": nursary})
    nursary = Nursary.objects.get(id=pk)
    if request.method == 'POST':
        print("B4 del")
        nursary.delete()
        print("after del")
        return redirect("/nursaries")

    return render(request, "n_app/delNursary.html", {"nursary": nursary})


# def confirmDelNursary(request):
#     return render(request, "n_app/confirmDelNursary.html")


def viewNursary(request, pk):
    # print("*****************************************************")
    # print(dir(request))
    nursary = Nursary.objects.get(id=pk)
    orders = Order.objects.filter(nursary_p=nursary)
    beds = Bed.objects.filter(nursary=nursary)
    bed_list = convert_to_rows_cols(beds, nursary.rows, nursary.columns)
    # Publisher.objects.filter(book__title__startswith='hello')
    context = {"nursary": nursary,
               "orders": orders,
               "beds": beds,
               "bed_list": bed_list}
    return render(request, "n_app/nursary-view.html", context)


def bedView(request, pk):
    bed = Bed.objects.get(pk=pk)
    return render(request, "n_app/bed_view.html", {"bed": bed})


def createOrder(request, pk):
    if request.method == "POST":
        print("B4 add order form val----")
        print(request.get_raw_uri)
        orderform = OrderForm(request.POST)
        if orderform.is_valid():
            print("--------B4 save add order form inside val")
            orderform.save()
            print("After save add order form inside val")
            return redirect("../")
    orderform = OrderForm
    return render(request, "n_app/create_oder.html", {"orderform": orderform})


def updateOrder(request, pk,):
    order = Order.objects.get(id=pk)
    nursary = order.nursary_p.id
    url = "/viewNursary/"+str(nursary)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        print("B4 form val")
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            print("inside form val")
            form.save()
            return redirect(url)
    return render(request, "n_app/updateNursary.html", {"nursary": form})


def delOrder(request, pk):
    order = Order.objects.get(id=pk)
    nursary = order.nursary_p.id
    # orders = Order.objects.filter(nursary_p=nursary)
    url = "/viewNursary/"+str(nursary)
    print(url)
    if request.method == "POST":
        order.delete()
        return redirect(url)
    return render(request, "n_app/delOrder.html", {"order": order})
