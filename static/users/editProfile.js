var uName = document.getElementById('username'),
fName = document.getElementById('fName'),
lName = document.getElementById('lName'),
email = document.getElementById('email'),
submitBtn = document.getElementById('submitBtn');

function inspectF(inp){
    if (uName.value != uVal){
        uName.classList.remove('unchanged')
    }else{
        uName.classList.add("unchanged")
    }
    if (fName.value != fVal){
        fName.classList.remove('unchanged')
    }else{
        fName.classList.add("unchanged")
    }
    if (lName.value != lVal){
        lName.classList.remove('unchanged')
    }else{
        lName.classList.add("unchanged")
    }
    if (email.value != eVal){
        email.classList.remove('unchanged')
    }else{
        email.classList.add("unchanged")
    }
    if (uName.classList.contains('unchanged') && fName.classList.contains('unchanged') && lName.classList.contains('unchanged') &&email.classList.contains('unchanged')){
        submitBtn.disabled = true
    }else{
        submitBtn.disabled = false
    }
}