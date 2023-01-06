function checkuotp()
{
    var f=document.frm.uotp.value;
    var reg=/^\d{4}$/;
    if (f=="")
    {
        document.getElementById("uotp").innerHTML="Please Enter 4 digit OTP";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("uotp").innerHTML="Please Enter Valid OTP";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("uotp").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}