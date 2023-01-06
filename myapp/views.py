from django.shortcuts import render,redirect
from .models import User,Product,Wishlist,Cart,Billing,Contact,Transaction
import random
from django.conf import settings
from django.core.mail import send_mail
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



# Create your views here.
def validate_login(request):
	email=request.GET.get('email')
	data={
		'is_taken':User.objects.filter(email__iexact=email).exists()		
	}
	return JsonResponse(data)
def validate_mobile(request):
	mobile=request.GET.get('mobile')
	data={
		'is_taken':User.objects.filter(mobile__iexact=mobile).exists()		
	}
	return JsonResponse(data)
def index(request):
	product=Product.objects.all()
	
	try:
		user=User.objects.get(email=request.session['email'])
		if user.usertype == 'user':
			wishlists=Wishlist.objects.filter(user=user)
			pw=[]
			for i in wishlists:
				pw.append(i.product)

			carts=Cart.objects.filter(user=user,payment_status=False)
			pc=[]
			for i in carts:
				pc.append(i.product)

			return render(request,"index.html",{'product':product,'pw':pw,'pc':pc,'carts':carts})
		else:
			return render(request,"seller_index.html",{'product':product})
	except:
		return render(request,"index.html",{'product':product})

	

def seller_index(request):
	user=User.objects.get(email=request.session['email'])
	product=Product.objects.all()
	return render(request,"seller_index.html",{'product':product})

def about(request):
	return render(request,"about.html")

def cart(request):
	carts=Cart.objects.filter(user=user,payment_status=False)
	return render(request,"cart.html",{'carts':carts})

def checkout(request):
	carts=Cart.objects.filter(user=user,payment_status=False)
	return render(request,"checkout.html",{'carts':carts})

def contact_us(request):
	try:

		user=User.objects.get(email=request.session['email'])
		carts=Cart.objects.filter(user=user,payment_status=False)
		if request.method=="POST":
			user.name=request.POST['name']
			user.email=request.POST['email']
			user.subject=request.POST['subject']
			user.message=request.POST['message']
			Contact.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				subject=request.POST['subject'],
				message=request.POST['message']
				)
			msg="Your Contact Sand Successfuly"
			return render(request,"contact-us.html",{'msg':msg,'user':user,'carts':carts})
		else:
			return render(request,"contact-us.html",{'user':user,'carts':carts})
	except:
		return render(request,"contact-us.html")
def my_account(request):
	try:
		user=User.objects.get(email=request.session['email'])
		carts=Cart.objects.filter(user=user,payment_status=False)

		return render(request,"my-account.html",{'carts':carts})
	except:
		return render(request,"my-account.html")
def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				product=Product.objects.all()
				if user.usertype=="user":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					wishlists=Wishlist.objects.filter(user=user)
					request.session['wishlist_count']=len(wishlists)
					carts=Cart.objects.filter(user=user,payment_status=False)
					request.session['cart_count']=len(carts)
					subtotal=0
					for i in carts:
						subtotal=subtotal+i.total_price
					request.session['subtotal']=int(subtotal)
					return redirect('index')
				else:
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					product=Product.objects.all()
					return redirect("seller_index.html")

			else:
				msg1="Password Is Incorrect "
				return render(request,"my-account.html",{'msg1':msg1})
		except:
			msg1="Email Is Incorrect"
			return render(request,"my-account.html",{'msg1':msg1})
	else:
		return render(request,"my-account.html")

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_pic']
		del request.session['wishlist_count']
		del request.session['cart_count']
		del request.session['subtotal']
		return render(request,"my-account.html")
	except:
		return render(request,"my-account.html")

def signup(request):
	try:
		if request.method=="POST":
			user=User()
			user.fname=request.POST['fname']
			user.lname=request.POST['lname']
			user.email=request.POST['email']
			user.mobile=request.POST['mobile']
			user.address=request.POST['address']
			try:
				User.objects.get(email=request.POST['email'])
				msg="Email Alredy Resister"
				return render(request,"my-account.html",{'msg':msg,'user':user})
			except:
				try:
					User.objects.get(mobile=request.POST['mobile'])
					msg="Mobile Number Alredy Resister"
					return render(request,"my-account.html",{'msg':msg,'user':user})
				except:
					if request.POST['password']==request.POST['cpassword']:

						User.objects.create(
							fname=request.POST['fname'],
							lname=request.POST['lname'],
							email=request.POST['email'],
							mobile=request.POST['mobile'],
							address=request.POST['address'],
							password=request.POST['password'],
							profile_pic=request.FILES['profile_pic'],
							usertype=request.POST['usertype']
							)
						msg="Your Account Create  Successfuly"
						return render(request,"my-account.html",{'msg':msg})
					else:
						msg="Password & Confrim Password Does not Matched"
						return render(request,"my-account.html",{'msg':msg,'user':user})
		else:
			return render(request,"my-account.html")
	except:
		msg_error="Please Fill All Blank"
		return render(request,"my-account.html",{'msg_error':msg_error,'user':user})

def profile(request):
	user=User.objects.get(email=request.session['email'])
	try:
		carts=Cart.objects.filter(user=user,payment_status=False)
		if request.method=="POST":
			user.fname=request.POST['fname']
			user.lname=request.POST['lname']
			user.mobile=request.POST['mobile']
			user.email=request.POST['email']
			user.address=request.POST['address']
			try:
				user.profile_pic=request.FILES['profile_pic']
			except:
				pass
			user.save()
			msg="Your Profile Update Successfuly"
			request.session['fname']=user.fname
			request.session['lname']=user.lname
			request.session['mobile']=user.mobile
			request.session['address']=user.address
			request.session['profile_pic']=user.profile_pic.url
			carts=Cart.objects.filter(user=user,payment_status=False)

			return render(request,"my-account.html",{'msg':msg,'user':user,'carts':carts})
		else:
			return render(request,"my-account.html",{'user':user,'carts':carts})
	except:
		msg="Please Fill All Blank"
		return render(request,"my-account.html",{'user':user,'msg':msg})

def seller_edit_profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.email=request.POST['email']
		user.address=request.POST['address']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		msg="Your Profile Update Successfuly"
		request.session['fname']=user.fname
		request.session['lname']=user.lname
		request.session['mobile']=user.mobile
		request.session['address']=user.address
		request.session['profile_pic']=user.profile_pic.url
		return render(request,"seller_edit_profile.html",{'msg':msg,'user':user})
	else:
		return render(request,"seller_edit_profile.html",{'user':user})



def change_password(request):
	user=User.objects.get(email=request.session['email'])

	carts=Cart.objects.filter(user=user,payment_status=False)
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				msg1="Your Password Changed Successfuly"
				subject = 'Change Your Password'			
				message = 'Dear, '+user.fname+" "+user.lname+",\n Your Password has been Change Successfuly!! \n New Password: "+str(user.password) +"\n Your UserName: "+user.email+"\n Don't Share any one Your  Password and usernam\n \n !!!Thank You!!!"
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [user.email, ]
				send_mail( subject, message, email_from, recipient_list )
				return render(request,"my-account.html",{'msg1':msg1,'carts':carts})
			else:
				msg1="New Password & Confrim New Password Does Not Matched"
				return render(request,"my-account.html",{'msg1':msg1,'carts':carts})
		else:
			msg1="Old Password Does Not Matched"
			return render(request,"my-account.html",{'msg1':msg1,'carts':carts})
	else:
		return render(request,"my-account.html",{'carts':carts})


def seller_chenge_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				msg1="Your Password Changed Successfuly"
				subject = 'Change Your Password'			
				message = 'Dear, '+user.fname+" "+user.lname+",\n Your Password has been Change Successfuly!! \n New Password: "+str(user.password) +"\n Your UserName: "+user.email+"\n Don't Share any one Your  Password and usernam\n \n !!!Thank You!!!"
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [user.email, ]
				send_mail( subject, message, email_from, recipient_list )
				return render(request,"seller_chenge_password.html",{'msg1':msg1})
			else:
				msg1="New Password & Confrim New Password Does Not Matched"
				return render(request,"seller_chenge_password.html",{'msg1':msg1})
		else:
			msg1="Old Password Does Not Matched"
			return render(request,"seller_chenge_password.html",{'msg1':msg1})
	else:
		return render(request,"seller_chenge_password.html")



def forgote_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP For Forgote Password'			
			message = 'Dear, '+user.fname+" "+user.lname+",\n You have reqquested for a new password.\nOTP: "+str(otp) +"\n Don't Share any one Your OTP and Password \n Thank You"
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			msg="Sent OTP"

			return render(request,"otp.html",{'msg':msg,'otp':otp,'email':user.email})
		except:
			msg="Email Not Resitered"
			return render(request,"forgote_password.html",{'msg':msg})
	else:
		
		return render(request,"forgote_password.html")

def otp(request):
	email=request.POST['email']
	otp=request.POST['otp']
	uotp=request.POST['uotp']
	if otp==uotp:
		return render(request,"new_password.html",{'email':email})

	else:
		msg="Your OTP Does Not Matched"
		return render(request,"otp.html",{'msg':msg,'otp':otp,'email':email})

def new_password(request):
	email=request.POST['email']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']
	if np==cnp:
		user=User.objects.get(email=email)
		if user.password==np:
			msg1="Sorry You Do Not Use Your Old Password"
			return render(request,"new_password.html",{'msg1':msg1,'email':email})
		else:
			user.password=np
			user.save()
			msg1="Your Password Change Successfuly"
			return render(request,"my-account.html",{'msg1':msg1})
	else:
		msg1="Your New Password & Confrim New Password Does Not Matched"
		return render(request,"new_password.html",{'msg1':msg1,'email':email})

	return render(request,"new_password.html")
def service(request):
	return render(request,"service.html")

def shop_detail(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	product=Product.objects.filter
	return render(request,"shop-detail.html",{'carts':carts})

def shop(request):
	try:
		user=User.objects.get(email=request.session['email'])
		product=Product.objects.all()
		carts=Cart.objects.filter(user=user,payment_status=False)

		delete=0
		for i in product:
			delete=i.product_discount
	
		return render(request,"shop.html",{'product':product,'delete':delete,'carts':carts})

	except:
		product=Product.objects.all()

		delete=0
		for i in product:
			delete=i.product_discount
	
		return render(request,"shop.html",{'product':product,'delete':delete})

	

def wishlist(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	return render(request,"wishlist.html",{'carts':carts})

def add_product(request):
	if request.method=="POST":
		seller=User.objects.get(email=request.session["email"])
		Product.objects.create(
			seller=seller,
			product_image=request.FILES['product_image'],
			product_company=request.POST['product_company'].lower(),
			product_name=request.POST['product_name'],
			product_price=request.POST['product_price'],
			product_size=request.POST['product_size'],
			product_category=request.POST['product_category'],
			product_genral_category=request.POST['product_genral_category'],
			product_discription=request.POST['product_discription']
			)
		msg="Your Product Add Successfuly"
		return render(request,"add_product.html",{'msg':msg})
	else:
		return render(request,"add_product.html")

def view_product(request):
	seller=User.objects.get(email=request.session['email'])
	products=Product.objects.filter(seller=seller)
	return render(request,"view_product.html",{'products':products})

def detail_product(request,pk):
	product=Product.objects.get(pk=pk)
	return render(request,"detail_product.html",{'product':product})



def edit_product(request,pk):
	product=Product.objects.get(pk=pk)
	if request.method=="POST":
		product.product_company=request.POST['product_company'].lower()
		product.product_name=request.POST['product_name']
		product.product_price=request.POST['product_price']
		product.product_size=request.POST['product_size']
		product.product_category=request.POST['product_category']
		product.product_genral_category=request.POST['product_genral_category']
		product.product_color=request.POST['product_color']
		product.product_discription=request.POST['product_discription']
		try:
			product.product_image=request.FILES['product_image']
		except:
			pass
		product.save()
		msg="Your Product Update Successfuly"
		return render(request,"edit_product.html",{'product':product,'msg':msg})
	else:
		return render(request,"edit_product.html",{'product':product})

def delete_product(request,pk):
	product=Product.objects.get(pk=pk)
	product.delete()
	# msg="Your Product Delete Successfuly"
	# return render(request,"view_product.html",{'msg':msg})
	return redirect(view_product)

def all(request):
	product=Product.objects.all()
	return render(request,"detail_product",{'product':product})

def buyer_product_detail(request,pk):
	try:
		wishlist_flag=False
		cart_flag=False
		product=Product.objects.get(pk=pk)
		delete=product.product_price+product.product_discount
		try:
			user=User.objects.get(email=request.session['email'])
			Wishlist.objects.get(user=user,product=product)
			wishlist_flag=True
		except:
			pass
		try:
			user=User.objects.get(email=request.session['email'])
			Cart.objects.get(user=user,product=product,payment_status=False)
			cart_flag=True
		except:
			pass
		user=User.objects.get(email=request.session['email'])
		products=Product.objects.all()
		wishlists=Wishlist.objects.filter(user=user)
		pw=[]
		for i in wishlists:
			pw.append(i.product)

		carts=Cart.objects.filter(user=user)
		pc=[]
		for i in carts:
			pc.append(i.product)
		carts=Cart.objects.filter(user=user,payment_status=False)
		return render(request,"buyer_product_detail.html",{'carts':carts,'pw':pw,'pc':pc,'products':products,'user':user,'product':product,'delete':delete,'wishlist_flag':wishlist_flag,'cart_flag':cart_flag})


	except:
		products=Product.objects.all()
		product=Product.objects.get(pk=pk)
		delete=product.product_price+product.product_discount
		return render(request,"buyer_product_detail.html",{'products':products,'product':product,'delete':delete})

def add_to_wishlist(request,pk):
	user=User.objects.get(email=request.session['email'])
	product=Product.objects.get(pk=pk)
	Wishlist.objects.create(user=user,product=product)
	return redirect('show_wishlist')

def show_wishlist(request):
	user=User.objects.get(email=request.session['email'])
	wishlists=Wishlist.objects.filter(user=user)
	wishlist_lenth=len(wishlists)
	request.session['wishlist_count']=len(wishlists)
	carts=Cart.objects.filter(user=user,payment_status=False)

	return render(request,"wishlist.html",{'wishlists':wishlists,'wishlist_lenth':wishlist_lenth,'carts':carts})

def remove_from_wishlist(request,pk):
	user=User.objects.get(email=request.session['email'])
	product=Product.objects.get(pk=pk)
	wishlist=Wishlist.objects.get(user=user,product=product)
	wishlist.delete()
	return redirect('show_wishlist')

def add_to_cart(request,pk):
	user=User.objects.get(email=request.session['email'])
	product=Product.objects.get(pk=pk)
	Cart.objects.create(user=user,product=product,product_qty=1,
		product_price=product.product_price,
		total_price=product.product_price
		)
	return redirect('cart')

def cart(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	cart_length=len(carts)
	subtotal=0
	for i in carts:
		subtotal=subtotal+i.product.product_price*i.product_qty
	shiping=0
	discount=0
	if subtotal < 1000:
		discount=0
		msg="No Discount"
	elif subtotal <5000:
		discount=5
		msg="5% Discount"
	elif subtotal <10000:
		discount=10
		msg="10% Discount"
	elif subtotal <20000:
		discount=12
		msg="12% Discount"
	elif subtotal <25000:
		discount=15
		msg="15% Discount"
	else:
		discount=20
		msg="20% Discount"
	discount=(subtotal*discount)/100
	tax=2
	tax1=(subtotal*2)/100
	total=subtotal+tax-discount-shiping
	request.session['cart_count']=len(carts)
	return render(request,"cart.html",{'cart_length':cart_length,'carts':carts,'subtotal':subtotal,'discount':discount,'tax':tax,'total':total})

def change_qty(request,pk):
	cart=Cart.objects.get(pk=pk)
	product_qty=int(request.POST['product_qty'])
	cart.product_qty=product_qty
	cart.total_price=cart.product_price*product_qty
	cart.save()
	return redirect('cart')

def checkout(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	subtotal=0
	for i in carts:
		subtotal=subtotal+i.product.product_price*i.product_qty
		shiping=0
		discount=0
		if subtotal < 1000:
			discount=0
			msg="No Discount"
		elif subtotal <5000:
			discount=5
			msg="5% Discount"
		elif subtotal <10000:
			discount=10
			msg="10% Discount"
		elif subtotal <20000:
			discount=12
			msg="12% Discount"
		elif subtotal <25000:
			discount=15
			msg="15% Discount"
		else:
			discount=20
			msg="20% Discount"
		discount=(subtotal*discount)/100
		tax=2
		tax1=(subtotal*2)/100
		total=int(subtotal+tax-discount-shiping)
	return render(request,"checkout.html",{'user':user,'tax':tax,'carts':carts,'subtotal':subtotal,'discount':discount,'total':total,'msg':msg})

def shipping_method(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user)
	subtotal=0
	for i in carts:
		subtotal=subtotal+i.product.product_price*i.product_qty
		shiping=0
		discount=0
		if subtotal < 1000:
			discount=0
			msg="No Discount"
		elif subtotal <5000:
			discount=5
			msg="5% Discount"
		elif subtotal <10000:
			discount=10
			msg="10% Discount"
		elif subtotal <20000:
			discount=12
			msg="12% Discount"
		elif subtotal <25000:
			discount=15
			msg="15% Discount"
		else:
			discount=20
			msg="20% Discount"
		discount=(subtotal*discount)/100
		tax=(subtotal*2)/100
		shiping1=0
		shiping2=10
		shiping3=20

		if shipping3==request.POST['shiping1']:
			total=subtotal+20+tax-discount-shiping
		elif shiping2==request.POST['shiping2']:
			total=subtotal+10+tax-discount-shiping
		else:
			total=subtotal+tax-discount-shiping

	return render(request,"checkout.html",{'tax':tax,'carts':carts,'subtotal':subtotal,'discount':discount,'total':total,'msg':msg})

def remove_from_cart(request,pk):
	user=User.objects.get(email=request.session['email'])
	product=Product.objects.get(pk=pk)
	cart=Cart.objects.get(user=user,product=product)
	cart.delete()
	return redirect('cart')

def billing_address(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.city=request.POST['city']
		user.address=request.POST['address']
		user.country=request.POST['country']
		user.state=request.POST['state']
		user.pincode=request.POST['pincode']
		user.save()
		Billing.objects.create(
			fname=request.POST['fname'],
			lname=request.POST['lname'],
			mobile=request.POST['mobile'],
			email=request.POST['email'],
			city=request.POST['city'],
			address=request.POST['address'],
			country=request.POST['country'],
			state=request.POST['state'],
			pincode=request.POST['pincode']
			)
		msg1="Your Billing Address Add Successfuly"
		carts=Cart.objects.filter(user=user,payment_status=False)
		subtotal=0
		for i in carts:
			subtotal=subtotal+i.product.product_price*i.product_qty
		discount=0
		if subtotal < 1000:
			discount=0
			msg="No Discount"
		elif subtotal <5000:
			discount=5
			msg="5% Discount"
		elif subtotal <10000:
			discount=10
			msg="10% Discount"
		elif subtotal <20000:
			discount=12
			msg="12% Discount"
		elif subtotal <25000:
			discount=15
			msg="15% Discount"
		else:
			discount=20
			msg="20% Discount"
		discount=(subtotal*discount)/100
		tax=2
		tax1=(subtotal*2)/100
		total=subtotal+tax-discount
		return render(request,'checkout.html',{'msg1':msg1,'user':user,'tax':tax,'carts':carts,'subtotal':subtotal,'discount':discount,'total':total,'msg':msg})

	else:
		return render(request,"checkout.html",{'user':user})
def category(request,name):
	product=Product.objects.filter(product_category=name)
	lenth=len(product)
	return render(request,"shop.html",{'product':product,'lenth':lenth})
	
	
def search(request):
	search=request.POST['search']

	try:
		product=Product.objects.filter(product_category__icontains=search)
		lenth=len(product)
		return render(request,"shop.html",{'product':product,'lenth':lenth})
	except:
		product=Product.objects.filter(product_name__icontains=search)
		lenth=len(product)
		return render(request,"shop.html",{'product':product,'lenth':lenth})

def top_search(request):
	search=request.POST['search']

	try:
		product=Product.objects.filter(product_category__icontains=search)
		lenth=len(product)
		return render(request,"index.html",{'product':product,'lenth':lenth})
	except:
		product=Product.objects.filter(product_name__icontains=search)
		lenth=len(product)
		return render(request,"index.html",{'product':product,'lenth':lenth})
def top_category(request,name):
	product=Product.objects.filter(product_genral_category=name)
	for i in product:
		delete=i.product_discount+i.product_price
	return render(request,"index.html",{'product':product,'delete':delete})

def range_category(request):
	range_category=request.POST['range_category']
	if request.POST['range_category']=='0':
		product=Product.objects.all()
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'range_category':range_category,'lenth':lenth})
	elif request.POST['range_category']=='1':
		product=Product.objects.all().order_by("-id")
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'range_category':range_category,'lenth':lenth})
	elif request.POST['range_category']=='2':
		product=Product.objects.all().order_by("-product_price")
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'range_category':range_category,'lenth':lenth})
	elif request.POST['range_category']=='3':
		product=Product.objects.all().order_by("product_price")
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'range_category':range_category,'lenth':lenth})
	else:
		product=Product.objects.all()
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'lenth':lenth})

def price(request):
	price=request.POST['price']
	if request.POST['price']=='1':
		product=Product.objects.filter(product_price__lte=1000)
		lenth=len(product)
		return render(request,"shop.html",{'product':product,'price':price,'lenth':lenth})
	elif request.POST['price']=='2':
		product=Product.objects.filter(product_price__gte=1001,product_price__lte=2500)
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'price':price,'lenth':lenth})
	elif request.POST['price']=='3':
		product=Product.objects.filter(product_price__gte=2501,product_price__lte=4000)
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'price':price,'lenth':lenth})
	elif request.POST['price']=='4':
		product=Product.objects.filter(product_price__gte=4001,product_price__lte=5000)
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'price':price,'lenth':lenth})
	elif request.POST['price']=='5':
		product=Product.objects.filter(product_price__gte=5001,product_price__lte=7000)
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'price':price,'lenth':lenth})
	elif request.POST['price']=='6':
		product=Product.objects.filter(product_price__gte=7001,product_price__lte=8600)
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'price':price,'lenth':lenth})
	elif request.POST['price']=='7':
		product=Product.objects.filter(product_price__gte=8601,product_price__lte=10000)
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'price':price,'lenth':lenth})
	elif request.POST['price']=='8':
		product=Product.objects.filter(product_price__gte=10001,product_price__lte=15000)
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'price':price,'lenth':lenth})
	elif request.POST['price']=='9':
		product=Product.objects.filter(product_price__gte=15001)
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'price':price})
	else:
		product=Product.objects.all()
		lenth=len(product)

		return render(request,"shop.html",{'product':product,'lenth':lenth})
def brand(request):
	brand=request.POST['brand'].lower()
	if brand == 'all':
		product=Product.objects.all()
		return render(request,"shop.html",{'product':product,'brand':brand})

	else:
		product=Product.objects.filter(product_company=brand)
		lenth=len(product)
		return render(request,"shop.html",{'product':product,'brand':brand,'lenth':lenth})

def initiate_payment(request):
    user=User.objects.get(email=request.session['email'])
    try:     
        amount =int(request.POST['amount'])
    except:
        return render(request, 'pay.html', context={'error': 'Wrong Accound Details or amount'})

    transaction = Transaction.objects.create(made_by=user, amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by.email)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()
    carts=Cart.objects.filter(user=user,payment_status=False)
    for i in carts:
    	i.payment_status=True
    	i.delete()
    	# i.save()
    carts=Cart.objects.filter(user=user,payment_status=False)
    request.session['cart_count']=len(carts)
    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    subject = 'Your Oder Conformation'
    message = 'Dear, '+user.fname+" "+user.lname+"\n\n Thank You for Sport Us, if any Quary please Contect Us, After Your Payment Confrim, You Get Conformation Email""\n\n Mobile Number : "+str(user.mobile)+"\n Email Id :"+user.email+",\n\n\n Your Address:"+user.address+"\n City: "+user.city+"\n  Pincode:"+str(user.pincode)+"\n\n Please Confrim Your Payment\n\n\n !!!Thank You!!!"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return render(request, 'redirect.html',context=paytm_params)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
            return render(request, 'confrim.html' , context=received_data)

        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'fail_payment.html', context=received_data)
    # return render(request, 'confrim.html' , context=received_data)
   
def my_order(request):
	cart=Cart.objects.filter(payment_status=True)
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	subtotal=0
	for i in cart:
		subtotal=subtotal+i.product.product_price*i.product_qty
	return render(request,"my_order.html",{'cart':cart,'subtotal':subtotal,'carts':carts})