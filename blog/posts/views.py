from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.
posts = [
    {"id": 1,
     "title": "one",
     "content": "one111, so I don't know what is one said bla bla bla"},
    {"id": 2,
         "title": "two",
         "content": "two22, and You don't know too two said bla bla bla"},
    {"id": 3,
         "title": "three",
         "content": "three333, and we do know three said bla bla bla"},
]

def home(request):
    html = ""
    for post in posts:
        html += f'''
        <div>
        <a href="/post/{post['id']}/">
            <h1>{post['id']} - {post['title']}</h1> 
        </a>
            <p>{post['content']}</p>
        </div>  
        '''
    return render(request, 'posts/index.html', {"posts": posts, "username": "ujeon"})

def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        return render(request, "posts/postcard.html", {"post_dict": post_dict})

    else:
        raise Http404()
