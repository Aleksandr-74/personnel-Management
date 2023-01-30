window.addEventListener('DOMContentLoaded', function(){

    `use strict`;

    let btn = document.querySelector(".brigade");

    btn.addEventListener('click',  function(event){
            event.preventDefault();
        fetch(`api/v1/brigadesAPI/${btn.id}`)
        .then(response =>console.log(response.json()))
     })



//
//    fetch('api/v1/brigadesAPI/1')
//        .then(response =>response.json())
//        .then(workers => workers_object(workers))
//        .catch(err => console.log(err))
//
//    function workers_object(response){
//        response.forEach(item => {
//            console.log(item)
//        })
//    }

    let formBrigade = document.getElementById("form_brigade");
        formBrigade.addEventListener('submit', function(event){
            event.preventDefault();
            let response =  fetch('brigades', {
                    method: 'POST',
                    body: new FormData(formBrigade),
                })
            })



});