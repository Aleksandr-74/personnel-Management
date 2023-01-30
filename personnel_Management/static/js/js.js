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

});          
