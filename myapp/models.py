from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	city=models.CharField(max_length=100,default='gandhinagar')
	country=models.CharField(max_length=100,default="india")
	state=models.CharField(max_length=100,default="gujrat")
	pincode=models.IntegerField(default=360570)
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to="profile_pic/")
	usertype=models.CharField(max_length=100,default="user")

	def __str__(self):
		return self.fname +" - "+self.lname

class Billing(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	mobile=models.PositiveIntegerField()
	email=models.EmailField()
	city=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	country=models.CharField(max_length=100,default="india")
	state=models.CharField(max_length=100,default="gujrat")
	pincode=models.IntegerField()


	def __str__(self):
		return self.fname +" - "+self.lname


class Product(models.Model):
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_image=models.ImageField(upload_to="image/")
	product_company=models.CharField(max_length=100)
	product_name=models.CharField(max_length=100)
	product_price=models.PositiveIntegerField()
	product_size=models.PositiveIntegerField()
	product_category=models.CharField(max_length=100,default="other")
	product_genral_category=models.CharField(max_length=100,default="other")
	product_color=models.CharField(max_length=100,default="other")
	product_discription=models.TextField()
	product_discount=models.IntegerField(default=50)
	wishlist_flag=models.BooleanField(default=False)
	

	def __str__(self):
		return self.seller.fname+" - "+ self.product_category+" - "+self.product_name

class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.fname+" - "+self.product.product_name

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	product_qty=models.PositiveIntegerField()
	product_price=models.PositiveIntegerField()
	total_price=models.PositiveIntegerField()
	payment_status=models.BooleanField(default=False)


	def __str__(self):
		return self.user.fname+" - "+self.product.product_name

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', 
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	subject=models.CharField(max_length=100)
	message=models.TextField()

	def __str__(self):
		return self.name+" - "+self.subject