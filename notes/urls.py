from django.urls import path

from notes import views

urlpatterns = [
    path('', views.show_notes, name='notes'),
    path('<int:note_id>/', views.show_note, name='note'),
    path('save-note/', views.make_note, name="save-note"),
]
