function checkname()
{
    var f=document.frm.name.value;
    var reg=/^[A-Za-z]+$/;
    if(f=="")
    {
        // alert("plese enter fname");
        document.getElementById("name").innerHTML="Please Enter First_Name";
        document.getElementById("submit").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("name").innerHTML="Please Enter only Alphabet";
        document.getElementById("submit").disabled="true";
    }
    else
    {
        document.getElementById("name").innerHTML="";
        document.getElementById("submit").disabled="";
    }
}

function checkEmail()
{
    var f=document.frm.email.value;
    var reg=/^[A-Za-z0-9-_.]+@[A-Za-z]+\.[A-Za-z]{2,4}$/;
    if(f=="")
    {
        document.getElementById("email").innerHTML="Plese Enter Email_Id";
        document.getElementById("submit").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("email").innerHTML="Please Enter Valid Email";
        document.getElementById("submit").disabled="true";
    }
    else
    {
        document.getElementById("email").innerHTML="";
        document.getElementById("submit").disabled="";
    }
}

function checkmobile()
{
    var f=document.frm.mobile.value;
    var reg=/^\d{10}$/;
    if (f=="")
    {
        document.getElementById("mobile").innerHTML="Please Enter 10 digit Mobile";
        document.getElementById("submit").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("mobile").innerHTML="Please Enter Valid Mobile Number";
        document.getElementById("submit").disabled="true";
    }
    else
    {
        document.getElementById("mobile").innerHTML="";
        document.getElementById("submit").disabled="";
    }
}

function checkfeedback()
{
    var f=document.frm.feedback.value;
    if (f=="")
    {
        document.getElementById("feedback").innerHTML="Please Enter Address";
        document.getElementById("submit").disabled="true";
    }
    else
    {
        document.getElementById("feedback").innerHTML=""
        document.getElementById("submit").disabled="";
    }
}