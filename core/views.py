from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.utils import timezone
from .models import Book, OrderBook, Order


def products(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, "products.html", context)


def checkout(request):
    return render(request, "checkout.html")


class HomeView(ListView):
    model = Book
    paginate_by = 10
    template_name = "home.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "product.html"


def add_to_cart(request, slug):
    book = get_object_or_404(Book, slug=slug)
    order_book, created = OrderBook.objects.get_or_create(
        book=book,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.books.filter(book__slug=book.slug).exists():
            order_book.quantity += 1
            order_book.save()
            messages.info(request, "Ilość książek została zaktualizowana.")
            return redirect("core:product", slug=slug)
        else:
            order.books.add(order_book)
            messages.info(request, "Książka została dodana do koszyka.")
            return redirect("core:product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.books.add(order_book)
        messages.info(request, "Książka została dodana do koszyka.")
        return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    book = get_object_or_404(Book, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.books.filter(book__slug=book.slug).exists():
            order_book = OrderBook.objects.filter(
                book=book,
                user=request.user,
                ordered=False
            )[0]
            order.books.remove(order_book)
            messages.info(request, "Książka została usunięta z koszyka.")
            return redirect("core:product", slug=slug)
        else:
            messages.info(request, "Książka nie była w twoim koszyku.")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "Nie masz aktywnego zamówienia.")
        return redirect("core:product", slug=slug)
