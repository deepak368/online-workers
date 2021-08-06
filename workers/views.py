from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserLoginForm,FeedbackForm,UserRequestForm,BookForm,workerRequestForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import login,logout,authenticate
from .models import feedbackmodel,userRequest,Book,workerRequest
from .filters import Search_work
from .decorators import admin_only
from django.utils.decorators import method_decorator
from django.contrib.auth.models import AnonymousUser

class UserRegisterView(TemplateView):
    form_class=UserRegisterForm
    model=User
    template_name ="work/registration.html"
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self,request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return redirect("error")

class UserLoginView(TemplateView):
    form_class=UserLoginForm
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        context={}
        context["form"]=form
        return render(request,"work/login.html",context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            # obj=EmailAuthBackend()
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("userpg")
            else:
                return redirect("login")
        return render(request,"work/registration.html")

def User_logout(request):
    logout(request)
    return redirect("login")

class FeedbackView(TemplateView):
    model=feedbackmodel
    form_class=FeedbackForm
    context={}
    template_name = "work/feedbackget.html"
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={"username": request.user})
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userpg")
        return render(request, self.template_name, self.context)
@method_decorator(admin_only,name='dispatch')
class feedbacklist(TemplateView):
    def get(self, request, *args, **kwargs):
        lists=feedbackmodel.objects.all()
        context={}
        context["lists"] = lists
        return render(request,"work/feedbacklist.html",context)

class UserRequestView(TemplateView):
    form_class=UserRequestForm
    model=userRequest
    template_name = "work/userrequest.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class(initial={"user":request.user})
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()

            return redirect("userreq-rply")
        return render(request, self.template_name, self.context)

class List_userRequest(TemplateView):
    def get(self, request, *args, **kwargs):
        users=userRequest.objects.all()
        context={}

        context["users"]=users
        return render(request,"work/listuserrequest.html",context)


class List_request(TemplateView):
    def get(self, request, *args, **kwargs):
        items=userRequest.objects.all().filter(user=request.user)
        context={}
        context["items"]=items
        return render(request,"work/indivituallist.html",context)

class requestEditView(TemplateView):
    model=userRequest
    form_class=UserRequestForm
    context={}
    template_name ="work/userrequest.html"
    def get(self, request, *args, **kwargs):
        edit=self.model.objects.get(id=kwargs["pk"])
        form=self.form_class(instance=edit)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        edit=self.model.objects.get(id=kwargs["pk"])
        form=self.form_class(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            return render(request,self.template_name,self.context)

class requestDeleteView(TemplateView):
    model=userRequest
    def get(self, request, *args, **kwargs):
        woker=self.model.objects.get(id=kwargs["pk"])
        woker.delete()
        return redirect("userpg")
def search_view(request):
    search =userRequest.objects.all()
    context={}
    workfilter = Search_work(request.GET,queryset=search)
    context["filter"] = workfilter
    return render(request, "work/search.html", context)


class WorkerRequestView(TemplateView):

    form_class=workerRequestForm
    template_name = "work/workerrequest.html"
    def get(self, request, *args, **kwargs):
        clint=userRequest.objects.get(id=kwargs["pk"])
        form=self.form_class(initial={"Clint":clint})
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("worker-reply")
@method_decorator(admin_only,name='dispatch')
class list_workerrequest(TemplateView):
    def get(self, request, *args, **kwargs):
        workers=workerRequest.objects.all()
        context={}
        context["workers"]=workers
        return render(request,"work/workerreqlist.html",context)



class Notification(TemplateView):
    def get(self, request, *args, **kwargs):
        items= userRequest.objects.filter(user=request.user)
        for item in items:
            id=item.id

        work = workerRequest.objects.filter(Clint_id=id)
        context = {}
        context["work"] = work
        return render(request, "work/notification.html", context)

class workerreqRemove(TemplateView):
    model=workerRequest
    def get(self, request, *args, **kwargs):
        woker=self.model.objects.get(id=kwargs["pk"])
        woker.delete()
        return redirect("userpg")

class BookView(TemplateView):
    form_class=BookForm
    model=Book
    template_name = "work/book.html"
    def get(self, request, *args, **kwargs):
        work = workerRequest.objects.get(id=kwargs["pk"])
        form=self.form_class(initial={"Username":request.user,"worker_name":work})
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("final")
@method_decorator(admin_only,name='dispatch')
class Bookdetails(TemplateView):
    def get(self, request, *args, **kwargs):
        workers = Book.objects.all()
        context = {}
        context["workers"] = workers
        return render(request, "work/Bookeddetails.html", context)



