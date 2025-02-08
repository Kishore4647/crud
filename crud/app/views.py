from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.shortcuts import render, redirect
from .models import Receipe  # Assuming &quot;Receipe&quot; is the correct model name
from django.http import HttpResponse
from .forms import OrderForm

def receipes(request):
    if request.method == 'POST':
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
        )
        return redirect('/receipes')

    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            receipe_name__icontains=request.GET.get('search'))

    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes')


def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes')

    context = {'receipe': queryset}
    return render(request, 'update_receipe.html', context)


def home(request):
    queryset = Receipe.objects.all()

    context = {'items':queryset}

    return render(request,'home.html',context)


def food_order(request,id):
    # Example food items (you can customize this with dynamic data from your database)
    food_items = Receipe.objects.get(id=id)

    # Total price calculation
    total_price = food_items.receipe_description

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['user_name']
            address = form.cleaned_data['address']
            quantity = form.cleaned_data['quantity']

            total_price=int(total_price)*quantity

            # Here you would save the order to the database
            # For example: Order.objects.create(address=address, total_price=total_price, ...)

            # Display a confirmation message with order details
            return render(request, 'order_confirmation.html', {
                'name':name,
                'address': address,
                'food_items': food_items,
                'quantity':quantity,
                'receipe_name': food_items.receipe_name,
                'price': food_items.receipe_description,
                'total_price': total_price,
                
            })
    else:
        form = OrderForm()

    return render(request, 'food_order.html', {
        'food_items': [food_items],
        'total_price': total_price,
        'receipe_description': food_items.receipe_description,
        'receipe_name': food_items.receipe_name,
        'form': form,
    })
