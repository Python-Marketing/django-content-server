<script>



{% if query %}

window.setInterval(function(){
    $(".results").load("/gumtree/results/{{query.id}}", function(responseTxt, statusTxt, jqXHR){
        if(statusTxt == "success"){

        }
        if(statusTxt == "error"){

        }
    });
}, 5000);




{% endif %}



</script>