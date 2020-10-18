from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('',views.index, name="index"),
    path('books/',views.BookListView.as_view(), name="booklist"),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name="bookdetail"),
    path('books/authors/',views.AuthorListView.as_view(),name="authors"),
    path('books/<int:pk>/author/',views.AuthorDeatailView.as_view(),name="authorDetail"),
    path('books/borrowedbooks/',views.LoanedBooksByUser.as_view(), name="loanedbooks"),
    path('books/allborrowedbooks/',views.LoanedBooksByAll.as_view(), name="allloanedbooks"),
    path('books/<uuid:pk>/renewal/',views.renew_books, name="renew_book_librarian"),
    path('books/authorcreate/',views.AuthorCreateView.as_view(), name="authorcreate"),
    path('books/<int:pk>/authorupdate/',views.AuthorUpdateView.as_view(),name="authorupdate"),
    path('books/<int:pk>/authordelete/',views.AuthorDeleteView.as_view(), name="authordelete"),
    path('books/add/',views.BoookCreateView.as_view(),name="bookcreate"),
    path('books/<int:pk>/bookupp/',views.BoookUpdateView.as_view(), name="bookupdate"),
]