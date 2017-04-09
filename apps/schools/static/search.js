function searchSchool(){
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
        url: '/api/schools/',
        data: {
            country: $('#country').val(),
            city: $('#city').val(),
            language: $('#idiom').val(),
            min_rating: $('#classification').slider("values")[0],
            max_rating: $('#classification').slider("values")[1],
            min_price: $('#price').slider("values")[0],
            max_price: $('#price').slider("values")[1],
            shift: $('input[name=shift]:checked', '#formSearch').val(),
            visa: $('input[name=visa]:checked', '#formSearch').val(),
            classes_type: $('input[name=classes]:checked', '#formSearch').val(),
            csrfmiddlewaretoken: $("[name*='csrfmiddlewaretoken']").val()
        },
        success: function(result){
            delete_school_list();
            recreate_school_list(result);
        }
    });
}

function recreate_school_list(result) {
    for (var i = 0; i < result.length; i++) {
        create_school(result[i]);
    }
}

function delete_school_list() {
    var search_result = document.getElementById("search-result");
    while (search_result.firstChild) {
        search_result.removeChild(search_result.firstChild);
    }
}

function create_school(school){
    var div_result = document.createElement("div");
    div_result.className="result";

    // School image profile
    var image_school_profile_link = document.createElement("a");
    image_school_profile_link.href = 'profile/' + school.id;
    var image_shcool_profole = document.createElement("img");
    image_shcool_profole.src = school.logo;
    image_school_profile_link.appendChild(image_shcool_profole);
    div_result.appendChild(image_school_profile_link);

    //School name h2
    var school_name = document.createElement("h2");
    var school_profile_link = document.createElement("a");
    school_profile_link.appendChild(document.createTextNode(school.name))
    school_profile_link.href = 'profile/' + school.id;
    school_name.appendChild(school_profile_link);
    div_result.appendChild(school_name);

    //Rating div
    var div_rating = document.createElement("div");
    div_rating.className = "school-rating";
    div_rating.appendChild(document.createTextNode(school.rating));
    div_result.appendChild(div_rating);

    //School text description paragraph
    var school_description = document.createElement('p');
    school_description.appendChild(document.createTextNode(school.short_phrase));
    div_result.appendChild(school_description);

    //School text description paragraph
    var school_language = document.createElement('p');
    school_language.appendChild(document.createTextNode(school.language));
    div_result.appendChild(school_language);


    document.getElementById('search-result').appendChild(div_result);

}

