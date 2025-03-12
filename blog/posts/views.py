from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
posts = [
    {"id": 1,
     "title": "one",
     "content": "one111"},
    {"id": 2,
         "title": "two",
         "content": "two22"},
    {"id": 3,
         "title": "three",
         "content": "three333"},
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

    return render(request, 'posts/home.html', {"name": "Taranjot"})

def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        html = f'''
            <h1>{post_dict['title']}</h1>
            <p>{post_dict['content']}</p>
        '''

        return HttpResponse(html)

    else:
        return HttpResponseNotFound("Post not found")

def local(request, local_name):
    return HttpResponse(f"<h1>{local_name}</h1>")

def google(request, id):
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)