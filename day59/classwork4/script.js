let namevar = String(document.getElementById('names').value)
let email = String(document.getElementById('emails').value)
let password = String(document.getElementById('passwords').value)
let btn = document.getElementById('submit')

btn.addEventListener('click', function(){
    if (namevar.length > 0){
        console.log(namevar)
    }

    if (email.length > 0){
        console.log(email)
    }

    if (password.length > 0){
        console.log(password)
    }
})