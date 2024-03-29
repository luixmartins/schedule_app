from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse 
from django.contrib.auth.decorators import login_required

from contact.models import Contact
from contact.forms import ContactForm

@login_required(login_url='login')
def create(request):
    form_action = reverse('create') 

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)

        context = {
            'form': ContactForm(), 
            'form_action': form_action, 
        }

        if form.is_valid():
            #contact = form.save(commit=False) #não salva no banco de dados 
            #contact.show = False 

            contact = form.save(commit=False)
            contact.owner = request.user 

            contact.save()

            return redirect('contact', contact_id=contact.id)

        
        return render(request, 'create.html', context)
    
    context = {
            'form': ContactForm(), 
            'form_action': form_action, 
        }

    return render(request, 'create.html', context)

@login_required(login_url='login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, show=True, owner=request.user) #busca contato 

    form_action = reverse('update', args=(contact_id, )) #para alterar dinamicamente a variavel no form. VERIFICAR FORM ACTION no arquivo CREATE.HTML 

    if request.method == "POST": #verifica o método para atualizar os dados 
        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'form': ContactForm(), 
            'form_action': form_action, 
        }

        if form.is_valid():
            contact = form.save()

            return redirect('contact', contact_id=contact.id) #dados salvos, redireciona para o detail 

        

        return render(request, 'create.html', context) #se o formulário não é valido, continua na msm página com os campos preenchidos 
    
    #método GET, acabou de chamar a url 
    context = {
            'form': ContactForm(instance=contact), 
            'form_action': form_action, 
        }

    return render(request, 'create.html', context)

@login_required(login_url='login')
def delete(request, contact_id):
    confirmation = request.POST.get('confirmation', 'no')
    contact = get_object_or_404(Contact, id=contact_id)
    
    if confirmation == 'yes':
        contact.delete()

        return redirect('home')

    context = {
        'contact': contact, 
        'confirmation': confirmation, 
    }
    return render(request, 'contact.html', context)
    