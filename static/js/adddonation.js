$(document).on('submit', '#don-form', function (e) {
    // e.preventDefault()
    $.ajax({
        type: 'POST',
        url: '/adddonation/',
        data: {
            title: $('#title').val(),
            category: $('#category').val(),
            bags: $('#bags').val(),
            address: $('#address').val(),
            city: $('#city').val(),
            postcode: $('#postcode').val(),
            phone: $('#phone').val(),
            data: $('#data').val(),
            time: $('#time').val(),
            more_info: $('#more_info').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
            this.currentStep++;
            this.updateForm();

},
    success:function () {
        alert("Dodano");
    }
})

});
