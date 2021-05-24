from django.http import HttpResponse
from django.shortcuts import redirect

 

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            print('/sa', request.user.groups.exists())

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print('group', group)

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not ')

        return wrapper_func

    return decorator


 
