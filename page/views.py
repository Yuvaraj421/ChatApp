
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    """
        This method render(provide service) to return home page.
        :param request:
        :return: home page.
    """
    return render(request, 'page/home.html')


def signup(request):
    """
        This method is used to sign up the users by providing the registration form and returns the signup page.
        :param request:
        :returns:  home page if successfully registered or returns to signup page.
    """
    # if the form is valid it redirects to home page else it stays in signup page.
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'page/registrationSuccess.html')
    else:
        form = UserCreationForm()
    return render(request, 'page/signup.html', {
        'form': form
    })
