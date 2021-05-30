//Discount
function haveDiscount(discount){
    Swal.fire({
            position: 'between',
            icon: 'success',
            title: 'You used'+discount+'coupon!',
            showConfirmButton: false,
            timer: 2500
        })
}
function notDiscount(){
    Swal.fire({
            position: 'between',
            icon: 'error',
            title: 'You have not coupon!',
            showConfirmButton: false,
            timer: 2500
    })
}
function submitDiscount(discount){
    $.ajax({
        type: "POST", 
        url: '/discount/',
        data: {'discount':discount,},
        dataType: "json",
        headers:{
            'X-CSRFToken':csrftoken,
        },
        success: function (data) {  	
            console.log("toal.",data.total)
            $("#total").text("$"+data.total);   
        }
    });
     
}
//---------------------------------------------------


//Pay
function submitFormData(totalDjango){
    console.log('Payment button clicked')
    var userFormData={
        'name': null,
        'email': null,
    }
    var shippingInfo={
            'country':null,
            'address': null,
            'state': null,
            'zipcode': null,
    }
    var total= document.getElementById("total").getAttribute('value');
    var address = document.getElementById("chooseCountry").value;
    shippingInfo.address = address	
    shippingInfo.state = document.getElementById("state").value ;
    shippingInfo.zipcode = document.getElementById("postcode").value;
    userFormData.name = user
    console.log('ShippingInfo:' , shippingInfo)
    console.log('userFormData:' , userFormData)
    console.log("total:",total)
    if (total==totalDjango){
        var url ='/process_order/'
        fetch(url,{
                method :'POST',
                headers : {
                    'Content-Type': 'application/json',
                    'X-CSRFToken' :csrftoken,
                },
                body:JSON.stringify({'userFormData':userFormData, 'shippingInfo':shippingInfo,'total':total}),
        })
        .then((response) =>response.json())
        .then((data) =>{
                console.log('Success:' ,data);
                Swal.fire({
                    position: 'between',
                    icon: 'success',
                    title: 'Thank you for your purchase',
                    showConfirmButton: false,
                    timer: 4500
                })

                cart ={}
                document.cookie = 'cart='+ JSON.stringify(cart) + ";domain=;path=/"

                location.reload();
                })
    }else console.log("clmm")
}
//---------------------------------------------------
//exchangePoin
function exchange(discount){
    $.ajax({
        type: "POST", 
        url: '/exchange/',
        data: {'discount':discount,},
        dataType: "json",
        headers:{
            'X-CSRFToken':csrftoken,
        },
        success: function (data) {  
            console.log(typeof(data.code))
            if (data.code==1){	
                swal("Gotcha!", "Successful conversion", "success");  
                $("#accumulation").text("Accumulated Points:"+data.point);  
            }
            else{
                swal("Oh No!", "You don't have enough points to redeem", 'error'); 
            }
        },
    });
     
}
//----------------------------------------------------------