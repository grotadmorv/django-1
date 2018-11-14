from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelForm
from django.urls import reverse_lazy
from pasteAsMarkdown.models import Markdown
from django.views.generic.edit import FormView


class PastebinForm(ModelForm):
    class Meta:
        model = Markdown
        fields = ["markdown_txt", "path"]



class PasteFormMarkdown(FormView):
    template_name = 'pasteAsMarkdown/form.html'
    form_class = PastebinForm



def create_url(request):
    if request.POST['markdown_txt']:
        a = Markdown(markdown_txt=request.POST['markdown_txt'], path=request.POST['path'])
        a.save()
        # print(Markdown.objects.all())
        return HttpResponseRedirect(f"/pasteAsMarkdown/show/{a.path}")

def show(request, path):
    m = Markdown.objects.get(path=path)
    return render(request, 'pasteAsMarkdown/show.html', {
        'path' : path
    })

