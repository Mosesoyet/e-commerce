window.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger')
    const Menubar = document.querySelector('.sidemenubar')
    const closeMenu = document.querySelector('.close-menu')

    
    
    

    



    /*Change the style of side menu bar so that if burger is clicked
    then the sidemenu appear
    */
   burger.addEventListener('click', () => {
       setTimeout(() => {
           Menubar.style.transform = 'translateY(0%)'
           const bodyOverlay = document.createElement('div')
           bodyOverlay.classList.add('overlay')
            setTimeout(() => {
                document.querySelector('body').append(bodyOverlay)
            }, 200)
       }, 100)
   })
   closeMenu.addEventListener('click', () => {
           Menubar.style.transform = 'translateY(-100%)'
           const bodyOverlay = document.querySelector('.overlay')
           document.querySelector('body').removeChild(bodyOverlay)
   })

   
})


function validateForm() {
    const firstName = document.getElementById('firstname').value
    const lastName = document.getElementById('lastname').value
    const passWord = document.getElementById('password').value
    const email = document.getElementById('email').value

    var regx = /([a-z A-Z 0-9 \. _]+)@([a-z A-Z]+).([a-z A-Z]{2, 6})/

    if (firstName.trim() === "" || lastName.trim() === "" || passWord.trim() === "") {
        alert("Missing Info")
        return false
    }

    if (email.trim() === "") {
        alert("Please enter a valid email")
    } else if ((regx.test(email))) {
        return true
    } else {
        alert("Wrong email entered")
        return false
    }

    
}