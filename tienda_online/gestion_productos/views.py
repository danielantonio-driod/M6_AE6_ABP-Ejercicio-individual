from django.shortcuts import render

# vista de gestión de productos.
def lista_productos(request):
    return render(request, 'gestion_productos/lista_productos.html')

def crear_producto(request):
    return render(request, 'gestion_productos/crear_producto.html') 

def detalle_producto(request, producto_id):
    return render(request, 'gestion_productos/detalle_producto.html', {'producto_id': producto_id})

def editar_producto(request, producto_id):
    return render(request, 'gestion_productos/editar_producto.html', {'producto_id': producto_id})

def eliminar_producto(request, producto_id):
    return render(request, 'gestion_productos/eliminar_producto.html', {'producto_id': producto_id})
