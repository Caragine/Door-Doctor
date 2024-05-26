from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Review
from .forms import ReviewForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            send_mail('New Review Submitted', 'A new review has been submitted.', 'settings.EMAIL_HOST_USER',
            ['adam.caragine@hotmail.com'],
            html_message=render_to_string('review_email.html', context = {
                'name': review.name,
                'street': review.street,
                'city': review.city,
                'state': review.state,
                'zip_code': review.zip_code,
                'phone_number': review.phone_number,
                'review_text': review.review_text
            })
        )
            return render(request, 'reviews/thank_you.html')
        
    else:
        form = ReviewForm()
    return render(request, 'reviews/submit_review.html', {'form': form})

def review_list(request):
    reviews = Review.objects.filter(approved=True)
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def approve_review(request, review_id):
    review = Review.objects.get(id=review_id)
    review.approved = True
    review.save()
    return redirect('admin_review_list')

def admin_review_list(request):
    reviews = Review.objects.filter(approved=False)
    return render(request, 'reviews/admin_review_list.html', {'reviews': reviews})

def thank_you(request):
    return render(request, 'reviews/thank_you.html')
