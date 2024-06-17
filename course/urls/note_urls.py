from django.urls import path

from course.views.note_views import (
    notes,
    note_list,
    add_note,
    edit_note,
    remove_note_confirmation,
    remove_note,
    detail_note,
)

urlpatterns = [
    path('notes/<int:id>/', notes, name='notes'),
    path('note_list/<int:id>/', note_list, name='note_list'),
    path('note/add/<int:id>/', add_note, name='add_note'),
    path('note/<int:pk>/edit', edit_note, name='edit_note'),
    path('note/<int:pk>/remove_confirmation',
         remove_note_confirmation, name='remove_note_confirmation'),
    path('note/<int:pk>/remove', remove_note, name='remove_note'),
    path('note/<int:pk>/detail', detail_note, name='detail_note'),
]
