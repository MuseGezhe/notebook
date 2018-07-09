from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,redirect
class VerifycodeMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.path == '/login/' and request.method == 'POST':
            # 判断验证码
            verifycode = request.POST.get('verifycode')
            if not verifycode.upper() == request.session.get('verifycode').upper():
                return redirect('/login/')
            else:
                return None


