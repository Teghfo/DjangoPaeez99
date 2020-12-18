// $(document).ready(function() {
//     $('.submitbutton').click(function() {
//         var pos = $(this).parent().find('.inputid').val();
//         var csrf = $(this).parent().find("input[name='csrfmiddlewaretoken']").val();
//         $.ajax({
//             // url: "cart/add_cart/" + pos,
//             type: "GET",
//             data: { csrfmiddlewaretoken: csrf },
//             success: function(data) {
//                 console.log(pos)
//             },
//             error: function(xhr, status, error) {
//                 console.log(xhr)
//                 var err = eval("(" + xhr.responseText + ")");
//                 alert(err.Message);
//             }
//         });
//     });
// });

jQuery(document).ready(function($) {
    var $form = $('#increment_form');

    $form.submit(function() {
        $.ajax({
            type: 'POST',
            url: $form.attr('action'),
            data: $form.serialize(),
            success: function(response) {
                $('body').html(response);
            }
        });

        return false;
    });
});