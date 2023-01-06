function checkFname()
{
    var f=document.frm.fname.value;
    var reg=/^[A-Za-z]+$/;
    if(f=="")
    {
        // alert("plese enter fname");
        document.getElementById("fname").innerHTML="Please Enter First_Name";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("fname").innerHTML="Please Enter only Alphabet";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("fname").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}

function checkLname()
{
    var f=document.frm.lname.value;
    var reg=/^[A-Za-z]+$/;
    if(f=="")
    {
        // alert("plese enter fname");
        document.getElementById("lname").innerHTML="Please Enter Last_Name";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("lname").innerHTML="Please Enter only Alphabet";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("lname").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}

function checkEmail()
{
    var f=document.frm.email.value;
    var reg=/^[A-Za-z0-9-_.]+@[A-Za-z]+\.[A-Za-z]{2,4}$/;
    if(f=="")
    {
        document.getElementById("email1").innerHTML="Plese Enter Email";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("email1").innerHTML="Please Enter Valid Email(e.g.abc@gmai.com)";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("email1").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}

function checkEmail()
{
    var f=document.frm.email.value;
    var reg=/^[A-Za-z0-9-_.]+@[A-Za-z]+\.[A-Za-z]{2,4}$/;
    if(f=="")
    {
        document.getElementById("email").innerHTML="Plese Enter Email";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("email").innerHTML="Please Enter Valid Email(e.g.abc@gmai.com)";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("email").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}
function checkmobile()
{
    var f=document.frm.mobile.value;
    var reg=/^\d{10}$/;
    if (f=="")
    {
        document.getElementById("mobile1").innerHTML="Please Enter 10 digit Mobile";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("mobile1").innerHTML="Please Enter Valid Mobile Number";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("mobile1").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}
function checkmobile()
{
    var f=document.frm.mobile.value;
    var reg=/^\d{10}$/;
    if (f=="")
    {
        document.getElementById("mobile").innerHTML="Please Enter 10 digit Mobile";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("mobile").innerHTML="Please Enter Valid Mobile Number";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("mobile").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}
function checaddress()
{
    var f=document.frm.address.value;
    if (f=="")
    {
        document.getElementById("address").innerHTML="Please Enter Address";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("address").innerHTML=""
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
        document.getElementById("password").innerHTML="Please Enter Password(6-12)";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("password").innerHTML="Please Enter one digit,small later,capital later and spacial character";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("password").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}

function checkcpassword()
{
    var f=document.frm.cpassword.value;
    var reg=/^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])(?!.*\s).{6,12}$/;
    if (f=="")
    {
        document.getElementById("cpassword").innerHTML="Please Enter Confrim Password";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("cpassword").innerHTML="Please Enter one digit,small later,capital later and spacial character";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("cpassword").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}

function checkphoto()
{
    var f=document.frm.profile_pic.value;
    if (f=="")
    {
        document.getElementById("profile_pic").innerHTML="Please Select File"
        document.getElementById("btn").disabled="true"
    }
    else
    {
        document.getElementById("profile_pic").innerHTML=""
        document.getElementById("btn").disabled=""
    }
}


function checkaadhaar()
{
    var f=document.frm.aadhaar.value;
    var reg=/^\d{12}$/;
    if (f=="")
    {
        document.getElementById("aadhaar").innerHTML="Please Enter 12 digit Aadhaar Number";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("aadhaar").innerHTML="Please Enter Valid Aadhaar Number";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("aadhaar").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}


function checkaadhaar()
{
    var f=document.frm.aadhaar.value;
    var reg=/^\d{12}$/;
    if (f=="")
    {
        document.getElementById("aadhaar").innerHTML="Please Enter 12 digit Aadhaar Number";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("aadhaar").innerHTML="Please Enter Valid Aadhaar Number";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("aadhaar").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}
function checkpincode()
{
    var f=document.frm.pincode.value;
    var reg=/^\d{6}$/;
    if (f=="")
    {
        document.getElementById("pincode").innerHTML="Please Enter 6 digit Pincode Number";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("pincode").innerHTML="Please Enter Valid Pincode Number";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("pincode").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}
function checkcity()
{
    var f=document.frm.city.value;
    var reg=/^[A-Za-z]+$/;
    if(f=="")
    {
        // alert("plese enter fname");
        document.getElementById("city").innerHTML="Please Enter City";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("city").innerHTML="Please Enter only Alphabet";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("city").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}

function checkgender()
{
    var f=document.frm.gender.value;
    var reg=/^[A-Za-z]+$/;
    if(f=="")
    {
        // alert("plese enter fname");
        document.getElementById("gender").innerHTML="Please Enter Gender";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("gender").innerHTML="Please Enter only Alphabet";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("gender").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}


function checkstate()
{
    var f=document.frm.state.value;
    var reg=/^[A-Za-z]+$/;
    if(f=="")
    {
        // alert("plese enter fname");
        document.getElementById("state").innerHTML="Please Enter Gender";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("state").innerHTML="Please Enter only Alphabet";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("state").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}

function checkdob()
{
    var f=document.frm.dob.value;
    if (f=="")
    {
        document.getElementById("dob").innerHTML="Please Enter Birth Date";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("dob").innerHTML=""
        document.getElementById("btn").disabled="";
    }
}

function checkotp()
{
    var f=document.frm.uotp.value;
    var reg=/^\d{4}$/;
    if (f=="")
    {
        document.getElementById("uotp").innerHTML="Please Enter OTP";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("uotp").innerHTML="Please Enter 6 digit OTP";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("uotp").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}

function checknewpassword()
{
    var f=document.frm.new_password.value;
    var reg=/^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])(?!.*\s).{6,12}$/;
    // var reg=/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
    if (f=="")
    {
        document.getElementById("new_password").innerHTML="Please Enter Password(6-12)";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("new_password").innerHTML="Please Enter one digit,small later,capital later and spacial character";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("new_password").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}

function checkcpassword()
{
    var f=document.frm.cnew_password.value;
    var reg=/^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])(?!.*\s).{6,12}$/;
    if (f=="")
    {
        document.getElementById("cnew_password").innerHTML="Please Enter Confrim Password";
        document.getElementById("btn").disabled="true";
    }
    else if(!reg.test(f))
    {
        document.getElementById("cnew_password").innerHTML="Please Enter one digit,small later,capital later and spacial character";
        document.getElementById("btn").disabled="true";
    }
    else
    {
        document.getElementById("cnew_password").innerHTML="";
        document.getElementById("btn").disabled="";
    }
}