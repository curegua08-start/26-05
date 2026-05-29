from django.shortcuts import render
# def --->funcion
#---> request : retorna la pagina web 
def home (request):
 #---> cada vez que llamamos a 'Home
 #--> etsmos hablandode la pagina Base html 
 return render(request,'Base.html')
