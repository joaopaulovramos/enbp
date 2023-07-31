# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView

from djangosige.apps.taticca_cv.forms.Forms import CVForm, CertificadoForm
from djangosige.apps.taticca_cv.models.taticca_cv import CVModel, CertificadoModel

from django.core.files.storage import default_storage






class ListView(CustomListView):
    template_name = 'taticca_cv/exemplo_operacao_list.html'
    model = CVModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('taticca_cv:listaexemplo')


    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tattico CV'
        context['add_url'] = reverse_lazy('taticca_cv:adicionaexemplo')
        return context

class AdicionarView(CustomCreateView):
    #form_class = NaturezaOperacaoForm
    form_class = CVForm
    template_name = "taticca_cv/add.html"
    success_url = reverse_lazy('taticca_cv:listaexemplo')
    success_message = "Adicionar Exemplo <b>%(cfop)s </b>adicionado com sucesso."


    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR EXEMPLO'
        context['return_url'] = reverse_lazy('taticca_cv:listaexemplo')
        return context






class EditarView(CustomUpdateView):
       form_class = CVForm
       model = CVModel

       template_name = "taticca_cv/edit.html"
       success_url = reverse_lazy('taticca_cv:editacv')
       success_message = "Item faturamento editado com sucesso."




       def get_object(self):
           current_user = self.request.user
           return CVModel.objects.get(user=current_user)

       def post(self, request, *args, **kwargs):
           self.object = self.get_object()
           form = CVForm(request.POST, request.FILES, instance=self.object)

           if len(form.files) != 0:
                current_user = self.request.user
                name = current_user.username+'.jpg'

                path = 'imagens/users/'+name
                if default_storage.exists(path):
                    default_storage.delete(path)


                request.FILES['foto'].name = name

           form.save(commit=True)
           return self.form_invalid(form)




       def get_success_message(self, cleaned_data):
           return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

       def get_context_data(self, **kwargs):
           context = super(EditarView, self).get_context_data(**kwargs)
           context['return_url'] = reverse_lazy('taticca_cv:editacv')
           current_user = self.request.user

           path = 'imagens/users/' + current_user.username + '.jpg'
           if default_storage.exists(path):
                context['foto'] = current_user.username + '.jpg'
           else:
               context['foto'] = 'user_geral_sistema.jpg'
           return context


################################ certificados



class ListCertificadoView(CustomListView):
    template_name = 'taticca_cv/certificado_list.html'
    model = CertificadoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('taticca_cv:listacertificados')


    def get_context_data(self, **kwargs):
        context = super(ListCertificadoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tattico CV'
        context['add_url'] = reverse_lazy('taticca_cv:adicionacertificado')
        return context

class AdicionarCertificadoView(CustomCreateView):
    form_class = CertificadoForm
    template_name = "taticca_cv/add_certificado.html"
    success_url = reverse_lazy('taticca_cv:listacertificados')
    success_message = "Certificado Adicionado."


    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarCertificadoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar certificado'
        context['return_url'] = reverse_lazy('taticca_cv:listacertificados')
        return context




