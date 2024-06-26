from django.urls import path

from course.views.note_views import (
    NoteList,
    NoteCreate,
    NoteUpdate,
    NoteDelete,
)

urlpatterns = [
    path('notes/<int:course_id>/', NoteList.as_view(), name='note-list'),
    path('note/create/<int:course_id>/',
         NoteCreate.as_view(), name='note-create'),
    path('note/update/<int:course_id>/<int:pk>/',
         NoteUpdate.as_view(), name='note-update'),
    path('note/delete/<int:course_id>/<int:pk>/',
         NoteDelete.as_view(), name='note-delete'),
]
