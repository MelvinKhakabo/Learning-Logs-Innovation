from django.shortcuts import render

def index(request):
    return render(request, 'learning_logs/home.html')


from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Topic
from django.contrib.auth.decorators import login_required
from .models import Topic


@login_required(
login_url='users:login'
) 
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    #Make sure the tpoic belongs to the current user
    if topic.owner != request.user:
       raise Http404
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)



from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse  # Import reverse to generate URLs by view name
from .forms import TopicForm

from django.shortcuts import render, get_object_or_404
from .models import Topic, Entry


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)  # Fetch the topic or return 404 if not found
    entries = topic.entry_set.order_by('-date_added')  # Get all related entries, ordered by date
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TopicForm

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect(reverse('learning_logs:topics'))

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import EntryForm

from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic
from .forms import EntryForm

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a specific topic."""
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Entry
from .forms import EntryForm

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    # Make sure the entry belongs to the current user
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request: Pre-fill the form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted: Process the updated data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


from django.shortcuts import render
from .models import Topic

def home(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/home.html')
# learning_logs/views.py

