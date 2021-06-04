
(function ($) {
    "use strict";

    /*[ Load page ]
    ===========================================================*/
    $(".animsition").animsition({
        inClass: 'fade-in',
        outClass: 'fade-out',
        inDuration: 1500,
        outDuration: 800,
        linkElement: '.animsition-link',
        loading: true,
        loadingParentElement: 'html',
        loadingClass: 'animsition-loading-1',
        loadingInner: '<div class="loader05"></div>',
        timeout: false,
        timeoutCountdown: 5000,
        onLoadEvent: true,
        browser: [ 'animation-duration', '-webkit-animation-duration'],
        overlay : false,
        overlayClass : 'animsition-overlay-slide',
        overlayParentElement : 'html',
        transition: function(url){ window.location.href = url; }
    });
    
    /*[ Back to top ]
    ===========================================================*/
    var windowH = $(window).height()/2;

    $(window).on('scroll',function(){
        if ($(this).scrollTop() > windowH) {
            $("#myBtn").css('display','flex');
        } else {
            $("#myBtn").css('display','none');
        }
    });

    $('#myBtn').on("click", function(){
        $('html, body').animate({scrollTop: 0}, 300);
    });


    /*==================================================================
    [ Fixed Header ]*/
    var headerDesktop = $('.container-menu-desktop');
    var wrapMenu = $('.wrap-menu-desktop');

    if($('.top-bar').length > 0) {
        var posWrapHeader = $('.top-bar').height();
    }
    else {
        var posWrapHeader = 0;
    }
    

    if($(window).scrollTop() > posWrapHeader) {
        $(headerDesktop).addClass('fix-menu-desktop');
        $(wrapMenu).css('top',0); 
    }  
    else {
        $(headerDesktop).removeClass('fix-menu-desktop');
        $(wrapMenu).css('top',posWrapHeader - $(this).scrollTop()); 
    }

    $(window).on('scroll',function(){
        if($(this).scrollTop() > posWrapHeader) {
            $(headerDesktop).addClass('fix-menu-desktop');
            $(wrapMenu).css('top',0); 
        }  
        else {
            $(headerDesktop).removeClass('fix-menu-desktop');
            $(wrapMenu).css('top',posWrapHeader - $(this).scrollTop()); 
        } 
    });


    /*==================================================================
    [ Menu mobile ]*/
    $('.btn-show-menu-mobile').on('click', function(){
        $(this).toggleClass('is-active');
        $('.menu-mobile').slideToggle();
    });

    var arrowMainMenu = $('.arrow-main-menu-m');

    for(var i=0; i<arrowMainMenu.length; i++){
        $(arrowMainMenu[i]).on('click', function(){
            $(this).parent().find('.sub-menu-m').slideToggle();
            $(this).toggleClass('turn-arrow-main-menu-m');
        })
    }

    $(window).resize(function(){
        if($(window).width() >= 992){
            if($('.menu-mobile').css('display') == 'block') {
                $('.menu-mobile').css('display','none');
                $('.btn-show-menu-mobile').toggleClass('is-active');
            }

            $('.sub-menu-m').each(function(){
                if($(this).css('display') == 'block') { console.log('hello');
                    $(this).css('display','none');
                    $(arrowMainMenu).removeClass('turn-arrow-main-menu-m');
                }
            });
                
        }
    });


    /*==================================================================
    [ Show / hide modal search ]*/
    $('.js-show-modal-search').on('click', function(){
        $('.modal-search-header').addClass('show-modal-search');
        $(this).css('opacity','0');
    });

    $('.js-hide-modal-search').on('click', function(){
        $('.modal-search-header').removeClass('show-modal-search');
        $('.js-show-modal-search').css('opacity','1');
    });

    $('.container-search-header').on('click', function(e){
        e.stopPropagation();
    });


    /*==================================================================
    [ Isotope ]*/
    var $topeContainer = $('.isotope-grid');
    var $filter = $('.filter-tope-group');
    // filter items on button click
    console.log("filter:",$filter)
    console.log("topeContainer:",$topeContainer)
    $filter.each(function () {
        $filter.on('click', 'button', function () {
            var filterValue =$(this).attr('data-filter');
            console.log("filerValue",filterValue)
            $topeContainer.isotope({filter: filterValue});
        });
        
    });

    // init Isotope
    $(window).on('load', function () {
        var $grid = $topeContainer.each(function () {
            $(this).isotope({
                itemSelector: '.isotope-item',
                layoutMode: 'fitRows',
                percentPosition: true,
                animationEngine : 'best-available',
                masonry: {
                    columnWidth: '.isotope-item'
                }
            });
        });
    });

    var $filter1 = $('.filter-tope-group1');
    // filter items on button click
    console.log("filter1:",$filter1)
    $filter1.each(function () {
        $filter1.on('click', 'button', function () {
            console.log("dsads")
            var filterValue1 = $(this).attr('data-filter');
            console.log("filerValue1",filterValue1)
            $topeContainer.isotope({filter: filterValue1});
             
        });
        
    });
    // init Isotope
     
    var isotopeButton1 = $('.filter-tope-group1 button');

    $(isotopeButton1).each(function(){
        $(this).on('click', function(){
            for(var i=0; i<isotopeButton1.length; i++) {
                $(isotopeButton1[i]).removeClass('filter-link-active');
            }
            $(this).addClass('filter-link-active');
        });
    });
    var isotopeButton = $('.filter-tope-group button');

    $(isotopeButton).each(function(){
        $(this).on('click', function(){
            for(var i=0; i<isotopeButton.length; i++) {
                $(isotopeButton[i]).removeClass('how-active1');
            }
            $(this).addClass('how-active1');
        });
    });

    /*==================================================================
    [ Filter / Search product ]*/
    $('.js-show-filter').on('click',function(){
        $(this).toggleClass('show-filter');
        $('.panel-filter').slideToggle(400);

        if($('.js-show-search').hasClass('show-search')) {
            $('.js-show-search').removeClass('show-search');
            $('.panel-search').slideUp(400);
        }    
    });

    //--------------------------

    //--------------------------


    $('.js-show-search').on('click',function(){
        $(this).toggleClass('show-search');
        $('.panel-search').slideToggle(400);

        if($('.js-show-filter').hasClass('show-filter')) {
            $('.js-show-filter').removeClass('show-filter');
            $('.panel-filter').slideUp(400);
        }    
    });



    /*==================================================================
    [ Chat ]*/
    $('.js-show-chat').on('click',function(){
        console.log("1")
        $('.js-panel-chat').addClass('show-header-chat');
        console.log("2")
    });
    $('.js-hide-chat').on('click',function(){
        $('.js-panel-chat').removeClass('show-header-chat');
    });

    /*==================================================================
    [ Cart ]*/
    $('.js-show-cart').on('click',function(){
        $('.js-panel-cart').addClass('show-header-cart');
    });
    $('.js-hide-cart').on('click',function(){
        $('.js-panel-cart').removeClass('show-header-cart');
    });
    /*==================================================================
    [ Favorite ]*/
    $('.js-show-favorite').on('click',function(){
        $('.js-panel-favorite').addClass('show-header-favorite');
    });
    $('.js-hide-favorite').on('click',function(){
        $('.js-panel-favorite').removeClass('show-header-favorite');
    });
    /*==================================================================
    [ Cart ]*/
    $('.js-show-sidebar').on('click',function(){
        $('.js-sidebar').addClass('show-sidebar');
    });

    $('.js-hide-sidebar').on('click',function(){
        $('.js-sidebar').removeClass('show-sidebar');
    });

    /*==================================================================
    [ +/- num product ] */
    $('.btn-num-product-down').on('click', function(){
        var numProduct = Number($(this).next().val());
        if(numProduct > 0) $(this).next().val(numProduct - 1);
    });

    $('.btn-num-product-up').on('click', function(){
        var numProduct = Number($(this).prev().val());
        $(this).prev().val(numProduct + 1);
    });

    /*==================================================================
    [ Rating ]*/
    $('.wrap-rating').each(function(){
        var item = $(this).find('.item-rating');
        var rated = -1;
        var input = $(this).find('input');
        $(input).val(0);

        $(item).on('mouseenter', function(){
            var index = item.index(this);
            var i = 0;
            for(i=0; i<=index; i++) {
                $(item[i]).removeClass('zmdi-star-outline');
                $(item[i]).addClass('zmdi-star');
            }

            for(var j=i; j<item.length; j++) {
                $(item[j]).addClass('zmdi-star-outline');
                $(item[j]).removeClass('zmdi-star');
            }
        });

        $(item).on('click', function(){
            var index = item.index(this);
            rated = index;
            $(input).val(index+1);
        });

        $(this).on('mouseleave', function(){
            var i = 0;
            for(i=0; i<=rated; i++) {
                $(item[i]).removeClass('zmdi-star-outline');
                $(item[i]).addClass('zmdi-star');
            }

            for(var j=i; j<item.length; j++) {
                $(item[j]).addClass('zmdi-star-outline');
                $(item[j]).removeClass('zmdi-star');
            }
        });
    });
    
    /*==================================================================
    [ Show modal1 ]*/
     



})(jQuery);
/*==================================================================
[ add cart ]*/
var addBtn= document.getElementsByClassName("add-cart")
var k=0
for(i=0;i<addBtn.length;i++){
    addBtn[i].addEventListener('click',function(){
        productId = this.dataset.product
        action = this.dataset.action
        temp = addBtn[i].value
        x=0 
        amount = this.dataset.amount
        console.log("ss:L",typeof(amount))
        if (action == "create"){
             
            x = document.getElementById("value").value;
            var size = document.getElementById("chooseSize").value;
            var color = document.getElementById("chooseColor").value;
            console.log('size:',size,'|color:',color,':',amount )
        }
        console.log("x:",typeof(x))
        
        if(size == 'Choose an option' || color == 'Choose an option'){
            console.log("ngu")            
        }
        else if(Number(amount)<Number(x)){
            Swal.fire({
                position: 'between',
                icon: 'error',
                title: 'Out of stock!'+'Just have:'+Number(amount),
                showConfirmButton: false,
                timer: 2500
            })
        }
        else{
            console.log('productId:',productId,'action:',action,'value:',x)
            console.log('USER:',user)
            if(user !='AnonymousUser' && action=="create"){
                addCart(productId,action,x,size,color)
                 
            }
            else{
                color = this.dataset.color
                size = this.dataset.size
                var total = document.getElementById("total").value
                console.log("total:",total)
                
                 
                console.log("i:",i,"sssssss",action,': ',color,':',size,':')
                updateCart(productId,action,color,size)
            }
        }
     })
}
function addCart(productId,action,value,size,color){
	console.log('User is authenticated, sending data...')
    $.ajax({
        type: "POST", 
        url: '/add_cart_item/',
        data: {'productId':productId, 'action':action,'value':value,'size':size,'color':color},
        dataType: "json",
        headers:{
            'X-CSRFToken':csrftoken,
        },
        success: function (data) {
            console.log('xxx:',data.change)
            if(data.change ==0){
                Swal.fire({
                    position: 'between',
                    icon: 'error',
                    title: 'Out of stock!',
                    showConfirmButton: false,
                    timer: 2500
                })
            }   
            else{
                
                $("#cartquantity").attr("value",data.quantity)
                 
            } 
             
            
        }
    });
	 
}
/*==================================================================
[ updata cart ]*/
/*var updataBtn= document.getElementsByClassName("update-cart")
for(i=0;i<updataBtn.length;i++){
    updataBtn[i].addEventListener('click',function(){
        productId = this.dataset.product
        action = this.dataset.action
        console.log('productId:',productId,'action:',action)
        console.log('USER:',user)
        if(user !='AnonymousUser'){
            updateCart(productId,action)
        }
     })
}*/
function updateCart(productId,action,color,size){
	console.log('User is authenticated, sending data...')
    $.ajax({
        type: "POST", 
        url: '/add_cart_item/',
        data: {'productId':productId, 'action':action,'color':color,'size':size},
        dataType: "json",
        headers:{
            'X-CSRFToken':csrftoken,
        },
        success: function (data) {  
            console.log('xxx:',data.change)
            if(data.change ==0){
                Swal.fire({
                    position: 'between',
                    icon: 'error',
                    title: 'Out of stock!',
                    showConfirmButton: false,
                    timer: 2500
                })
            }   
            else{
                
                $("#cartquantity").attr("value",data.quantity)
                $("#total").text("$"+data.total);   
            }          
            
            $("#ajax_cart").html()
        

        }
    });
}
/*==================================================================
[ add favorive ]*/
 
var  addFavorite= document.getElementsByClassName("add-favorite")
for(i=0;i<addFavorite.length;i++){
    addFavorite[i].addEventListener('click',function(){
    productId = this.dataset.product
    action = this.dataset.action
    var btn=document.getElementsByClassName("favorite")
    x = btn[productId-1].value
    console.log('action',action)
    console.log("productId",productId)
    console.log("Value",x)
    if (x==1){
        action ="remove"
    }
    if(user !='AnonymousUser' && action == "remove"){
        addFavorite2(productId,action)
    }else{
        addFavorite1(productId)
         
    }

})
}
function addFavorite1(productId){
	console.log('sending data...')
		var url = '/add_favorite/'
		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			},
			body:JSON.stringify({'productId':productId})
		})
		.then((response) => {
            return response.json();
         })
         .then((data) => {
             location.reload()
         });
}
function addFavorite2(productId,action){
    console.log('User is authenticated, sending data...')
		var url = '/add_favorite/'
		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			},
			body:JSON.stringify({'productId':productId,'action':action})
		})
		.then((response) => {
            return response.json();
         })
         .then((data) => {
             location.reload()
         });
}

/*==================================================================
[ quickView ]*/
// var quickBtn= document.getElementsByClassName("quickView")
// for(i=0;i<quickBtn.length;i++){
   
//     quickBtn[i].addEventListener('click',function(){
//         productId = this.dataset.product
//         console.log("lalalala",productId)
         
//         $.ajax({
//             url:'/quickView/',
//             type : "POST", 
//             data : { 'productId':productId }, 
//             dataType: "html",
//             headers:{
//                 'X-CSRFToken':csrftoken,
//             },
//             success : function(data) {
                
//                 console.log("success"); // another sanity check
//                 $('#myBtn').html(data)
//             },
            
//         });
//     })
// }
