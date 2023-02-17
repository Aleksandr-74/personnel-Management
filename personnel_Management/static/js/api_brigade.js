let currentUrl = window.location.pathname;
pk = currentUrl.split('/')[2]
let url = 'api/v1/brigadesAPI/' + pk

let delet_btn = document.querySelector('.delet_btn')

function readCookie(name) {
    let nameEQ = name + "=";
    let ca = document.cookie.split(';');
    for(let i=0;i < ca.length;i++) {
        let c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0)
            return c.substring(nameEQ.length,c.length);
    }
    return null;
}

let csrftoken = readCookie('csrftoken');


    /*******Удалене бригады*******/
delet_btn.addEventListener('click',  function(event){
    event.preventDefault();
    fetch(url, {
        method: 'DELETE',
         headers: {"X-CSRFToken":csrftoken }
        })
    .catch(err => console.log(err))
    let fieldInput = document.querySelector('.card');
    fieldInput.remove()
});
