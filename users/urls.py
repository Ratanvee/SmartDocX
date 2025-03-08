from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import handler404
# from users.views import custom_404_view  # Import the custom view
from django.urls import path, include
from .views import register, login_view, user_logout, dashboard, upload_document, home
from .views import save_print_order, create_payment, verify_payment
# handler404 = custom_404_view
# from django.conf.urls import handler404
# from .views import custom_404
from django.conf.urls import handler404
from .views import custom_404_view  # Replace 'your_app' with your app name

handler404 = custom_404_view
# from .views import get_chart_data
# from .views import revenue_api, orders_api
from .views import print_document  # Import the new view
# handler404 = custom_404  # Set the custom 404 view



urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    # path('upload/<slug:unique_url>/', upload_document, name='upload_document'),
    path('pay/', create_payment, name='create_payment'),
    path('pay', create_payment, name='create_payment_no_slash'),  # Allow without a slash
    path('verify-payment/', verify_payment, name="verify_payment"),
    path("upload_document/", upload_document, name="upload_document"),  # Add this line
    path("upload/<slug:unique_url>/", upload_document, name="upload_document"),
    # path("print_order/", print_order, name="print_order"),
    # path("print_document/", print_document, name="print_document"),
    path("print-document/", print_document, name="print-document"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
