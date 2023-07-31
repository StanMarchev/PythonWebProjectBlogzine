from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render



from blogzine.blog_auth.forms.user_profile import  ProfileEditForm
from blogzine.blog_auth.models import UserProfile







@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=user_profile)

    return render(request, 'auth/dashboard-edit-profile.html', {'form': form})
@login_required
def view_profile(request):

    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'auth/profileview.html', {'user_profile': user_profile})




