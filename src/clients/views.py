# Django
from django.shortcuts import render, redirect, HttpResponse

# Models
from clients.models import Clients, Products

# Forms
from clients.forms import FormClient, FormClientCreate, FormProduct


def home(request):
    context = {'db_table_list': ['Clients', 'Products']}
    return render(request, template_name='home.html', context=context)


def list_clients(request):
    clients_list = Clients.objects.all()
    form_client = FormClient
    context = {'clients_list': clients_list, 'form': form_client}

    return render(request, template_name='clients.html', context=context)


def add_client(request):
    if request.method == 'POST':
        client_form = FormClientCreate(request.POST)

        if client_form.is_valid():
            data_form = client_form.cleaned_data
            first_name = data_form['first_name']
            last_name = data_form['last_name']
            identification = data_form['identification']

            client = Clients(
                first_name=first_name,
                last_name=last_name,
                identification=identification,
            )
            client.save()

            return redirect('clients')

        else:
            form = client_form
            clients_list = Clients.objects.all()
            return render(request=request, template_name='clients.html',
                          context={
                              'form': form,
                              'clients_list': clients_list,
                          })
    else:
        return HttpResponse('Error: this method is not allowed')


def delete_client(request):
    if request.method == 'POST':
        client_id = request.POST.get('delete_button')
        client = Clients.objects.get(pk=client_id)
        client.delete()
    return redirect('clients')


def list_products(request):
    products_list = Products.objects.all()
    form_product = FormProduct
    context = {'products_list': products_list, 'form': form_product}
    return render(request, template_name='products.html', context=context)


def add_product(request):
    if request.method == 'POST':
        product_form = FormProduct(request.POST)

        if product_form.is_valid():
            data_form = product_form.cleaned_data
            name = data_form['name']
            price = data_form['price']

            product = Products(
                name=name,
                price=price,
            )
            product.save()

            return redirect('products')

        else:
            form = product_form
            product_list = Products.objects.all()
            return render(request=request, template_name='products.html',
                          context={
                              'form': form,
                              'product_list': product_list,
                          })
    else:
        return HttpResponse('Error: this method is not allowed')


def delete_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('delete_button')
        product = Products.objects.get(pk=product_id)
        product.delete()
    return redirect('products')
