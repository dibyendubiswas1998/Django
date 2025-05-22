from django.shortcuts import render
from .models import Tweet
from .forms import TweetForms
from django.shortcuts import get_object_or_404, redirect


def index(request):
    return render(request, 'index.html')


# List the Tweet:
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})


# Create Tweet
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
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet,  pk=tweet_id, user=request.user) # access by particular user
    
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})