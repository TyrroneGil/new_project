---
marp: true
theme: default
paginate: true
---

# 🔐 Django Password Hashing & Change Guide

---

## 🧩 Password Hashing in Django

- Django hashes passwords automatically
- Default: **PBKDF2 + SHA256**
- Stored format:
```
algorithm$iterations$salt$hash
```

---

## ✅ Hashing with create_user()

```python
from django.contrib.auth.models import User

user = User.objects.create_user(
    username='john',
    password='mypassword123'
)
```

---

## ✅ Hashing with set_password()

```python
user = User(username='john')
user.set_password('mypassword123')
user.save()
```

---

## 🔍 Manual Hashing (Advanced)

```python
from django.contrib.auth.hashers import make_password, check_password

hashed = make_password('mypassword123')

check_password('mypassword123', hashed)
```

---

## ❌ Wrong Way

```python
user.password = 'mypassword123'
user.save()
```

🚨 Stores plain text password!

---



---
### 🔄 Change Password
## Backend

```python
from django.contrib.auth.models import User

user = User.objects.get(username='john')
user.set_password('new_password')
user.save()
```

---

## 🔐 With Old Password Check

```python
if user.check_password('old_password'):
    user.set_password('new_password')
    user.save()
```

---

## 🌐 Django View

```python
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
```

---

## 🔌 API (Django REST)

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class ChangePasswordView(APIView):
    def post(self, request):
        user = request.user

        if not user.check_password(request.data.get("old_password")):
            return Response({"error": "Wrong password"}, status=400)

        user.set_password(request.data.get("new_password"))
        user.save()

        return Response({"message": "Password updated"})
```

---

## 🛠️ Django Admin

- Go to Admin Panel
- Select user
- Click **Change password**

---

## 🔐 Best Practices

- Use `set_password()` or `create_user()`
- Never store plain text passwords
- Use HTTPS
- Enforce strong passwords
- Consider **Argon2**

---

## 🚀 Summary

| Feature | Method |
|--------|--------|
| Hash password | create_user(), set_password() |
| Verify password | check_password() |
| Change password | set_password() |
| API change | APIView |

---

# 🎉 Thank You
