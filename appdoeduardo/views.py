from django.shortcuts import render, redirect
from .models import Top15, common_sectors
# Create your views here.
def home(request):
  top15 = Top15.objects.all()
  sectors = common_sectors.objects.all()
  return render(request, "home.html", context = {
    "top15": top15,
    "sectors": sectors
  })
  
def create_top15(request):
  if request.method == "POST":
    Top15.objects.create(
    team = request.POST["team"],
    place = request.POST["place"],
    fuel = request.POST["fuel"],
    placement = request.POST["placement"]
    )

    return redirect("home")
  return render(request, "forms1.html", context={"action": "Adicionar"})

def update_top15(request, id):
  top15 = Top15.objects.get(id = id)
  if request.method == "POST":
    top15.team = request.POST["team"]
    top15.place = request.POST["place"]
    top15.fuel = request.POST["fuel"]
    top15.placement = request.POST["placement"]
    top15.save()
    
    return redirect("home")
  return render(request, "forms1.html", context={"action": "Atualizar","top15": top15})

def delete_top15 (request, id):
  top15 = Top15.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      top15.delete()

    return redirect("home")
  return render(request, "are_you_sure1.html", context={"top15": top15})

def create_sector(request):
  if request.method == "POST":
    common_sectors.objects.create(
    sector = request.POST["sector"],
    priority = request.POST["priority"],
    importance = request.POST["importance"],
    difficulty = request.POST["difficulty"]
    )
    return redirect("home")
  return render(request, "forms2.html", context = {"action": "Adicionar", "importance_choices": common_sectors.importance.field.choices,"difficulty_choices": common_sectors.difficulty.field.choices }) 
  
def update_sectors(request, id):
  sector = common_sectors.objects.get(id = id)
  if request.method == "POST":
    sector.sector = request.POST["sector"]
    sector.priority = request.POST["priority"]
    sector.importance = request.POST["importance"]
    sector.difficulty= request.POST["difficulty"]
    sector.save()
    
    return redirect("home")
  return render(request, "forms2.html", context={"action": "Atualizar", "sector": sector, "importance_choices": common_sectors.importance.field.choices, "difficulty_choices": common_sectors.difficulty.field.choices })

def delete_sector (request, id):
  sector = common_sectors.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      sector.delete()

    return redirect("home")
  return render(request, "are_you_sure2.html", context={"sector": sector})
