function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



document.addEventListener("DOMContentLoaded", ()=>{


    const submitButton = document.querySelector(".btn-primary")
    
    submitButton.addEventListener("click", (e)=>{
        e.preventDefault();
        var value = CKEDITOR.instances['id_body'].getData()
        let category = document.querySelector("#category").value
        let header = document.querySelector("#header").value
        let language = document.querySelector("#language").value;
        fetch('/api/', {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                "Content-Type": "application/json",
              },
            body: JSON.stringify({
                header:header,
                body:value,
                category:category,
                language:language,
            })
        })
        .then(response =>{
            if(response.ok){
                alert("You successfully added a document!");
                window.location.replace("/")
            }
            return response.json()
        })
        .then(data =>{
            alert("error" + data["error"])
        })
    })

})


