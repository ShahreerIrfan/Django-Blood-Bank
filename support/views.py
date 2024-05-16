from django.shortcuts import render,redirect
from .forms import SupportForm
from.models import Support

# Create your views here.
def support(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            support_instance = form.save(commit=False)
            support_instance.who_need_support = request.user
            support_instance.save()
            return redirect('home')  # Redirect to a success page or another view
    else:
        form = SupportForm()  # Correctly instantiate the form with parentheses
    return render(request, 'support/support.html', {'form': form})