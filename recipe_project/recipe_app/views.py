from http.client import responses

import requests
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import TourismForm
from .serializers import TourismSerializer
from rest_framework import status
from .models import Tourism, User, loginTable
from django.contrib import messages



# Create your views here.

# Create endpoint views here.

class TourismCreateView(APIView):

    def post(self,request):

        serializer = TourismSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):

        tourism = Tourism.objects.all()
        serializer = TourismSerializer(tourism,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

# Detail endpoint views here.

class TourismListView(APIView):

    def get(self,request):

        tourism = Tourism.objects.all()
        serializer = TourismSerializer(tourism,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class TourismDetailView(APIView):

    def get(self,request,id):

        tourism = Tourism.objects.get(id=id)
        serializer = TourismSerializer(tourism,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)


# Update endpoint views here.

class TourismUpdateView(APIView):

    def patch(self,request,id):

        tourism = get_object_or_404(Tourism,id=id)

        serializer = TourismSerializer(tourism,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):

        tourism = Tourism.objects.get(id=id)
        serializer = TourismSerializer(tourism,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)


# Delete endpoint views here.

class TourismDeleteView(APIView):

    def delete(self,request,id):

        tourism = get_object_or_404(Tourism,id = id)

        tourism.delete()
        return Response({'message':'Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)


    def get(self,request,id):

        tourism = Tourism.objects.get(id = id)
        serializer = TourismSerializer(tourism,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)




def Tourism_create(request):


    form = TourismForm(request.POST, request.FILES)

    if request.method == 'POST':

        if form.is_valid():

            form.save()
            data=form.cleaned_data

            api_url = 'http://127.0.0.1:8000/add-data/'
            response = requests.post(api_url,data)

            if response.status_code == 200:
                return redirect('admin-detail')
            else:
                return redirect('admin_view')

        else:
            form = TourismForm()


        return redirect('admin-detail')

    return render(request, 'create_tourism.html',{'form':form})



def Tourism_list(request):
    api_url = f'http://127.0.0.1:8000/list-data/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
    else:
        data=[]

    paginator = Paginator(data,3)
    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)

    except EmptyPage:
        page= paginator.page(page_number.num_pages)

    return render(request,'edit-tourism.html',{'data':data,'page':page})


def Tourism_Update(request, id):
    tourism_instance = get_object_or_404(Tourism, id=id)

    form = TourismForm(request.POST or None, request.FILES or None, instance=tourism_instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            data = form.cleaned_data

            api_url = f'http://127.0.0.1:8000/update-data/{id}/'

            response = requests.patch(api_url, data=data)

            # Check the response from the API
            if response.status_code == 200:
                return redirect('detail')  # Redirect on successful update
            else:
                return redirect('list')  # Redirect to another view on failure

    return render(request, 'update_tourism.html', {'form': form})





def Tourism_Detail(request,id):
    api_url = f'http://127.0.0.1:8000/detail-data/{id}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
    else:
        data=[]
    return render(request,'detail_tourism.html',{'data':data})


def Tourism_delete(request,id):

    api_url = f'http://127.0.0.1:8000/delete-data/{id}'
    response = requests.delete(api_url)

    if response.status_code == 200:
        print(f'{id} Deleted successfully')
    else:
        print(f'Failed to delete {id}')

    return redirect('detail')


def base_view(request):
    api_url = f'http://127.0.0.1:8000/list-data/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
    else:
        data = []

    paginator = Paginator(data, 3)
    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request,'list_tourism.html',{'data':data,'page':page})





def userRegistration(request):

    login_table = loginTable()
    userprofile = User()

    if request.method=='POST':

        userprofile.username=request.POST['username']
        userprofile.password = request.POST['password']
        userprofile.password2 = request.POST['password2']

        login_table.username = request.POST['username']
        login_table.password = request.POST['password']
        login_table.password2 = request.POST['password2']
        login_table.type='user'

        if request.POST['password']==request.POST['password2']:
            userprofile.save()
            login_table.save()

            messages.info(request,'Registration Success')
            return redirect('login')
        else:
            messages.info(request,'Password not working')
            return redirect('base')

    return render(request,'adminfile/register.html')



def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=loginTable.objects.filter(username=username,password=password,type ='user').exists()

        try:
            if user is not None:
                user_details=loginTable.objects.get(username=username,password=password)
                user_name = user_details.username
                type=user_details.type

                if type=='user':
                    request.session['username'] = user_name
                    return redirect('base')
                elif type=='admin':
                    request.session['username'] = user_name
                    return redirect('admin_view')
            else:
                messages.info(request,'Invalid Username or Password')
        except:
            messages.info(request,'Invalid Role')

    return render(request, 'adminfile/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):

    return render(request,'adminfile/index.html')

def admin_view(request):

    user_name = request.session['username']
    user = User.objects.all()

    paginator = Paginator(user, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request,'adminfile/listview.html',{'user_name':user_name,'page':page})



def user_view(request):
    user_name = request.session['username']

    return render(request,'base.html',{'user_name':user_name})


def AdminTourismCreate(request):

    form = TourismForm(request.POST, request.FILES)

    if request.method == 'POST':

        if form.is_valid():

            form.save()
            data=form.cleaned_data

            api_url = 'http://127.0.0.1:8000/add-data/'
            response = requests.post(api_url,data)

            if response.status_code == 200:
                return redirect('admin-detail')
            else:
                return redirect('admin_view')

        else:
            form = TourismForm()


        return redirect('admin-detail')

    return render(request, 'adminfile/admin-create.html',{'form':form})


def AdminTourismList(request):
    api_url = f'http://127.0.0.1:8000/list-data/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
    else:
        data=[]

    paginator = Paginator(data,3)
    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)

    except EmptyPage:
        page= paginator.page(page_number.num_pages)

    return render(request,'adminfile/admin-list.html',{'data':data,'page':page})



def AdminTourismDetail(request,id):
    api_url = f'http://127.0.0.1:8000/detail-data/{id}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
    else:
        data=[]

    return render(request,'adminfile/admin-detail.html',{'data':data})




def AdminTourismDelete(request,id):

    api_url = f'http://127.0.0.1:8000/delete-data/{id}'
    response = requests.delete(api_url)

    if response.status_code == 200:
        print(f'{id} Deleted successfully')
    else:
        print(f'Failed to delete {id}')

        return redirect('admin-detail')



def AdminTourismUpdate(request,id):
    tourism_instance = get_object_or_404(Tourism, id=id)

    form = TourismForm(request.POST or None, request.FILES or None, instance=tourism_instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            data = form.cleaned_data

            api_url = f'http://127.0.0.1:8000/update-data/{id}/'

            response = requests.patch(api_url, data=data)

            # Check the response from the API
            if response.status_code == 200:
                return redirect('admin-detail')  # Redirect on successful update
            else:
                return redirect('admin_view')  # Redirect to another view on failure

    return render(request, 'adminfile/admin-update.html', {'form': form})





















