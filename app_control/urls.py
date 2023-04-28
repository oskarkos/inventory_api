from django.urls import path, include
from .views import (
    DianResolutionView, InventoryView, ShopView, SummaryView, InvoiceView, PurchaseView, SaleByShopView,
    InventoryGroupView, SalePerformance, InventoryCSVLoaderView, UpdateInvoiceView
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register('inventory', InventoryView, "inventory")
router.register('inventory-csv', InventoryCSVLoaderView, "inventory-csv")
router.register('shop', ShopView, "shop")
router.register('summary', SummaryView, "summary")
router.register('purchase-summary', PurchaseView, "purchase-summary")
router.register('sales-by-shop', SaleByShopView, "sales-by-shop")
router.register('group', InventoryGroupView, "group")
router.register('top-selling', SalePerformance, "top-selling")
router.register('invoice', InvoiceView, "invoice")
router.register('dian-resolution', DianResolutionView, "dian-resolution")


urlpatterns = [
    path("", include(router.urls)),
    path('update-invoice/<str:invoice_number>/',
         UpdateInvoiceView.as_view(), name='update-invoice')
]
