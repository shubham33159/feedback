from django.http import HttpResponseRedirect

from django.shortcuts import render

from .forms import ReviewForm

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from reviews.models import Review

# Create your views here.

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

### Class View ####
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request,"reviews/review.html",{
#         "form" : form
#     })

#     def post(self, request):
#         print("Inside Post")
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
        
#         return render(request,"reviews/review.html",{
#         "form" : form
#     })


### Form View ####
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

### Create View ###
class ReviewView(CreateView):
    template_name = "reviews/review.html"
    models = Review
    form_class = ReviewForm
    success_url = "/thank-you"

    

class ThankYouView(TemplateView):
    template_name = "reviews/thank-you.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context

# def thank_you(request):
#     return render(request, "reviews/thank-you.html")      


# class ReviewListView(TemplateView):
#     template_name = "reviews/review-list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewListView(ListView):
    template_name = "reviews/review-list.html"
    model = Review
    context_object_name = "reviews"
    
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gte=4)
        return data
    
# class SingleReviewView(TemplateView):
#     template_name = "reviews/single-review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context


## Detail View
class SingleReviewView(DetailView):
    template_name = "reviews/single-review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # review_id = self.kwargs["pk"]
        # loaded_review = Review.objects.get(id=review_id)

        loaded_review = self.object     # alternative of above 2 lines
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context



    

class AddFavorite(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)

