from django.shortcuts import render

# Create your views here.


def basket(request):
    """
    Renders the basket contents page
    """

    return render(request, 'basket/basket.html')