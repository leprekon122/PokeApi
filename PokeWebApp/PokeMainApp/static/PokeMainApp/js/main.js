function login_logout(){
    var user = document.getElementById('user').innerHTML

    if( user != 'AnonymousUser'){
        document.getElementById('logout').style.display ='block'
        document.getElementById('logins').style.display = 'none'

    }
}
login_logout()


function add_poc(){
    var user = document.getElementById('user').innerHTML
    if( user == 'AnonymousUser'){
        window.alert('you must login !!!')
        return false
    } else {
        return true
    }

}