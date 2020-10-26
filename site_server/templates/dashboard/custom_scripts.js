<script>


function select_category(){

    var category_class = $('#label').val();
    console.log(category_class);
    $('#category .' + category_class).prop('selected', true);
    $('#category .' + category_class).show();


}

function select_area_locations(){
    $('#location option').hide();
    //var area_class = $('#area').val().replace("+", "-");
    $("#location option").each(function(){
        this.selected=false;
        $('#location .' + this.value).hide();
    });

    $("#area option:selected").each(function(){

        $('#location .' + this.value).prop('selected', true);
        $('#location .' + this.value).show();
    });


}


function select_location(){
    //$('#area').prop('selected', false);
    $('#area option').hide();
    $('#location option').hide();
    $("#area option").each(function(){
        this.selected=false;
    });

    $("#location option").each(function(){
        this.selected=false;
    });

    var province_class = $('#province').val().replace("+", "-");
    console.log(province_class);
    $('#area .' + province_class).prop('selected', true);
    $('#area .' + province_class).show();
    select_area_locations()
}


function new_query(){

    console.log('Starting')
    $( ".card-body" ).load( "/api/add_gumtree_query/", function() {

    });
}


function add_gumtree_query(){

    var form = $("#query-form");
    var postUrl = form.attr('action');
    var category=[];
     $('#category :selected').each(function(){
         category[$(this).val()]=$(this).val();
     });

    var location=[];
     $('#location :selected').each(function(){
         location[$(this).val()]=$(this).val();
     });

     $('#area :selected').each(function(){
         location[$(this).val()]=$(this).val();
     });


    var data = {
        label: $('#label').val(),
        category: category,
        province: $('#province').val(),
        location: location,
        term: $('#term').val(),
        csrfmiddlewaretoken: '{{ csrf_token }}'
    };

    console.log(data)

    $.ajax({
      type: "post",
      url: postUrl,
      data: data,
      beforeSend: function() {

      },
      success: function(data) {
        console.log('success')
        //window.location = '/';
      },
      error: function(xhr) { // if error occured
        console.log(xhr.responseText)
      },
      complete: function() {
        console.log('complete')
      }
    });

}

(function($) {



 if('{{ request.user.is_staff }}' == 'False'){
    window.location = '/accounts/social_login/'
 };

$("#query-form").on('submit', function(e) {
  alert('test');
  e.preventDefault();

  var postUrl = $(this).attr('action');

  var data = {
    location: $(this).find('#location').val(),
    category: $(this).find('#category').val(),
    terms: $(this).find('#terms').val(),
    csrfmiddlewaretoken: '{{ csrf_token }}'
  };

  if ( data['location'].length > 1 ) {

    $.ajax({
      type: "post",
      url: postUrl,
      data: data,
      beforeSend: function() {

      },
      success: function(data) {
        console.log('success')
        //window.location = '/';
      },
      error: function(xhr) { // if error occured
        console.log(xhr.responseText)
      },
      complete: function() {
        console.log('complete')
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