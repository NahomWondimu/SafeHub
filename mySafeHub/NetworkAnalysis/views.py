from django.http import HttpResponse
from django.template import loader

# Create your views here.
def Net_Analysis(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())