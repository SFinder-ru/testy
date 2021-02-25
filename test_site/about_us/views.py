from django.shortcuts import render


def about_us_view(request):
    return render(request, "site_pages/about.hml")
