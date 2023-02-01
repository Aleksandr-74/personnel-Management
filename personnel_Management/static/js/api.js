window.addEventListener('DOMContentLoaded', function(){

    `use strict`;


    let btn = document.querySelector(".brigade");
    let delet_btn = document.querySelector('.delet_btn')
    let update_btn = document.getElementById('send')
    let url = 'api/v1/brigadesAPI/' + delet_btn.id

    fetch(url)
    .then(response =>(response.json()))
    .then(brigade => add_card_brigade(brigade))

    function add_card_brigade(response){
        let cardBrigade = document.createElement('div');
        cardBrigade.classList.add('card-brige');
        cardBrigade.innerHTML = `
            <div>Город : <span>${ response.citi }</span></div>

            `;
             document.querySelector(".card-body").appendChild(cardBrigade)
    }


    /*******Удалене бригады*******/
    delet_btn.addEventListener('click',  function(event){
        event.preventDefault();
        fetch(url, {
            method: 'DELETE',
        })
        .catch(err => console.log(err))
        let fieldInput = document.querySelector('.card');
        fieldInput.remove()
    })


    /*******Изменение бригады*******/
    let formBrigade = document.getElementById("form_brigade");
        formBrigade.addEventListener('submit', function(event){
            event.preventDefault();
            fetch(url, {
                method: 'PUT',
                body: new FormData(formBrigade)
            });
        });

});