from .models import Company, Usuario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            companies=list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company=companies[0]
                datos={'message':'Success', 'companies':companies}
            else:
                datos={'message':'Company not found'}
            return JsonResponse(datos)
        else:
            companies = list(Company.objects.values())
            if len(companies)>0:
                datos={'message':'Success', 'companies':companies}
            else:
                datos={'message':'Companies not found'}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Company.objects.create(name=jd['name'], website=jd["website"], foundations=jd["foundations"])

        datos = {'message':'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        companies=list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company=Company.objects.get(id=id)
            company.name=jd['name']
            company.website=jd['website']
            company.foundations=jd['foundations']
            company.save()
            datos={'message':'Success'}
        else:
            datos={'message':'Company not found'}
        return JsonResponse(datos)

    def delete(self, request, id):
        companies=list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            Company.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':'Company not found'}
        return JsonResponse(datos)

class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            usuarios=list(Usuario.objects.filter(id=id).values())
            if len(usuarios)>0:
                company=usuarios[0]
                datos={'message':'Success', 'usuarios':usuarios}
            else:
                datos={'message':'Usuario not found'}
            return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios)>0:
                datos={'message':'Success', 'usuarios':usuarios}
            else:
                datos={'message':'Usuarios not found'}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Usuario.objects.create(
            nombre=jd['nombre'], 
            apellido_paterno=jd["apellido_paterno"], 
            apellido_materno=jd["apellido_materno"], 
            edad=jd["edad"], 
            email=jd["email"], 
            telefono=jd["telefono"]
        )

        datos = {'message':'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        usuarios=list(Usuario.objects.filter(id=id).values())
        if len(usuarios)>0:
            usuario=Usuario.objects.get(id=id)
            usuario.nombre=jd['nombre']
            usuario.apellido_paterno=jd['apellido_paterno']
            usuario.apellido_materno=jd['apellido_materno']
            usuario.edad=jd['edad']
            usuario.email=jd['email']
            usuario.telefono=jd['telefono']
            usuario.save()
            datos={'message':'Success'}
        else:
            datos={'message':'Usuario not found'}
        return JsonResponse(datos)

    def delete(self, request, id):
        usuarios=list(Usuario.objects.filter(id=id).values())
        if len(usuarios)>0:
            Usuario.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':'Usuario not found'}
        return JsonResponse(datos)