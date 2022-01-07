from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect('list_blogs')

    form = RegisterForm()
    return render(
        request,
        'profiles/register.html',
        {
            "form": form,
        }
    )


def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(
        request,
        "profiles/profile.html",
        {"user": user}
    )


@login_required
def update(request):
    if request.POST:
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form and profile_form:
            user_form.save()
            profile_form.save()

            messages.success(request, "Profile update successfully!")
            return redirect('profiles:profile', request.user.pk)

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

    return render(
        request,
        'profiles/update.html',
        context
    )

