window.addEventListener('DOMContentLoaded', function(){

     `use strict`;

     let addField = document.getElementById('add_field');
     let deleteField = document.getElementById('delete_field')
     let fieldInput = document.getElementById('fieldSelect');

    deleteField.addEventListener("click", function(event){
        event.preventDefault();
        let fieldInput = document.getElementById('fieldSelect');
        fieldInput.remove()
    });

    addField.addEventListener("click", function(event){
        event.preventDefault();
        let clone = fieldInput.cloneNode(true);
        document.getElementById('wrapperInput').appendChild(clone);
     });


//     let form = document.querySelector(".formBrigage").serialize();
//     console.log(fo)
//     //    input = formReg.getElementsByTagName('input');
//        form.addEventListener('submit', function(event){
//            event.preventDefault();
//            let response =  fetch('brigades', {
//                    method: 'POST',
//                    body: new URLSearchParams(new FormData(form))
//                })
//          });
});          
//new URLSearchParams(new FormData(formElement));