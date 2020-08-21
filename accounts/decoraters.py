from django.http import HttpResponse
from django.shortcuts import redirect


def UserAuth(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_user(allowed_user = []):
    def userallowed(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_user:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("you are not authorized to view this page: ")
        
        return wrapper_func
    return userallowed


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group  == 'customer':
            return redirect('user-page')
        if group == 'admin':
            return view_func(request, *args , **kwargs)

    return wrapper_func