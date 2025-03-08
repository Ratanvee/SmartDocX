# from django.db import models

# class UploadForm(models.Model):
#     PAPER_SIZES = [
#         ('A4', 'A4'), ('A3', 'A3'), ('Letter', 'Letter'), ('Legal', 'Legal')
#     ]
#     PAPER_TYPES = [
#         ('Standard', 'Standard'), ('Premium', 'Premium'), ('Glossy', 'Glossy'), ('Matte', 'Matte')
#     ]
#     PRINT_COLORS = [
#         ('Black & White', 'Black & White'), ('Color', 'Color')
#     ]
#     PRINT_SIDES = [
#         ('One Side', 'One Side'), ('Both Sides', 'Both Sides')
#     ]
#     BINDING_TYPES = [
#         ('Staple', 'Staple'), ('Spiral Binding', 'Spiral Binding'), ('Hardcover Binding', 'Hardcover Binding')
#     ]

#     owner_id = models.IntegerField()
#     order_id = models.CharField(max_length=50, unique=True)
#     file_path = models.FileField(upload_to='uploads/')
#     paper_size = models.CharField(max_length=10, choices=PAPER_SIZES, default='A4')
#     paper_type = models.CharField(max_length=10, choices=PAPER_TYPES, default='Standard')
#     print_color = models.CharField(max_length=15, choices=PRINT_COLORS, default='Black & White')
#     print_sides = models.CharField(max_length=10, choices=PRINT_SIDES, default='One Side')
#     binding = models.CharField(max_length=20, choices=BINDING_TYPES, default='Staple')
#     no_of_copies = models.PositiveIntegerField(default=1)
#     payment_rupee = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_id = models.CharField(max_length=50, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     no_of_documents = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"Order {self.order_id} by {self.owner_id}"

# class UserLogin(models.Model):
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     owner_id = models.AutoField(primary_key=True)

#     def __str__(self):
#         return self.username

# class OrderComplete(models.Model):
#     STATUS_CHOICES = [
#         ('Pending', 'Pending'), ('Process', 'Process'), ('Failed', 'Failed'), ('Complete', 'Complete')
#     ]

#     owner_id = models.IntegerField()
#     document_path = models.FileField(upload_to='completed_orders/')
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
#     create_time = models.DateTimeField(auto_now_add=True)
#     no_of_pages = models.PositiveIntegerField()

#     def __str__(self):
#         return f"Order for {self.owner_id} - {self.status}"

# class ShopDetails(models.Model):
#     shop_id = models.AutoField(primary_key=True)
#     shop_email = models.EmailField(unique=True)
#     shop_name = models.CharField(max_length=100)
#     shop_phone = models.CharField(max_length=15)
#     shop_address = models.TextField()
#     currency = models.CharField(max_length=10, default='INR')
#     owner_id = models.IntegerField()
#     owner_account_no = models.CharField(max_length=50)
#     price_bw_page = models.DecimalField(max_digits=10, decimal_places=2)
#     price_color_page = models.DecimalField(max_digits=10, decimal_places=2)
#     price_spiral_binding = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     price_hardcover_binding = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     double_side_price = models.DecimalField(max_digits=10, decimal_places=2)
#     single_side_price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.shop_name

# class OwnerPaymentDone(models.Model):
#     PAYMENT_CHOICES = [
#         ('Yes', 'Yes'), ('No', 'No')
#     ]

#     owner_id = models.IntegerField()
#     send_money_to_owner = models.CharField(max_length=3, choices=PAYMENT_CHOICES, default='No')
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Payment to {self.owner_id}: {self.send_money_to_owner}"




# # this is temporary file
# # Compare this snippet from users/views.py:

# # class UploadedFile(models.Model):
# #     file = models.FileField(upload_to="documents/")
# #     uploaded_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return self.file.name
    


# from django.db import models

# class UploadedFile(models.Model):
#     file = models.FileField(upload_to="uploads/")
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.file.name

# class Order(models.Model):
#     file_url = models.CharField(max_length=500)  # Store uploaded file path
#     paper_size = models.CharField(max_length=50, choices=[
#         ("a4", "A4 (210 × 297 mm)"),
#         ("letter", "Letter (8.5 × 11 in)"),
#         ("legal", "Legal (8.5 × 14 in)"),
#         ("a3", "A3 (297 × 420 mm)"),
#     ])
#     paper_type = models.CharField(max_length=50, choices=[
#         ("standard", "Standard (80 gsm)"),
#         ("premium", "Premium (100 gsm)"),
#         ("glossy", "Glossy (120 gsm)"),
#         ("matte", "Matte (120 gsm)"),
#     ])
#     print_color = models.CharField(max_length=20, choices=[
#         ("bw", "Black & White"),
#         ("color", "Color"),
#     ])
#     print_sides = models.CharField(max_length=20, choices=[
#         ("single", "Single-sided"),
#         ("double", "Double-sided"),
#     ])
#     binding = models.CharField(max_length=50, choices=[
#         ("none", "None"),
#         ("staple", "Staple"),
#         ("spiral", "Spiral Binding"),
#         ("hardcover", "Hardcover Binding"),
#     ], default="none")
#     copies = models.PositiveIntegerField(default=1)
#     order_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order {self.id} - {self.file_url}"





# # from django.db import models

# # class PrintOrder(models.Model):
# #     file = models.FileField(upload_to="uploads/")
# #     paper_size = models.CharField(max_length=20)
# #     paper_type = models.CharField(max_length=20)
# #     print_color = models.CharField(max_length=10)
# #     print_sides = models.CharField(max_length=10)
# #     binding = models.CharField(max_length=20)
# #     copies = models.IntegerField(default=1)
# #     created_at = models.DateTimeField(auto_now_add=True)


from django.contrib.auth import login  # Ensure this import is correct

from django.db import models

class Payment(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    payment_id = models.CharField(max_length=100, unique=True)
    signature = models.CharField(max_length=200)
    amount = models.IntegerField()
    currency = models.CharField(max_length=10, default="INR")
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.status}"
    





from django.db import models

class UploadedDocument(models.Model):
    file = models.FileField(upload_to="uploads/")  # File will be stored in media/uploads/
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Auto set upload time

from django.utils.timezone import now  # Import now()

from django.db import models
from django.utils import timezone


class PrintOrder(models.Model):
    unique_url = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    page_size = models.CharField(max_length=50)
    paper_type = models.CharField(max_length=50)
    print_color = models.CharField(max_length=50)
    print_sides = models.CharField(max_length=50)
    binding = models.CharField(max_length=50)
    copies = models.PositiveIntegerField()
    transaction_id = models.CharField(max_length=100)
    total_pages = models.PositiveIntegerField(default=1)
    order_id = models.CharField(max_length=100, unique=True)
    # created_at = models.DateTimeField(auto_now_add=True)  # Remove default
    # ✅ New field for storing the uploaded document
    order_time = models.DateTimeField(default=timezone.now)  # Use timezone-aware default

    document = models.FileField(upload_to="user_uploads/", null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - {self.unique_url}"

import uuid
from django.contrib.auth.models import AbstractUser
# from djongo import models  # Use djongo's models for MongoDB compatibility
from django.db import models

import uuid
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    unique_url = models.CharField(max_length=255, unique=True, blank=True, null=True)
    total_orders = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_customers = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)  # Ensure it's an integer, not an ObjectId

    # Fix conflicting reverse accessors
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Unique related name to prevent conflicts
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Unique related name to prevent conflicts
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.unique_url:  # Generate only if empty
            base_url = self.username.lower().replace(" ", "-")
            unique_part = str(uuid.uuid4())[:8]
            self.unique_url = f"{base_url}-{unique_part}"

            # Ensure uniqueness in the database
            while CustomUser.objects.filter(unique_url=self.unique_url).exists():
                unique_part = str(uuid.uuid4())[:8]
                self.unique_url = f"{base_url}-{unique_part}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
