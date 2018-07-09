from django.utils.deprecation import MiddlewareMixin
from axf.models import User
from django.http import JsonResponse

class CheckLoginMiddleware(MiddlewareMixin):
    def process_request(self,request):
        #验证是否登录
        if request.path == '/carts/':
            token = request.COOKIES.get('token')
            try:
                #已登录
                user = User.objects.get(tokenValue=token)
                request.user = user
                request.token = token
            except User.DoesNotExist as e:
                #未登录
                return JsonResponse({'error':1})