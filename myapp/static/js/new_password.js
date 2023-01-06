function checknew_password()
{
    var f=document.frm.new_password.value;
    var reg=/^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])(?!.*\s).{6,12}$/;
    // var reg=/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
    if (f=="")
    {
        document.getElementById("new_password").innerHTML="Please Enter Password";
        document.getElementById("ca").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("new_password").innerHTML="Please Enter Valid Password";
        document.getElementById("ca").disabled="true";
    }
    else
    {
        document.getElementById("new_password").innerHTML="";
        document.getElementById("ca").disabled="";
    }
}

function checkcnew_password()
{
    var f=document.frm.cnew_password.value;
    var reg=/^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])(?!.*\s).{6,12}$/;
    if (f=="")
    {
        document.getElementById("cnew_password").innerHTML="Please Enter Confrim Password";
        document.getElementById("ca").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("cnew_password").innerHTML="Please Enter Valid Confrim New Password";
        document.getElementById("ca").disabled="true";
    }
    else
    {
        document.getElementById("cnew_password").innerHTML="";
        document.getElementById("ca").disabled="";
    }
}