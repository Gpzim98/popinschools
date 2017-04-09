function searchSchool(){
    var country = $('#country').val();
    var city = $('#city').val();
    var idiom = $('#idiom').val();
    var classification = $('#classification').slider("values");
    var price = $('#price').slider("values");
    var visa = $('input[name=visa]:checked', '#formSearch').val();
    var classes = $('input[name=classes]:checked', '#formSearch').val();
    var shift = $('input[name=shift]:checked', '#formSearch').val();
    var part_time = $('#part-time').prop("checked");
    var anual = $('#anual').prop("checked");
    var full_time = $('#full-time').prop("checked");
    var semester = $('#semester').prop("checked");
    var intensive = $('#intensive').prop("checked");
    var trimestral = $('#trimestral').prop("checked");
    var business = $('#business').prop("checked");
    var mensal = $('#mensal').prop("checked");

    $.ajax({
        type: 'GET',
        url: '/schools/',
        data: {
            country: country,
            city: city,
            csrfmiddlewaretoken: $("[name*='csrfmiddlewaretoken']").val()
        },
        success: function(result){
            console.log('Success: ' + result);
        }
    });

}

