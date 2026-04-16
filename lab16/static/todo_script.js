document.addEventListener("DOMContentLoaded", loadTasks);

function loadTasks() {
    fetch("/get_tasks")
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById("tasklist");
            list.innerHTML = "";

            data.forEach(task => {
                createTaskElement(task.id, task.task);
            });
        });
}

function addTask(){
    const input = document.querySelector('#taskinput')
    const task = input.value.trim()

        if(task ==="") return;

        fetch("/add_task", {
            method: "post",
            headers : {"content-type":"application/json"},
            body: JSON.stringify({task:task})
        })
        .then(()=>{
            input.value="";
            loadTasks();
        })
    
}
function deleteTask(id){
    fetch("/delete_task",{
        method : "POST",
        headers : {"Content-Type" : "application/json"},
        body: JSON.stringify({id: id})
    })

    .then(()=> loadTasks())
}
function createTaskElement(id, taskText){
    const list = document.querySelector("#tasklist")
    const li = document.createElement("li")

    li.textContent = taskText + " "
    li.classList.add("task-item")

    const btn = document.createElement("button")
    btn.innerHTML = "&#10060;"
    btn.onclick = ()=> deleteTask(id)
    btn.classList.add("btn-delete-item")

    li.appendChild(btn)
    list.appendChild(li)

}