from fastapi import APIRouter, HTTPException

from schema.product import Product, ProductCreate, products

product_router = APIRouter()



# create product
@product_router.post('/', status_code=201)
def create_product(payload: ProductCreate):
    # get the product id
    product_id = len(products) + 1
    new_product = Product(
        id=product_id,
        name=payload.name,
        price=payload.price,
        quantity_available=payload.quantity_available
    )
    products[product_id] = new_product
    return {'message': 'Product created successfully', 'data': new_product}


# list all products
@product_router.get('/', status_code=200)
def list_products():
    return {'message': 'success', 'data': products}


# Edit a product
@product_router.put('/{product_name}', status_code=200)
def edit_product(product_name: str, payload=ProductCreate):
    current_product = None

    #Get the current product
    for product in products:
        if product.name == product_name:
            current_product = product
        break
    if not current_product:
        raise HTTPException(status_code=404, detail="Product not found")
    current_product.price = payload.price
    current_product.quantity_available = payload.quantity_available
    return {'message': 'Product edited successfully', 'data': current_product}

    
