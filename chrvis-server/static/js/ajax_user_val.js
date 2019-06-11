$(function() {
    document.getElementById("submit_button").disabled = true;
    $('#id_email').keyup(function() {
        $.ajax({
            type: "GET",
            url: "/val_user",
            data: {
                'search_text' : $('#id_email').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'json'
        });
    });
});
function searchSuccess(data, textStatus, jqXHR)
{
    if (data.data.length === 1){
      document.getElementById("submit_button").disabled = true;
      var modal_btn = document.getElementById("modal-btn");
      modal_btn.click();
      console.log(data.data[0]);
      $('#id_email').val(data.data[0].email);
      $('#exampleModalLongTitle').html("Hi, " + data.data[0].username);
    }
    else{
      document.getElementById("submit_button").disabled = false;
    }
}
