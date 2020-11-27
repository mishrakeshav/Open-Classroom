// get all the elements
const clickedPost = document.getElementById("clicked-post");
const postTextArea = document.getElementById("post-textarea");
const cancelPost = document.getElementById("cancel-post")

// add event listeners
clickedPost.addEventListener("click", () => {
  clickedPost.classList.toggle("d-none");
  postTextArea.classList.toggle("d-none");
})
cancelPost.addEventListener("click", () => {
  clickedPost.classList.toggle("d-none");
  postTextArea.classList.toggle("d-none");
})
$(function() {
  $(".dropdown-menu").on('click', 'a', function() {
    $(this).parents('.dropdown').find('button').text($(this).text());
  });
});

$(document).ready(function(){
  $("#flip").click(function(){
    $("#panel").slideToggle("slow");
  });
});
