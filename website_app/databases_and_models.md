---
marp: true
style: |
  * { font-size: 1em; }
  .columns {
    display: flex;
  }
  .columns > * {
    flex: 1;
    padding: 0 1em;
  }
---

# Databases and Models in Django with PostgreSQL

---

## Introduction

In Django, the database is where your application's data is stored. Django uses an Object-Relational Mapping (ORM) system that allows you to interact with the database using Python code instead of raw SQL queries. The core component of this ORM is the **Model**.

A **Model** is a Python class that represents a database table. Each attribute of the class corresponds to a field in the table, and each instance of the class represents a row in the table.

---

## Why PostgreSQL?

PostgreSQL is a powerful, open-source relational database management system. It's known for its robustness, extensibility, and compliance with SQL standards. Django supports PostgreSQL out of the box, making it a great choice for Django applications.

---

## Setting Up PostgreSQL

Before connecting Django to PostgreSQL, you need to have PostgreSQL installed and running on your system.

### Installation

- **Windows**: Download and install from the [official PostgreSQL website](https://www.postgresql.org/download/windows/).
- **macOS**: Use Homebrew: `brew install postgresql`
- **Linux**: Use your package manager, e.g., `sudo apt-get install postgresql` on Ubuntu.
---
### Creating a Database

After installation, create a database for your Django project:

```sql
CREATE DATABASE your_database_name;
CREATE USER your_username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;
```

---

## Configuring Django to Use PostgreSQL

In your Django project's `settings.py` file, configure the database settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Installing psycopg2

Django needs the `psycopg2` library to connect to PostgreSQL. Install it using pip:

```bash
pip install psycopg2-binary
```

---

## Creating Models

<div class="columns">
<div>

Models are defined in your Django app's `models.py` file. Here's an example:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
```

</div>
<div>

### Field Types

Django provides various field types:
- `CharField`: For short text
- `TextField`: For long text
- `IntegerField`: For integers
- `DecimalField`: For decimal numbers
- `DateField`/`DateTimeField`: For dates and times
- `BooleanField`: For true/false values
- `ForeignKey`: For relationships between models
- `ManyToManyField`: For many-to-many relationships

</div>
</div>

---

## Migrations

Migrations are Django's way of propagating changes you make to your models into the database schema.

### Creating Migrations

After defining or changing models, create a migration:

```bash
python manage.py makemigrations
```

### Applying Migrations

Apply the migrations to update the database:

```bash
python manage.py migrate
```

---

## Using Models in Views

<div class="columns">
<div>

In your views, you can use the model classes to interact with the database:

```python
from django.shortcuts import render
from .models import Book, Author

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    books = author.book_set.all()
    return render(request, 'author_detail.html', {'author': author, 'books': books})
```

</div>
<div>

### Common Query Operations

- `Model.objects.all()`: Get all objects
- `Model.objects.get(id=1)`: Get a single object by ID
- `Model.objects.filter(field=value)`: Filter objects
- `Model.objects.create(field=value)`: Create a new object
- `object.save()`: Save changes to an object
- `Model.object.filter(id=1).delete()`: Delete an object
- `Model.object.filter(id=1).update()`: Update an object

</div>
</div>

---

## Admin Interface

Django provides a built-in admin interface for managing your models. To use it:

1. Register your models in `admin.py`:

```python
from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
```

2. Create a superuser:

```bash
python manage.py createsuperuser
```

3. Access the admin at `/admin/` in your browser.

---

## Best Practices

<div class="columns">
<div>

1. **Use meaningful names**: Choose descriptive names for your models and fields.
2. **Define relationships**: Use ForeignKey and ManyToManyField to represent relationships between models.
3. **Use migrations**: Always use Django's migration system to change your database schema.

</div>
<div>

4. **Validate data**: Use field validators and model validation to ensure data integrity.
5. **Index fields**: Add database indexes to frequently queried fields for better performance.
6. **Use select_related and prefetch_related**: Optimize queries when fetching related objects.

</div>
</div>

---

## Troubleshooting

<div class="columns">
<div>

### Connection Issues
- Ensure PostgreSQL is running
- Check your database credentials in `settings.py`
- Verify that the database exists and the user has permissions

</div>
<div>

### Migration Errors
- Check for syntax errors in your models
- Ensure all dependencies are installed
- Review migration files for conflicts

</div>
<div>

### Performance Issues
- Use `select_related()` for ForeignKey relationships
- Use `prefetch_related()` for ManyToMany relationships
- Add database indexes to frequently queried fields

</div>
</div>

---

This guide covers the basics of working with databases and models in Django using PostgreSQL. For more advanced topics, refer to the official Django documentation.