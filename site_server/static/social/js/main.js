/*  ---------------------------------------------------
    Template Name: Amin
    Description:  Amin magazine HTML Template
    Author: Colorlib
    Author URI: https://colorlib.com
    Version: 1.0
    Created: Colorlib
---------------------------------------------------------  */

'use strict';

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");
        $(".signup-section").show();
        $("#id_login").val('');
        $("#id_password").val('');
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    // Humberger Menu
    $(".humberger-open").on('click', function () {
        $(".humberger-menu-wrapper").addClass("show-humberger-menu");
        $(".humberger-menu-overlay").addClass("active");
        $(".nav-options").addClass("humberger-change");
    });


    $('.nav-item').on('mouseover', function () {
       var li = $(this).children();
        console.log(!li.hasClass('wait') + " : mouseover");
        if(!li.hasClass(' wait')){
           li.addClass("wait");
           console.log(li.attr('class') + " : add");
           $(li).stop(true, true).delay(100).animate(
           {
              opacity: .5,
              borderradius: "50%"
           },
           {
              step: function( now, fx ) {
                var data = fx.elem.id + " " + fx.prop + ": " + now;
                //console.log(data);
                //$( "body" ).append( "<div>" + data + "</div>" );
              }
           }, 100*1000
           );


       }
    })

    $('.nav-item').on('mouseout', function () {
       var li = $(this).children();
       console.log(li.hasClass('wait') + " : mouseout");
       if(li.hasClass('wait')){
           li.addClass(" wait");
           console.log(li.attr('class') + " : add");
           $(li).stop(true, true).delay(100*10).animate(
           {
              opacity: 1,
              borderradius: "50%"
           },
           {
              step: function( now, fx ) {
                var data = fx.elem.id + " " + fx.prop + ": " + now;
                //console.log(data);
                //$( "body" ).append( "<div>" + data + "</div>" );
              }

           }, 100*1000
           );
       li.removeClass("wait");
       console.log(li.attr('class') + " : remove");

        var data = $(li.html()).attr('src').split(".");
        var file = data[0];
        var ext = "." + data[data.length - 1];
        var id = file.split("/")[file.split("/").length - 1]

        if(file.indexOf("-action") == -1){
            file = file.replace("-stop", "");
            file = file + "-action";
        } else if(file.indexOf("-stop") == -1) {
            file = file.replace("-action", "");
            file = file + "-stop";
        } else {
            file = file.replace("-stop", "").replace("-action", "");;
        };

        var html = $(li.html()).attr('src', file + ext);
        li.html(html);

       }
    })

})(jQuery);