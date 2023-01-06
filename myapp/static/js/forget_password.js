function checkEmail()
{
	var f=document.frm.email.value;
	var reg=/^[A-Za-z0-9-_.]+@[A-Za-z]+\.[A-Za-z]{2,4}$/;
	if (f=="")
	{
		document.getElementById("email").innerHTML="Please Enter Email";
		document.getElementById("btn").disabled="true";
	}
	else if(!reg.test(f))
	{
		document.getElementById("email").innerHTML="Please Enter Valid Email Id";
		document.getElementById("btn").disabled="true";
	}
	else
	{
		document.getElementById("email").innerHTML="";
		document.getElementById("btn").disabled="";
	}
}