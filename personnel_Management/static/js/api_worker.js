let currentUrl = window.location.pathname;
pk = currentUrl.split('/')[2]
url = currentUrl +"api/v1/workersAPI/" + pk
fetch(url).then(response => response.json())
.then(worker => get_card(worker))
.catch(err => console.log(err))

function get_card(response){
    let cardWorker= document.createElement('div');
    cardWorker.classList.add('card-worker');
    cardWorker.innerHTML = `
    <div class="">
        <h3 class="title_text">${ response.roles }: ${ response.name_worker }</h3>
    </div>

    `;
    document.querySelector(".wrapper-worker").appendChild(cardWorker)
}

let worker_id = document.getElementById('worker_id')
worker_id.addEventListener('click',  function(event){
            event.preventDefault();
        fetch(url, {
            method: 'DELETE',
        })
        .catch(err => console.log(err))
        let fieldInput = document.querySelector('.card-worker');
        fieldInput.remove()
     })












