from django.shortcuts import render, redirect
from .models import Message, Profile
from .forms import MessageForm, ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('message_history')
    else:
        form = MessageForm()
    return render(request, 'messages/send_message.html', {'form': form})

@login_required
def message_history(request):
    messages = Message.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'messages/message_history.html', {'messages': messages})

@login_required
def change_name(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('message_history')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'messages/change_name.html', {'form': form})
