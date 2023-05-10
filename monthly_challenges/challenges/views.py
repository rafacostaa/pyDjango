from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "January",
    "february": "February",
    "march": "March"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Page not founded")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month] )
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + forward_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This page is not founded")
    

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)