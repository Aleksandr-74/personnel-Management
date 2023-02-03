document.addEventListener("DOMContentLoaded", () => {

    let currentUrl = window.location.pathname;
    pk = currentUrl.split('/')[2]
    let url = 'api/v1/brigadesAPI/' + pk

    let btn = document.querySelector(".brigade");
    let delet_btn = document.querySelector('.delet_btn')
    let update_btn = document.getElementById('send')
//    let url = 'api/v1/brigadesAPI/' + delet_btn.id

//    fetch(url)
//    .then(response =>(response.json()))
//    .then(brigade => add_card_brigade(brigade))

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
//    let formBrigade = document.getElementById("form_brigade");

//    const ajaxSend = (formData) => {
//        fetch(url, { // файл-обработчик
//            method: "PUT",
//            headers: {
//                "Content-Type": "application/json", // отправляемые данные
//            },
//            body: JSON.stringify(formData)
//        })
//            console.log(JSON.stringify(formData))
//            .then(response => alert("Сообщение отправлено"))
//            .catch(error => console.error(error))
//    };
//
//    if (document.getElementById("form_brigade")) {
//        const forms = document.getElementById("form_brigade");
//
//        for (let i = 0; i < forms.length; i++) {
//            forms[i].addEventListener("submit", function (e) {
//                e.preventDefault();
//
//                let formData = new FormData(this);
//                formData = Object.fromEntries(formData);
//
//                ajaxSend(formData)
//                    .then((response) => {
//                        console.log(response);
//                    })
//                    .catch((err) => console.error(err))
//            });
//        };
//    }






    let formBrigade = document.getElementById("form_brigade");
    formBrigade.addEventListener('submit', function(event){
        event.preventDefault();

        let formData = new FormData(this);
        formData = Object.fromEntries(formData);
        console.log(JSON.stringify(formData))


        fetch(url, {
            method: 'PUT',
            headers: {
                "Content-Type": "application/json", // отправляемые данные
            },
            body: JSON.stringify(formData)
             })
        .then(response => console.log(response))
        .catch(err => console.log(err))
    });

});