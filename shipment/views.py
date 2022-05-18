from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from shipment.widgets_values import WidgetValues

# from .forms import WidgetsForm
from .models import Shipment


@login_required
def check_widget(request):
    # if request.method == "POST":
    #     form = WidgetsForm(request.POST, instance=request.user)
    #     if form.is_valid():
    #         form.save()
    #         widgets = form.cleaned_data.get("widgets")
    #         messages.success(request, f"Widget set to {widgets}!")
    context = {}
    # form = WidgetsForm
    # context["form"] = form
    supplier = request.user.is_supplier
    if not supplier:
        print("customer")
        shipments = Shipment.objects.filter(customer=request.user).prefetch_related()
        context["shipments"] = shipments
    else:
        shipments = Shipment.objects.filter(supplier=request.user).prefetch_related()
        context["shipments"] = shipments

    # widgets = str(request.user.widgets)
    # if widgets == "Charts":
    #     widgetvalue = WidgetValues.Charts.value
    #     context["value"] = widgetvalue
    # elif widgets == "Info":
    #     widgetvalue = WidgetValues.Info.value
    #     context["value"] = widgetvalue
    # elif widgets == "Lists":
    #     widgetvalue = WidgetValues.Lists.value
    #     context["value"] = widgetvalue
    # elif widgets == "Statistics":
    #     widgetvalue = WidgetValues.Statistics.value
    #     context["value"] = widgetvalue
    # else:
    #     context["value"] = "none"
    return render(request, "shipment/home.html", context)


def about(request):
    return render(request, "shipment/about.html")
