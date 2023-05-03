from django.shortcuts import render
import random


def index(request):
    text_area = request.POST.get("tarea")
    n = request.POST.get("n")

    res = text_area
    original_list = res
    if text_area is not None and n is not None:
        n = int(n)
        original_list = text_area.split("\r\n")
        while ("" in original_list):
            original_list.remove("")

        if len(original_list) >= n:
            res = random.sample(original_list, n)
            res = ' '.join(res)
        else:
            res = "Za mało elementów by wylosować"

    return render(request, "index.html", {"res": res})
