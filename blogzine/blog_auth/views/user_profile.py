from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render



from blogzine.blog_auth.forms.user_profile import  ProfileEditForm



@login_required
def view_profile(request):
    user = request.user
    return render(request, 'common', {'user': user})



@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  #
    else:
        form = ProfileEditForm(instance=user)

    return render(request, 'auth/dashboard-edit-profile.html', {'form': form})




