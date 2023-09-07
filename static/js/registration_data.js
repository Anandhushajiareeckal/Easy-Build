function register_data(){
    var name=document.getElementById("inp_1").value;
    var phone=document.getElementById("inp_2").value;
    var email=document.getElementById("inp_3").value;
    var state=document.getElementById("state").value;
    var district=document.getElementById("inp_4").value;
    var current_location=document.getElementById("inp_5").value;
    var languages_knows=document.getElementById("inp_6").value;
    var password=document.getElementById("inp_7").value;
    
    if(name==""){
        document.getElementById("name_alert").innerHTML="Enter name !"
    }
    else{
        document.getElementById("name_alert").innerHTML=""
    }
    if(phone==""){
        document.getElementById("phone_alert").innerHTML="Enter phone number !"
    }
    else{
        document.getElementById("phone_alert").innerHTML=""
    }
    if(email==""){
        document.getElementById("email_alert").innerHTML="Enter email !"
    }
    else{
        document.getElementById("email_alert").innerHTML=""
    }
    if(state==""){
        document.getElementById("state_alert").innerHTML="Enter state!"
    }
    else{
        document.getElementById("state_alert").innerHTML=""
    }
    if(district==""){
        document.getElementById("dist_alert").innerHTML="Enter district !"
    }
    else{
        document.getElementById("dist_alert").innerHTML=""
    }
    if(current_location==""){
        document.getElementById("loca_alert").innerHTML="Enter current location !"
    }
    else{
        document.getElementById("loca_alert").innerHTML=""
    }
    if(languages_knows==""){
        document.getElementById("lang_alert").innerHTML="Enter languages knows !"
    }
    else{
        document.getElementById("lang_alert").innerHTML=""
    }
    if(password==""){
        document.getElementById("pass_alert").innerHTML="Enter password!"
    }
    else{
        document.getElementById("pass_alert").innerHTML=""
    }
    

}

