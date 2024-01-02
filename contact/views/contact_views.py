from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Q 
from django.core.paginator import Paginator

from contact.models import Contact

# Create your views here.
def home(request):
    contacts = Contact.objects.all()

    paginator = Paginator(contacts, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj, 
        'site_title': 'Contacts'
    }

    print(context)

    return render(request, 'index.html', context)

def contact(request, contact_id):
    #single_contact = Contact.objects.filter(pk=contact_id).first()

    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    contact_name = f'{single_contact.first_name} {single_contact.last_name}'

    context = {
        'contact': single_contact,
        'site_title': contact_name 
    }

    return render(request, 'contact.html', context)

def search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('home')
    
    contacts = Contact.objects.filter(show=True) \
        .filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value) | Q(email__icontains=search_value)) \
        .order_by('-id')
    
    paginator = Paginator(contacts, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj, 
        'site_title': 'Search'
    }
    print(context)

    return render(request, 'index.html', context)