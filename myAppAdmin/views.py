from django.shortcuts import render, HttpResponse
from myAppAdmin.models import Contact
from myApp import settings
import boto3
import os
from django.conf import settings
# Create your views here.

class allformfunc():

    def index(request):
        return render(request, 'index.html')

    def register(request):
        return render(request, 'register.html')



    def awsupload(file_local_path,file_name,bucket_folder_path):

        ROOT_DIR=settings.BASE_DIR
        S3_BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME
        REGION_NAME = settings.AWS_S3_REGION_NAME
        s3_client = boto3.client("s3", 
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name=REGION_NAME)
        
        s3_client.upload_file(ROOT_DIR+file_local_path+file_name,S3_BUCKET_NAME,bucket_folder_path+file_name)


    def form(request):
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone1 = request.POST.get("phone1")
            file1 = request.FILES
            img = file1.get('file1')
            print(img ,file1)
            
            user_folder = 'media/ammar-practice'
            img_extension = os.path.splitext(img.name)[1]
            file_name = os.path.splitext(img.name)[0]
            print(user_folder)
            print(user_folder)
            if not os.path.exists(user_folder):
                os.makedirs(user_folder,mode = 0o777)
            img_save_path = "%s/%s%s"%(user_folder,file_name,img_extension)
            print("@@@",img.name)
            print(type(img_save_path))
            print(img_save_path)

            with open(img_save_path,"wb+") as f:
                for chunk in img.chunks():
                    f.write(chunk)

            bucket_folder_path = 'ammar-practice/'
            print(file_name+img_extension)
            allformfunc.awsupload("/"+user_folder+"/",file_name+img_extension,bucket_folder_path)

        return render(request, 'form.html')


    def charts(request):
        return render(request, 'charts.html')

    def forgot(request):
        return render(request, 'forgot-password.html')

    def error(request):
        return render(request, '404.html')

    def blank(request):
        return render(request, 'blank.html')

    def about(request):
        return HttpResponse("about page")
        
