from django.http import HttpResponse
from _api.models import User
from django.core import serializers


# Create your views here.
def login(req):

    uname = req.GET.get('uname')
    upass = req.GET.get('upass')
    # u = User(uname= uname, upass= upass)

    data = User.objects.filter(uname= uname, upass = upass)
    json = serializers.serialize('json', data, fields=('uname', 'upass', 'email'))



    return HttpResponse(json , content_type='application/json')