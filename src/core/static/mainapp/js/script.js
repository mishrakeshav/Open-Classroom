// get all the elements 
const clickedPost = document.getElementById("clicked-post");
const postTextArea = document.getElementById("post-textarea");
const cancelPost = document.getElementById("cancel-post")
try{

    // add event listeners
    clickedPost.addEventListener("click", ()=>{
        clickedPost.classList.toggle("d-none");
        postTextArea.classList.toggle("d-none");
    })
    cancelPost.addEventListener("click", ()=>{
        clickedPost.classList.toggle("d-none");
        postTextArea.classList.toggle("d-none");
    })
} catch(err){
    console.log(err)
}
try{

    function copyCode() {
        /* Get the text field */
        var copyText = document.getElementById("classroom-code");
      
        /* Select the text field */
        copyText.select();
        copyText.setSelectionRange(0, 99999); /*For mobile devices*/
      
        /* Copy the text inside the text field */
        document.execCommand("copy");
      
        /* Alert the copied text */
        alert("Classroom code copied to clipboard");
    }
}catch(err){
    console.log(err);
}

