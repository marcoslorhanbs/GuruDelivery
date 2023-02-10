function showLogin()
{
    document.getElementById("Login").style = "display:block";
    document.getElementById("Register").style = "display: none";
    document.getElementById("ForgotPass").style = "display: none";
    document.getElementById("CheckEmail").style = "display: none";
}
function showRegister()
{
    document.getElementById("Register").style = "display: block";
    document.getElementById("Login").style = "display:none";
}
function showForgotPass()
{
    document.getElementById("ForgotPass").style = "display: block";
    document.getElementById("Login").style = "display:none";
}
function showCheckEmail()
{
    document.getElementById("CheckEmail").style = "display: block";
    document.getElementById("ForgotPass").style = "display: none";
    document.getElementById("Login").style = "display:none";
}