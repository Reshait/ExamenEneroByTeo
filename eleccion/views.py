from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from eleccion.models import Circunscripcion, Mesa
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect


# Create your views here.


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

class Index(TemplateView):
    template_name = "eleccion/index.html"


def Login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/eleccion/')
                #Me falla si no estoy en /eleccion/
            else:
                return HttpResponse("Su cuenta esta deshabilitada.")
        else:
            print "Nombre de usuario o password incorrectos: {0}, {1}".format(username, password)
            return HttpResponse("Datos de login incorrectos.")

    else:
        return render(request, 'eleccion/login.html', {})  


@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/eleccion/')
#Me falla si no estoy en /eleccion/

class CircunscripcionLista(ListView):
	model = Circunscripcion
	template_name = "eleccion/circunscripcion.html"


class CircunscripcionCrear(CreateView):
    template_name = 'eleccion/formulario.html'
    model = Circunscripcion
    fields = ('nombre', 'nEscanos')
    success_url = reverse_lazy('circunscripcion_url')

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super(CircunscripcionCrear, self).get_context_data(**kwargs)
        # anyadimos nuevas variables de contexto al diccionario
        context['titulo'] = 'Crear Circunscripcion'
        context['nombre_btn'] = 'Crear'
        # devolvemos el contexto
        return context

def ListadoMesas():
    listadoTitulos = Mesa.objects.all()[:10]
    return listadoMesas

class CircunscripcionDetalle(DetailView):
    model = Circunscripcion
    template_name = 'eleccion/vistaDetallada.html'

    def get_context_data(self, **kwargs):
        context = super(CircunscripcionDetalle, self).get_context_data(**kwargs)
#        context['listadoMesas'] = ListadoMesas()
        return context


class CircunscripcionEditar(UpdateView):
	template_name = 'eleccion/formulario.html'
	model = Circunscripcion
	fields = ('nombre', 'nEscanos')
	success_url = reverse_lazy('circunscripcion_url')

	def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
		context = super(CircunscripcionEditar, self).get_context_data(**kwargs)
	    # anyadimos nuevas variables de contexto al diccionario
		context['titulo'] = 'Editar Circunscripcion'
		context['nombre_btn'] = 'Editar'
        # devolvemos el contexto
		return context

	def dispatch(self, request, *args, **kwargs):
		if not request.user.has_perms('eleccion.change_circunscripcion'):
			return redirect('circunscripcion_url')
		return super(CircunscripcionEditar, self).dispatch(request, *args, **kwargs)

#	def form_valid(self, form):
#		messages.success(self.request, 'Circunscripcion editada correctamente')
#		return super(CircunscripcionEditar, self).form_valid(form)

class CircunscripcionEliminar(DeleteView):
    template_name = 'eleccion/eliminar.html'
    model = Circunscripcion
    success_url = reverse_lazy('circunscripcion_url')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('eleccion.delete_circunscripcion'):
            return redirect('circunscripcion_url')
        return super(CircunscripcionEliminar, self).dispatch(request, *args, **kwargs)

#    def form_valid(self, form):
#        messages.success(self.request, 'Entrada eliminada correctamente')
#        return super(CircunscripcionEliminar, self).form_valid(form)
