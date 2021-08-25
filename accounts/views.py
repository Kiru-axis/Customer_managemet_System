from django.shortcuts import render
from django.shortcuts import redirect
from .models import Tag,Customer,Product,Order
from .forms import OrderForms
# Create your views here.
# home view function
def dashboard(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    total_customers=customers.filter()
    total_orders=orders.count()
    delivered=orders.filter(status="Delivered").count()
    pending=orders.filter(status="Pending").count()
    context={
        "orders":Order.objects.all(),
        "customers":Customer.objects.all(),
        "total_orders":total_orders,
        "total_customers":total_customers,
        "delivered":delivered,
        "pending":pending,
    }
    return render (request, 'accounts/dashboard.html',context)

# products view function
def products(request):
    context={
        "products":Product.objects.all(),
    }
    return render (request, 'accounts/products.html',context)

def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    orders_count=orders.count()
    context={
        "customers": customer,
        "orders": orders,
        "orders_count": orders_count,
        "products":Product.objects.all(),

    }
    return render (request, 'accounts/customer.html',context)

# create order
def createOrder(request):
    form=OrderForms()
    if request.method =="POST":
        form=OrderForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context={
        "form":form
    }
    return render (request, 'accounts/order_form.html',context)

# update orders
def updateOrder(request,pk):
    form=OrderForms()
    order=Order.objects.get(id=pk)
    form=OrderForms(instance=order)
    if request.method == 'POST':
        form=OrderForms(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context={
        "form":form
    }
    return render (request, 'accounts/order_form.html',context)

# delete orders
def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method =="POST":
        order.delete()
        print(order)
        return redirect('dashboard')
    context={
        "order":order,
    }
    return render (request, 'accounts/delete_order.html',context)
