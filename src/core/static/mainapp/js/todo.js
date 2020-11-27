try{

    $(document).ready(function() {
        // executes when HTML-Document is loaded and DOM is ready
         console.log("hllo");
       
           $( ".card" ).hover(
           function() {
             $(this).addClass('shadow-lg').css('cursor', 'pointer'); 
           }, function() {
             $(this).removeClass('shadow-lg');
           }
         );
         
       // document ready  
    });
} catch(err){
    console.log(err)
}