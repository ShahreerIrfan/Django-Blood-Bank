from django.shortcuts import render,redirect
from .forms import SupportForm
from.models import Support
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def support(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            support_instance = form.save(commit=False)
            support_instance.who_need_support = request.user
            support_instance.save()
            return redirect('home')  
    else:
        form = SupportForm()  
    return render(request, 'support/support.html', {'form': form})


# ...........