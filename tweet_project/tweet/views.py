from django.shortcuts import render
from .models import Tweet
from .forms import TweetForms, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

def index(request):
    return render(request, 'index.html')


# List the Tweet:
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})


# Create Tweet
@login_required # make authenticate
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForms(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False) # save the data into form but not in DB
            tweet.user = request.user 
            tweet.save() # save the all data into DB
            return redirect('tweet_list')
    
    else:
        form = TweetForms()
    
    return render(request, 'tweet_form.html', {'form': form})


# Edit Tweet
@login_required # make authenticate
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet,  pk=tweet_id, user=request.user) # access by particular user
    
    if request.method == 'POST':
        form = TweetForms(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False) # save the data into form but not in DB
            
            tweet.user = request.user # save the tweet to particular user
            tweet.save() # save the all data into DB
            return redirect('tweet_list')
    
    else:
        form = TweetForms(instance=tweet)
        
    return render(request, 'tweet_form.html', {'form': form})


# Delete Tweet:
@login_required # make authenticate
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet,  pk=tweet_id, user=request.user) # access by particular user
    
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})



# User Registration:
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1']) # set the cleaned password1 
            user.save() #save the data:
            login(request, user)
            
            return redirect('tweet_list')
    
    else:
        form = UserRegistrationForm()
    
    
    return render(request, 'regustration/register.html', {'form':form})