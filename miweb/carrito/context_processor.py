

def importe_total_carro(request):
    total=0
    cantidad_productos = 0 
    
    
    
    if request.user.is_authenticated:
        if 'carrito' in request.session: 
            for key, value in request.session["carrito"].items():
                total=total+(int(value["precio"]))
                cantidad_productos += value["cantidad"]
    return {"importe_total_carro":total, "cantidad_productos": cantidad_productos}


