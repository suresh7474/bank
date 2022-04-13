from django.shortcuts import render
from .models import Employee,Address
from django.core.serializers import serialize
from django.http import JsonResponse,HttpResponse
import json
def user(request):
    qs=Address.objects.all().prefetch_related('employee')
    jeson=serialize('json',qs)
    pdict=json.loads(jeson)
    s=[]
    r=0
    for c,i in enumerate(qs):
        a=i.employee.all()
        d=(serialize('json',a))
        # print(d)
        p=json.loads(d)
        for j in p:
            s.append((j['pk'],j['fields']['ename'],pdict[0]['fields']))
            # print(type(j))

    return HttpResponse(s)



