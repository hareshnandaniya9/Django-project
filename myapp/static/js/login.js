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

function checkpassword()
{
    var f=document.frm.password.value;
    var reg=/^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])(?!.*\s).{6,12}$/;
    // var reg=/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
    if (f=="")
    {
        document.getElementById("password").innerHTML="Please Enter Password";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("password").innerHTML="Please Enter Valid Password";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("password").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}