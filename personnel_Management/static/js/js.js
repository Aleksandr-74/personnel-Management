window.addEventListener('DOMContentLoaded', function(){

     `use strict`;

     let addField = document.getElementById('add_field');
     console.log(addField);
     addField.addEventListener('clic', function(event){
          event.preventDefault();
          alert('Привет');
     });
     

});

