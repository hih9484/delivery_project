from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def join(request):
    if request.method == 'GET':
        return render(request, 'registration/join.html')
    elif request.method == 'POST':
        # 가입시에 제출한 username과 중복된 계정이 있는지 확인
        # count()는 object의 수량을 센다
        # data가 0이라면 중복되는 계정이 없다는 뜻
        data = User.objects.filter(username = request.POST.get('username')).count()
        if data == 0:
            # password 와 password_check가 일치하는지 확인
            if request.POST.get('password') == request.POST.get('password_check'):
                # 일치한다면 User 테이블의 객체를 하나 생성하여 값들을 넣어준다(계정 생성)
                user = User()
                user.username = request.POST.get('username')
                # password는 set_password 를 통해 암호화 과정을 거쳐서 지정하게끔
                user.set_password(request.POST.get('password'))
                #user.address = request.POST.get('address')
                user.email = request.POST.get('email')
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.save()
            else:
                # 패스워드가 일치하지 않는다면
                # 회원가입 양식을 채워주기 위해 context에 사전형으로 입력 정보를 넣어주고 password_error 항목도 같이 전달
                context = dict(request.POST)
                context.update(
                    {
                        'password_error' : '패스워드 불일치'
                    }
                )
                return render(request, 'registration/join.html', context)
        else:
            # 중복된 계정이 있다면 다시 양식을 채워 넣기 위해 request.POST를 넘겨준다
            # request.POST는 사전형
            context = dict(request.POST)
            context.update(
                {
                    'username_error' : '해당 username은 이미 존재합니다'
                }
            )
            return render(request, 'registration/join.html', context)

        # 아이디 생성이 문제없이 완료되면 메인 페이지로 이동
        return redirect('/store')