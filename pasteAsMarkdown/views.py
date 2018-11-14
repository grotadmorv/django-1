from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelForm
from django.urls import reverse_lazy
from pasteAsMarkdown.models import MarkdownModel
from markdown2 import Markdown
from django.views.generic.edit import FormView
import uuid



class PastebinForm(ModelForm):
    class Meta:
        model = MarkdownModel
        fields = ["markdown_txt", "path"]



class PasteFormMarkdown(FormView):
    template_name = 'pasteAsMarkdown/form.html'
    form_class = PastebinForm



def create_url(request):
    if request.POST['markdown_txt']:
        if not request.POST['path']:
            path = str(uuid.uuid4())
        else:
            path = request.post['path']
        a = MarkdownModel(markdown_txt=request.POST['markdown_txt'], path=path)
        a.save()
        # print(Markdown.objects.all())
        return HttpResponseRedirect(f"/pasteAsMarkdown/show/{a.path}")

def show(request, path):
    markdowner = Markdown()
    markdown_txt = markdowner.convert(str(MarkdownModel.objects.get(path=path)))
    return render(request, 'pasteAsMarkdown/show.html', {
        'path' : path,
        'markdown_txt' : markdown_txt
    })

