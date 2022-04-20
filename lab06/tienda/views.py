from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto

# Create your views here.
def index(request):
    product_list=Producto.objects.order_by('nombre')[:6]
    cat_list = Categoria.objects.all()
    context={'product_list': product_list,'cat_list':cat_list}
    return render(request, 'index.html', context)

def producto(request,producto_id):
    cat_list = Categoria.objects.all()
    producto = get_object_or_404(Producto,pk=producto_id)
    context={'producto': producto,'cat_list':cat_list}
    return render(request,'producto.html',context)

def categoria(request,categoria_id):
    cate=Producto.objects.filter(categoria_id=categoria_id)
    context={'cate': cate}
    return render(request,'categoria.html',context)