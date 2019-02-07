from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from board_app.forms import BoardForm
from board_app.models import BoardDB
from django.core.paginator import Paginator

# Create your views here.
def boardIndex(request):
    if request.method == 'GET':
        # 인터넷에서 url 요청이 있을때 if문이 실행
        data = BoardDB.objects.all()
        #data에 모든 객체를 불러 담음
        context = {}
    elif request.method == 'POST':
        data = BoardDB.objects.filter(title__contains=request.POST.get('search'))
        context = {}
    paging = Paginator(data, 3)
    page = paging.page(request.GET.get('page',1))
    context.update(
        {
            'data': page,
            'page_range':paging.page_range
        }
    )
    return render(request, 'board_app/index.html',context)

def boardDetail(request, board_id):
    if request.method == 'GET':
        data = BoardDB.objects.get(id=board_id)

        data.view_count += 1

        # update_fields 는 튜플 자료형이기 때문에 업데이트할 필드가 하나밖에 없더라도 , 를 입력 해줘야 한다
        data.save(update_fields=('view_count',))

        context = {
            'data': data
        }

        return render(request, 'board_app/detail.html', context)

def boardWrite(request):
    if request.user.is_active:
        if request.method == 'GET':
            # BoardForm 객체를 보내줄 때 author는 접속한 유저의 이름 값을 애초에 넣어준다
            form = BoardForm(initial={'author': request.user.username})

            context = {
                'form': form
            }

            return render(request, 'board_app/write.html', context)

        elif request.method == 'POST':
            data = BoardDB(
                title=request.POST.get('title'),
                author=request.POST.get('author'),
                context=request.POST.get('context')
            )
            data.save()

            # 작성과 동시에 그 게시물의 상세 창(detail.html)으로 넘어간다 기존은 return redirect('detail', data.id)
            # 상세 창에서 그 게시물의 데이터를 추출하기 위해 data.id(게시물의 id)도 같이 넘김
            # detail의 url 정규 표현식에도 사용된다
            return redirect('index')
    else:
        return redirect('login')


def boardUpdate(request):
    if request.user.is_active:
        if request.method == 'GET':

            data = BoardDB.objects.get(id=request.GET.get('id'))

            if request.user.username == data.author:
                form = BoardForm(
                    initial={
                        'title': data.title,
                        'author': data.author,
                        'context': data.context
                    }
                )
            context = {
                'data': data,
                'form': form
            }
            return render(request, 'board_app/update.html', context)
        elif request.method == 'POST':

            data = BoardDB.objects.get(id=request.POST.get('id'))

            if request.user.username == data.author:
                data.title = request.POST.get('title')
                data.author = request.POST.get('author')
                data.context = request.POST.get('context')
                data.save()

            return redirect('index')
    else:
        return redirect('login')

def boardDelete(request):
    if request.user.is_active:
        if request.method == 'GET':

            board_id = request.GET.get('id')

            context = {
                'id': board_id
            }

            return render(request, 'board_app/delete.html', context)

        elif request.method == 'POST':
            data = BoardDB.objects.get(id=request.POST.get('id'))

            data.delete()

            return redirect('index')
    else:
        return redirect('login')

def boardGoodBad(request, type):
    if request.user.is_active:
        if request.method == 'GET':
            data = BoardDB.objects.get(id=request.GET.get('id'))
            if type == 'good':
                data.good_count += 1
            elif type == 'bad':
                data.bad_count += 1

            # 추천 버튼을 누르는 동시에 detail 페이지로 redirect 시켜주기 때문에 조회수도 자동적으로 상승
            # 그렇기 때문에 조회수를 미리 하나 줄인다
            data.view_count -= 1

            # updata_data 필드의 갱신을 막기 위해서 updata_field 를 직접 명시
            data.save(update_fields=('good_count', 'bad_count', 'view_count'))

        return redirect('detail', data.id)
    else:
        return redirect('login')
