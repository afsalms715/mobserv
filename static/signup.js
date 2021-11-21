$(document).ready(function(){
    var alpha= new RegExp('[A-Z]');
    var number= new RegExp('[0-9]');

    $("#password").keyup(function(){
        var pass=$(this).val()
        if(pass.length>= 8){
            $(".plength").css("color","green");
        }else{
            $(".plength").css("color","red");
        }
        if(pass.match(alpha)){
            $(".palpha").css("color","green");
        }else{
            $(".palpha").css("color","red");
        }
        if(pass.match(number)){
            $(".pnumber").css("color","green");
        }else{
            $(".pnumber").css("color","red");
        }
    })
//    $("#signup").validation({
//        rules:{
//            name:{
//                required:true,
//                minlength:3
//            },
//             email:{
//                required:true,
//                email:true
//            },
//             username:{
//                required:true,
//                minlength:3
//            },
//        }
//    })
  })