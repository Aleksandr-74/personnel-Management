let currentUrl = window.location.pathname;
pk = currentUrl.split('/')[2]
url = currentUrl +"api/v1/workersAPI/" + pk


let worker_id = document.getElementById('worker_id')
worker_id.addEventListener('click',  function(event){
            event.preventDefault();
        fetch(url, {
            method: 'DELETE',
        })
        .catch(err => console.log(err))
        let fieldInput = document.querySelector('.wrapper-worker');
        fieldInput.remove()
     })












