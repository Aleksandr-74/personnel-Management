window.addEventListener('DOMContentLoaded', function(){

    `use strict`;



    let btn = document.querySelector(".brigade");
    let delet_btn = document.querySelector('.delet_btn')
    let update_btn = document.getElementById('send')


    btn.addEventListener('click',  function(event){
            event.preventDefault();
        fetch(`brigades/<int:brigade_id>/api/v1/brigadesAPI/<int:pk>/`)
        .then(response =>console.log(response.json()))
     })



    /*******Удалене бригады*******/
    delet_btn.addEventListener('click',  function(event){
        event.preventDefault();
        console.log(delet_btn.id)
        url = 'api/v1/brigadesAPI/' + delet_btn.id
        console.log(url)
        fetch(url, {
            method: 'DELETE',
        })
        .then(response =>console.log(response.json()))
        .catch(err => console.log(err))
        })


    update_btn.addEventListener('click',  function(event){
        event.preventDefault();
        console.log(delet_btn.id)
        url = 'api/v1/brigadesAPI/' + delet_btn.id
        console.log(url)
        fetch(url, {
            method: 'PUT',
        })
        .then(response =>console.log(response.json()))
        .catch(err => console.log(err))
        })




    function workers_object(response){
        response.forEach(item => {
            console.log(item)
        })
    }

    let formBrigade = document.getElementById("form_brigade");
        formBrigade.addEventListener('submit', function(event){
            event.preventDefault();
            let response =  fetch('brigades', {
                    method: 'POST',
                    body: new FormData(formBrigade),
                })
            })



});