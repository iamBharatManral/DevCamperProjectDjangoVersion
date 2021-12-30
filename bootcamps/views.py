from django.http import JsonResponse
# Create your views here.

def getAllBootcamps(request):
  return JsonResponse({"success": True, "msg" : "Show all bootcamps"})

def getBootcampById(request,id):
  return JsonResponse({"success": True, "msg" : "Show bootcamp with id"})

def updateBootcamp(request,id):
  return JsonResponse({"success": True, "msg" : "Update bootcamp with id"})

def deleteBootcamp(request,id):
  return JsonResponse({"success": True, "msg" : "Delete bootcamp with id"})

def createBootcamp(request):
  return JsonResponse({"success": True, "msg" : "Create a new bootcamp"})
