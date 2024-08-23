from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Review
from .forms import ReviewForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import os
import uuid
# Create your views here.

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.token = uuid.uuid4()
            review.save()
            print(review.token)
            send_review_email(review)
            return render(request, 'reviews/thank_you.html')
        
    else:
        form = ReviewForm()
    return render(request, 'reviews/submit_review.html', {'form': form})

def send_review_email(review):

    approve_url = reverse('reviews:approve_review', kwargs={'token': review.token})
    full_url = f"{settings.SITE_URL}{approve_url}"

    context = {
                'name': review.name,
                'street': review.street,
                'city': review.city,
                'state': review.state,
                'zip_code': review.zip_code,
                'phone_number': review.phone_number,
                'review_text': review.review_text,
                'token': review.token,
                'approve_url': full_url,
            }
    
    send_mail('New Review Submitted', 'A new review has been submitted.', os.getenv('EMAIL_HOST_USER'),
            ['nydoordoctor@hotmail.com'],
            html_message=render_to_string('reviews/review_email.html', context), fail_silently=False,)

def approve_review(request, token):
    review = get_object_or_404(Review, token=token)
    review.approved = True
    review.save()
    return redirect('reviews:review_list')

def review_list(request):
    reviews = Review.objects.filter(approved=True)
    processed_reviews = []

    for review in reviews:
        full_name = review.name
        name_parts = full_name.split()
        first_name = name_parts[0]
        last_initial = name_parts[1][0] if len(name_parts) > 1 else ''
        processed_reviews.append({'first_name': first_name, 
                                'last_initial': last_initial,
                                'city': review.city,
                                'state': review.state,
                                'review_text': review.review_text,
                                'created_at': review.created_at})

    return render(request, 'reviews/review_list.html', {'reviews': processed_reviews})

def thank_you(request):
    return render(request, 'reviews/thank_you.html')
