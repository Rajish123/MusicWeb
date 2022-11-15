from django.shortcuts import redirect


def auth_middleware(get_response):
    def middleware(request):
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.user.is_authenticated:
            # return redirect('accounts:login', instance=returnUrl)
            return redirect(f'/accounts/login/?return_url={returnUrl}')
            
        response = get_response(request)
        return response
    return middleware