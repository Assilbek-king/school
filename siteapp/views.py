from django.shortcuts import render
from siteapp.models import *
# Create your views here.

def indexHandler(request):
    blog = Blog.objects.all()[:3]
    teacher = Teacher.objects.filter(status=1)[:4]
    sabaq = Ashiqsabaq.objects.all()
    calc = Calculate.objects.all()[:4]
    post = Post.objects.all()[:3]
    gallery = Gallery.objects.all()
    contact = Contact.objects.all()[:1]

    return render(request, 'index.html', {'blog': blog,
                                          'teacher': teacher,
                                          'sabaq': sabaq,
                                          'calc': calc,
                                          'post': post,
                                          'gallery': gallery,
                                          'contact': contact
                                          })

def gosHandler(request):
    contact = Contact.objects.all()[:1]
    gos = Gos.objects.all()

    return render(request, 'gos.html', {'gos': gos,
                                         'contact': contact})


def postHandler(request):
    post = Post.objects.filter(status=1)
    contact = Contact.objects.all()[:1]

    return render(request, 'blog.html', {'post': post,
                                         'contact': contact})



def postItemHandler(request,post_id):
    posts = Post.objects.all()[:3]
    post = Post.objects.get(id=int(post_id))
    contact = Contact.objects.all()[:1]

    return render(request, 'blog-single.html', {'post': post,
                                                'posts': posts,
                                                'contact': contact})


def aboutHandler(request):
    contact = Contact.objects.all()[:1]
    return render(request, 'about.html', {'contact': contact })


def teacherHandler(request):
    teacher = Teacher.objects.order_by('-id')
    contact = Contact.objects.all()[:1]

    return render(request, 'teacher.html', {'teacher': teacher,
                                            'contact': contact
                                            })


def galleryHandler(request):
    gallery = Gallery.objects.all()
    contact = Contact.objects.all()[:1]

    return render(request, 'gallery.html', {'gallery': gallery,
                                            'contact': contact
                                            })


def contactHandler(request):
    contact = Contact.objects.all()[:1]

    return render(request, 'contact.html', {'contact': contact })
