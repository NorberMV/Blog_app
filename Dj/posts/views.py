
"""Posts views."""

# Django
#from django.shortcuts import render
from django.shortcuts import render

# Utilities
from datetime import datetime

# Lists of dictionaries with the posts
posts = [
    {
        'title': 'Coveñas',
        'user': {
            'name': 'Deisy Posada',
            'picture': 'https://i.ibb.co/2qDS85H/dey.png'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.ibb.co/9p8K5yV/Dey-Cove-as.png',
    },
    {
        'title': 'Cyberpunk android by Jeronimo Garces',
        'user': {
            'name': 'Norberto Moreno V.',
            'picture': 'https://i.ibb.co/V2SmTmJ/Norber-Cyber-Punk.jpg'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.ibb.co/VJ66RyY/Whats-App-Image-2021-01-12-at-2-55-33-PM.jpg',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

def list_posts(request):

    """List existing posts"""
    return render(request, 'feed.html', {'posts':posts})