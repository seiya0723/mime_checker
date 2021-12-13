from django.shortcuts import render,redirect
from django.contrib import messages

from django.views import View
from .models import Topic
from .forms import TopicForm

import magic


class BbsView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):
        
        form        = TopicForm(request.POST,request.FILES)

        if form.is_valid():
            print("バリデーションOK")

            mime    = magic.from_buffer(request.FILES["document"].read(1024) , mime=True)
            messages.add_message(request, messages.INFO, mime)
            print(mime)

        else:
            print("バリデーションNG")

        return redirect("bbs:index")

index   = BbsView.as_view()

