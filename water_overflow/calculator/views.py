from django.shortcuts import render

from .water_overflow import WaterOverflow

def index(request):
    template = 'index.html'

    return render(request, template)

def get_content(request):
    template = 'index.html'
    context = dict()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if not all(request.POST.get(key) != '' for key in ('liquid_volume', 'row', 'position')):
            context["error_message"] = "Please be sure to fill-in all the data needed."
        else:
            liquid_volume_input = float(request.POST.get('liquid_volume'))
            row = int(request.POST.get('row'))
            pos = int(request.POST.get('position'))
            try:
                glasses = WaterOverflow.get_content(liquid_volume_input)
                liquid_level = glasses[row][pos].content
                context["success_message"] = f"The liquid volume of glass in row {row} at position {pos} is {liquid_level} mL when {liquid_volume_input} L of liquid is poured."
            except Exception:
                context["error_message"] = f"The glass in row: {row} and position: {pos} is EMPTY when {liquid_volume_input} L of liquid is poured."

    return render(request, template, context)
