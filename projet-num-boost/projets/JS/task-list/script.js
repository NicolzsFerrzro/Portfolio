// Tout le script est issus d'une formation IBM, 
// cependant il ne fonctionnait pas j'ai donc fait un travail inversé en cherchant d'où venait l'erreur
// il y avait une erreur dans l'implémentation de la valeur de input
// il y avait également une erreur dans la boucle for qui ajoute le bouton delete à toutes les taches

// Constants for input, button, and task list area
let taskInput = document.querySelector('#newtask input');
let taskSection = document.querySelector('.tasks');

// Listener for the Enter key to add a new task
taskInput.addEventListener("keyup", (e) => {
    if (e.key === "Enter") {
        createTask();
    }
});

// Event listener for the 'Add' button
document.querySelector('#push').onclick = function () {
    createTask();
};

// Function to create a new task
function createTask() {
    // Check if the input field is empty
    if (taskInput.value.trim().length === 0) {
        alert("The task field is empty. Enter a task name and try again.");
    } else {
        // Insert new task into the task area
        taskSection.innerHTML += `
            <div class="task">
                <label class="taskname">
                    <input onclick="updateTask(this)" type="checkbox" class="check-task">
                    <p>${taskInput.value}</p>
                </label>
                <div class="delete" >
                    <img src="delete-icone.png" width="26" height="26" alt="icone-delete">
                    <i class="uil uil-trash"></i>
                </div>
            </div>
        `;

        // Clear the input field
        taskInput.value = "";

        // Add delete functionality to all tasks
        let currentTasks = document.querySelectorAll(".delete");
        for (let i = 0; i < currentTasks.length; i++) {
            currentTasks[i].onclick = function () {
                this.parentNode.remove();
            };
        }

        // Handle task list overflow
        taskSection.offsetHeight >= 200
            ? taskSection.classList.add("overflow")
            : taskSection.classList.remove("overflow");
    }
}

// Function to update the task status
function updateTask(task) {
    let taskItem = task.parentElement.querySelector("p");
    if (task.checked) {
        taskItem.classList.add("checked");
    } else {
        taskItem.classList.remove("checked");
    }
}