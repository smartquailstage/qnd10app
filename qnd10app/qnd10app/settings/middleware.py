from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group

class GroupAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is not authenticated
        if not request.user.is_authenticated:
            # Allow access to the login page
            if request.path == '/login/':
                return self.get_response(request)
            # Otherwise, forbid access
            return HttpResponseForbidden("Acceso Denegado.Usted intento violar el articulo N.56 del contrato de tecnologias Para volver a ingresar contactese con: SmartQuail.S.A.S - +592-99-6352-1262")

        # Check if the user is a member of the specified group
        required_group_name = 'Administrador'  # Replace with your desired group name
        required_group = Group.objects.filter(name=required_group_name).first()

        if required_group and request.user.groups.filter(id=required_group.id).exists():
            return self.get_response(request)
        else:
            return HttpResponseForbidden("Acceso Denegado.Usted intento violar el articulo N.56 y N.58 del contrato de tecnologias Para volver a ingresar contactese con: SmartQuail.S.A.S - +592-99-6352-1262")