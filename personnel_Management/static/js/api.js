window.addEventListener('DOMContentLoaded', function(){

    `use strict`;

    fetch('api/v1/brigadesAPI')
        .then(response =>response.json())
        .then(workers => workers_object(workers))
        .catch(err => console.log(err))
    
    function workers_object(response){
        response.forEach(item => {
            console.log(item)
        })
    }




});