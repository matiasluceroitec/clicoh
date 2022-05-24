# Test Clicoh

<a href="#"><img src="https://img.shields.io/badge/Dajango-4.0.4-yellow"></a>
<a href="#"><img src="https://img.shields.io/badge/djangorestframework-3.13.1-yellowgreen"></a>

## Install Project

### - Clone this repository 
### - Create a virtual enviorment
### - run `pip install -r requirements.txt`

## Run the Project

### run `python clicoh/manage.py migrate`
### run `python clicoh/manage.py runserver`

## Endpoints

### Get all Products
`localhost:8000/products/products`
### Get a Products
`localhost:8000/products/products/<id>`
### Post a product
Post --> `localhost:8000/products/products`

```
data = {
    "id": String,
    "name": String,
    "price": Decimal,
    "stock": Integer
}
```

### Patch stock a product 
Patch --> `localhost:8000/products/products/<id>`

```
data = {
    "stock" : Integer
}
```

### Get all Order
`localhost:8000/products/orders/`

### Get all OrderDetail
`localhost:8000/products/ordersdetail/`

```
No llegue a :
- Finalizar el Readme
- Actualizar una orden y sus detalles
- Deploye en Heroku pero lanza un error de distribucion de python que no pude solucionar
- Agregar todos los tests
```