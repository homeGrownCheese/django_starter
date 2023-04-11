# Django Starter

A basic Django project template that includes user registration, login, logout, and password reset.

If using the database caching
```
./manage createcachetable
```
Otherwise comment out in settings.py
``` py
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache_table",
    }
}
```