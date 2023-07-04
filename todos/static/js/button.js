function completeTask(){
    event.preventDefault();
    url = event.target.getAttribute("href");
    axios.post(url).then(response => {
        console.log(response)
        document.querySelector(`[data-todo-id="${response["data"]["todo"]["id"]}"]`).textContent = response['data']['todo']['completed'];
    })

};


window.onload = function(){
    document.querySelectorAll(".btn-success").forEach(btn => btn.addEventListener("click", completeTask))
};