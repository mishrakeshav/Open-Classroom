// get all the elements 
const clickedPost = document.getElementById("clicked-post");
const postTextArea = document.getElementById("post-textarea");
const cancelPost = document.getElementById("cancel-post")

// add event listeners
clickedPost.addEventListener("click", ()=>{
    clickedPost.classList.toggle("d-none");
    postTextArea.classList.toggle("d-none");
})
cancelPost.addEventListener("click", ()=>{
    clickedPost.classList.toggle("d-none");
    postTextArea.classList.toggle("d-none");
})