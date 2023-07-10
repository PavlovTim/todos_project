function completeTask(){
    event.preventDefault();
    url = event.target.getAttribute("href");
    console.log(url);
    axios.post(url).then(response => {
        console.log(response);
        status = response['data']['todo']['completed'];
        document.querySelector(`[data-todo-id="${response["data"]["todo"]["id"]}"]`).textContent = "Completed: True";
    })

};


window.onload = function(){
    document.querySelectorAll(".btn-success").forEach(btn => btn.addEventListener("click", completeTask))
};