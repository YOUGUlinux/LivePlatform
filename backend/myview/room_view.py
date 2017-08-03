from django.http import HttpResponse
from django.utils import timezone # put it into toolkits?
from backend.models import User,LiveRoom,Punishment
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from . import toolkits
import os

CODE = toolkits.CODE #assign to local name to reduce the usage of its long prefix
bi2obj = toolkits.bi2obj
LOG = toolkits.Log

def hasLogin(dic):
    return 'user' not in dic
'''
def createDir(room_id):#db will do this automaticlly
    path = os.path.join(os.getcwd(),'files',str(room_id))
    os.makedirs(path)
    return room_id'''

@require_POST
def createRoom(request):
    thumbnail = request.FILES.get('thumbnail',None)
    slide = request.FILES.get('slide',None)
    name = request.POST.get('name')
    creater_id = request.POST.get('creater_id')
    room = LiveRoom(name = name, creater_id = creater_id)
    if(thumbnail):
        thumbnail_type = os.path.splitext(thumbnail.name)[1]
        if(thumbnail_type.endswith(('.jpg','.png','.jpeg','.gif'))):
            room.thumbnail_path = thumbnail
        else:
            return HttpResponse(CODE['20'])
    if(slide):
        slide_type = os.path.splitext(slide.name)[1]
        if(slide_type.endswith(('.ppt','.pptx','.pps'))):#any type else ?
            room.slide_path = slide
        else:
            return HttpResponse(CODE['20'])
    room.save()
    return HttpResponse(room.id) # return the new room's id

@require_POST
def endRoom(request):
    body = bi2obj(request)
   # user = request.session['user']# session need save a user entity & a room entity
    #room = request.session['room']
    session_user = { 'id': 1 }
    session_room = { 'id': 1 }
    request.session['user'] = session_user
    request.session['room'] = session_room
    if('user' in request.session):
        user = request.session['user']
        if('room' in request.session):
            rooms = LiveRoom.objects.filter(id = session_room['id'])
            if(len(rooms) > 0):
                room = rooms[0]
                if(room.creater_id == user['id']):#creater_id : a way to save one query.  must end it by the creater !
                    room.end_time = timezone.now()
                    room.is_living = False
                    room.save()
                    LOG("CQX-room_view.endRoom" , "Room: " + str(room.id) +"has been closed")
                    return HttpResponse(CODE['0'])
                else:
                    return HttpResponse(CODE['5'])
            else :
                return HttpResponse(CODE['6'])
            
        else:
            return HttpResponse(CODE['7'])
    else :
        return HttpResponse(CODE['5'])


