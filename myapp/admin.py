from django.contrib import admin
from .models import User,Product,Wishlist,Cart,Billing,Contact,Transaction
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Billing)
admin.site.register(Contact)
admin.site.register(Transaction)
