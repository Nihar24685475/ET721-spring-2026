function validatePassword(){
    const password = document.querySelector('input[name="password"]').value

    if(password.length < 6){
        alert("Password must be at least 6+ characters")
        return false
    }
    
    return true
}
