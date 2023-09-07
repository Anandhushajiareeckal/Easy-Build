function login_sub(){
    var user_name=document.getElementById("log_uname").value;
    var password=document.getElementById("log_pass").value;

    if(user_name==""){
        document.getElementById("user_alert").innerHTML="Enter username !"
    }
    else{
        document.getElementById("user_alert").innerHTML=""
    }
    if(password==""){
        document.getElementById("pass_alert").innerHTML="Enter password !"
    }
    else{
        document.getElementById("pass_alert").innerHTML=""
    }

}