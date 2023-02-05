let currentUrl = window.location.pathname;
pk = currentUrl.split('/')[2]
let url = 'api/v1/brigadesAPI/' + pk

let delet_btn = document.querySelector('.delet_btn')


    /*******Удалене бригады*******/
delet_btn.addEventListener('click',  function(event){
    event.preventDefault();
    fetch(url, {
        method: 'DELETE',
        })
    .catch(err => console.log(err))
    let fieldInput = document.querySelector('.card');
    fieldInput.remove()
});
