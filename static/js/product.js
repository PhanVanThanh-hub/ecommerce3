function myFunction(e) {
    console.log("ok",e)
    $.ajax({
        type: "POST", 
        url: '',
        data: {'e':e},
        dataType: "html",
        headers:{
            'X-CSRFToken':csrftoken,
        },
        success: function (data) {
            $(".sortBy").html(data)
            console.log("maybe")
        }
    });
  }
  function submitFormSearch(){
     
    $.ajax({
        url: '',
        type: 'post',
        data: new FormData(document.getElementById("search")),
        processData: false,
        contentType: false,
        dataType: 'html',
        success: function (data){
            $(".sortBy").html(data)
            console.log("okmen")
            
        }
    })
}
