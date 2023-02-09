let create_form = document.getElementById('objects')
create_form.addEventListener('submit',  function(event){
     event.preventDefault();

    fetch('request/api/v1/objectAPI/', {
        method: 'POST',
        body: new FormData(create_form)
        })
        .then(respose => console.log(respose))
        .catch(err => console.log(err))

});