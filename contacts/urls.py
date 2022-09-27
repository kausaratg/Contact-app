from django.urls import path
from contacts.views import ContactDetail, ContactList

urlpatterns = [
    path('', ContactList.as_view()),
    path('<int:id>', ContactDetail.as_view()),
]
