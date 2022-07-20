function random_password() {
    var length = 8
    //evaluate character type
    var charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^";
    //return value
    var password = "";
    for (var i = 0; i < length; i++) {
        //picks a character within charSet at index of random number
        password += charSet.charAt(Math.floor(Math.random() * charSet.length));
    }
    console.log(password)

    var password1 = document.getElementById("id_password1")
    var password2 = document.getElementById("id_password2")

    password1.type = 'text'
    password1.value = password

    password2.type = 'text'
    password2.value = password
}