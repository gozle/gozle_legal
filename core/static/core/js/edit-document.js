document.addEventListener("DOMContentLoaded", () => {
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
    
    
    
    const submitButton = document.querySelector(".btn-primary");
    submitButton.addEventListener("click", (e) => {
        e.preventDefault(); // Prevent default form submission

        var value = CKEDITOR.instances['id_body'].getData();
        let category = document.querySelector("#category").value;
        let header = document.querySelector("#header").value;
        let documentId = document.querySelector("#documentId").value; // Assuming you have a hidden input for document ID
        let language = document.querySelector("#language").value;
        console.log(language)
        fetch(`/api/${documentId}`, { // Update the URL with the document ID
            method: "PUT", // Use PUT method
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                header: header,
                body: value,
                category: category,
                language: language,
            })
        })
        .then(response => {
            if (response.ok) {
                window.location.replace(`/documents/${documentId}`);  
            } 
            else{
                console.log("something went wrong")
            }
        })
    });
});
