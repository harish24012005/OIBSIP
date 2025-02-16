// script.js

document.addEventListener("DOMContentLoaded", () => {
    loadTasks();
});

function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value.trim();

    if (taskText === "") {
        alert("Please enter a task!");
        return;
    }

    let task = { text: taskText, completed: false };
    saveTask(task);
    taskInput.value = "";
    renderTasks();
}

function saveTask(task) {
    let tasks = getTasks();
    tasks.push(task);
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function getTasks() {
    return JSON.parse(localStorage.getItem("tasks")) || [];
}

function renderTasks() {
    let pendingTasks = document.getElementById("pendingTasks");
    let completedTasks = document.getElementById("completedTasks");
    pendingTasks.innerHTML = "";
    completedTasks.innerHTML = "";

    let tasks = getTasks();

    tasks.forEach((task, index) => {
        let li = document.createElement("li");
        li.innerHTML = `
            <span class="${task.completed ? 'completed' : ''}">${task.text}</span>
            <div class="buttons">
                <button class="complete-btn" onclick="toggleComplete(${index})">${task.completed ? 'Undo' : '✔'}</button>
                <button class="edit-btn" onclick="editTask(${index})">✏</button>
                <button class="delete-btn" onclick="deleteTask(${index})">🗑</button>
            </div>
        `;

        if (task.completed) {
            completedTasks.appendChild(li);
        } else {
            pendingTasks.appendChild(li);
        }
    });
}

function toggleComplete(index) {
    let tasks = getTasks();
    tasks[index].completed = !tasks[index].completed;
    localStorage.setItem("tasks", JSON.stringify(tasks));
    renderTasks();
}

function editTask(index) {
    let tasks = getTasks();
    let newTaskText = prompt("Edit your task:", tasks[index].text);

    if (newTaskText !== null) {
        tasks[index].text = newTaskText.trim();
        localStorage.setItem("tasks", JSON.stringify(tasks));
        renderTasks();
    }
}

function deleteTask(index) {
    let tasks = getTasks();
    tasks.splice(index, 1);
    localStorage.setItem("tasks", JSON.stringify(tasks));
    renderTasks();
}

function loadTasks() {
    renderTasks();
}
