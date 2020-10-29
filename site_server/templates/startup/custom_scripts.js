<script>

function add_task(id) {

    var name = $('.name');
    name.val("");
    var email = $('.email');
    email.val("task@site.com");
    email.hide();
    var phone = $('.phone');
    phone.val("Task");
    phone.hide();
    var subject = $('.subject');
    subject.val("Task Added");
    subject.hide();
    var message = $('.message');
    message.val(id+"=id : ");
    $('html, body').animate({
            scrollTop: $("#contact").offset().top
    }, 500);
}


$('#portfolioCarousel').carousel({
  interval: 100000
})


$('.carousel .carousel-item').each(function(){
    var minPerSlide = 3;
    var next = $(this).next();
    if (!next.length) {
    next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));

    for (var i=0;i<minPerSlide;i++) {
        next=next.next();
        if (!next.length) {
        	next = $(this).siblings(':first');
      	}

        next.children(':first-child').clone().appendTo($(this));
      }
});


(function($) {


  'use strict';

  /**
   * =====================================
   * Function for email address validation
   * =====================================
   */
  function isValidEmail(emailAddress) {
    var pattern = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
    return pattern.test(emailAddress);
  };


    /**
     * ============================
     * CONTACT FORM 2
     * ============================
    */
    $("#contact-form").on('submit', function(e) {
      e.preventDefault();
      var success = $(this).find('.email-success'),
        failed = $(this).find('.email-failed'),
        loader = $(this).find('.email-loading'),
        postUrl = $(this).attr('action');

      var data = {
        name: $(this).find('.name').val(),
        email: $(this).find('.email').val(),
        subject: $(this).find('.subject').val(),
        phone: $(this).find('.phone').val(),
        message: $(this).find('#message').val()
      };

      if ( isValidEmail(data['email']) && (data['message'].length > 1) && (data['name'].length > 1) ) {

        $.ajax({
          type: "GET",
          url: postUrl,
          data: data,
          beforeSend: function() {
            loader.fadeIn(1000);
          },
          success: function(data) {
            loader.fadeOut(1000);
            success.delay(500).fadeIn(1000);
            failed.fadeOut(500);
            $('.name').val(''),
            $('.email').val(''),
            $('.subject').val(''),
            $('.phone').val(''),
            $('#message').val('')
            window.location = '/';
          },
          error: function(xhr) { // if error occured
            loader.fadeOut(1000);
            failed.delay(500).fadeIn(1000);
            success.fadeOut(500);
          },
          complete: function() {
            loader.fadeOut(1000);
          }
        });
      } else {
        loader.fadeOut(1000);
        failed.delay(500).fadeIn(1000);
        success.fadeOut(500);
      }
      return false;
    });

} (jQuery) );



</script>