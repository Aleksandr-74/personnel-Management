window.addEventListener('DOMContentLoaded', function(){

    `use strict`;


    let btn = document.querySelector(".brigade");
    let delet_btn = document.querySelector('.delet_btn')
    let update_btn = document.getElementById('send')


    /*******Удалене бригады*******/
    delet_btn.addEventListener('click',  function(event){
        event.preventDefault();
        url = 'api/v1/brigadesAPI/' + delet_btn.id
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
            url = 'api/v1/brigadesAPI/' + delet_btn.id
            fetch(url, {
                method: 'PUT',
                body: new FormData(formBrigade)
            });
        });

});