# ElementLab5

Creating REST API using Django REST Framework.

## Installation

### Installing requirements
``` 
pip install -r requirements.txt
```

### Applying migrations
```
python manage.py migrate
```

### Run server
```
python manage.py runserver 
```

## Usage

### Products

#### Get products list
> /api/products

#### Get product detail
> /api/products/1

### Categories

#### Get categories list
> /api/categories

#### Get category detail
> /api/categories/1

#### Get products of category
> /api/categories/1/products