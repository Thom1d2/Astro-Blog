from django.shortcuts import render

# create post_list views

def post_list(request):
    return render(request, 'astroblog/post_list.html', {})
