"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from decorator_include import decorator_include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transaction/', decorator_include(login_required,include("transaction.urls"))),
    path('account/', decorator_include(login_required,include("account.urls"))),
    path('balance/sheet/', decorator_include(login_required,include("balance_sheet.urls"))),
    path('items/', decorator_include(login_required,include('items.urls'))),
    path('supplier/', decorator_include(login_required,include('supplier.urls'))),
    path('sales/', decorator_include(login_required,include('sales.urls'))),
    path('purchase/', decorator_include(login_required,include('purchase.urls'))),
    path('employee/', decorator_include(login_required,include('employee.urls'))),
    path('salary/', decorator_include(login_required,include('salary.urls'))),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
