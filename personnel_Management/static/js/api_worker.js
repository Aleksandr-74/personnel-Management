let currentUrl = window.location.pathname;
pk = currentUrl.split('/')[2]
url = currentUrl +"api/v1/workersAPI/" + pk

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

let worker_id = document.getElementById('worker_id')
worker_id.addEventListener('click',  function(event){
            event.preventDefault();
        fetch(url, {
            method: 'DELETE',
            headers: {"X-CSRFToken":csrftoken }
        })
        .catch(err => console.log(err))
        let fieldInput = document.querySelector('.wrapper-worker');
        fieldInput.remove()
     })












