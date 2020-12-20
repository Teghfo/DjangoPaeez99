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



// jQuery(document).ready(function($) {
//     var $form = $('#increment_form');

//     $form.submit(function() {
//         $.ajax({
//             type: 'POST',
//             url: $form.attr('action'),
//             data: $form.serialize(),
//             success: function(response) {
//                 $('body').html(response);
//             }
//         });

//         return false;
//     });
// });

$(document).ready(function() {


    $(".add-cart-product-btn").on("click", function(event) {
        event.preventDefault();
        var csrf = $("input").parent().find("input[name='csrfmiddlewaretoken']").val();

        var $link = $(event.currentTarget);
        var productId = $link.attr("data")
        var pathSend = document.location.href.replace(document.location.pathname, "/cart/add_cart/" + productId)

        $.ajax({
            url: pathSend,
            type: "POST",
            data: {
                csrfmiddlewaretoken: csrf
            },
            success: function(response) {
                var $res = $(response).find(`.${productId}`).text()
                var $sumPrice = $(response).find(`.sum-price-${productId}`).text()
                var $sumAllPrice = $(response).find("#sum-of-all-food").text()
                $(`.${productId}`).html($res)
                $(`.sum-price-${productId}`).html($sumPrice)
                $("#sum-of-all-food").html($sumAllPrice)

            },
            error: function(xhr, status, error) {
                var err = eval("(" + xhr.responseText + ")");
                alert(err.Message);
            }
        });

    })


    $(".dec-cart-product-btn").on("click", function(event) {
        event.preventDefault();
        var csrf = $("input").parent().find("input[name='csrfmiddlewaretoken']").val();

        var $link = $(event.currentTarget);
        var productId = $link.attr("data")
        var pathSend = document.location.href.replace(document.location.pathname, "/cart/decrement_cart/" + productId)

        $.ajax({
            url: pathSend,
            type: "POST",
            data: {
                csrfmiddlewaretoken: csrf
            },
            success: function(response) {
                var $res = $(response).find(`.${productId}`).text()
                var $sumPrice = $(response).find(`.sum-price-${productId}`).text()
                var $sumAllPrice = $(response).find("#sum-of-all-food").text()
                if ($res === "") {
                    $('body').html(response);
                } else {

                    $(`.${productId}`).html($res)
                    $(`.sum-price-${productId}`).html($sumPrice)
                    $("#sum-of-all-food").html($sumAllPrice)
                }
            },
            error: function(xhr, status, error) {
                var err = eval("(" + xhr.responseText + ")");
                alert(err.Message);
            }
        });

    })


    $(".remove-cart-product-btn").on("click", function(event) {
        event.preventDefault();
        var csrf = $("input").parent().find("input[name='csrfmiddlewaretoken']").val();

        var $link = $(event.currentTarget);
        var productId = $link.attr("data")
        var pathSend = document.location.href.replace(document.location.pathname, "/cart/delete_from_cart/" + productId)

        $.ajax({
            url: pathSend,
            type: "POST",
            data: {
                csrfmiddlewaretoken: csrf
            },
            success: function(response) {
                $('body').html(response);

            },
            error: function(xhr, status, error) {
                console.log(xhr)
                var err = eval("(" + xhr.responseText + ")");
                alert(err.Message);
            }
        });

    })
})