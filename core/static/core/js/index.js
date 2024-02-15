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

const csrftoken = getCookie('csrftoken');

let deleteButton = document.querySelector("#delete-document")
let documentId = document.querySelector("#doc-id").innerHTML

deleteButton.addEventListener("click", (e)=>{
    fetch(`/api/${documentId}`, {
        method: 'DELETE',
        headers: {'X-CSRFToken': csrftoken},
        body: JSON.stringify({
            id : documentId
        })
    })
    
    .then(response => {
        if (response.ok) {
            alert('Document was successfully deleted');
            window.location.replace("/")
        } else {
            alert("Error")
        }
    })
})



