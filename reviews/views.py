from django.http import HttpResponseRedirect

from django.shortcuts import render

from .forms import ReviewForm

from django.views import View

from django.views.generic.base import TemplateView

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request,"reviews/review.html",{
        "form" : form
    })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()

#     return render(request,"reviews/review.html",{
#         "form" : form
#     })


class ThankYouView(TemplateView):
    template_name = "reviews/thank-you.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context

# def thank_you(request):
#     return render(request, "reviews/thank-you.html")        