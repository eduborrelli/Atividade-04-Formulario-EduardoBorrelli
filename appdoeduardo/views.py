from django.shortcuts import render, redirect
from .models import Top15, common_sectors
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  top15 = Top15.objects.all()
  sectors = common_sectors.objects.all()
  return render(request, "home.html", context = {
    "top15": top15,
    "sectors": sectors
  })

@login_required
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

@login_required
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

@login_required
def delete_top15 (request, id):
  top15 = Top15.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      top15.delete()

    return redirect("home")
  return render(request, "are_you_sure1.html", context={"top15": top15})

@login_required
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

@login_required
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

@login_required
def delete_sector (request, id):
  sector = common_sectors.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      sector.delete()

    return redirect("home")
  return render(request, "are_you_sure2.html", context={"sector": sector})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action": "Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )
    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")