$(function() {

    $("#mycarousel").carousel({
    interval: 3000}); 

    $('.show-form').click(function() {
        $(this).next().slideToggle();
    });

    $('.show-review-form').click(function() {
        $('.review_form').slideDown();
        $(this).hide();
    });

    $('.fa-times').click(function() {
        $('.review_form').slideUp();
        $('.show-review-form').show();
    });

    $('.add_new_form_button').click(function() {
        $('.hidden-city').slideDown();
        $('.add_city').slideUp();
        $(this).hide();
    });

    $('.edit_past').click(function() {
        $('.edit__trip').toggle('show');
        $('.a-tag').toggle();
    });

    $('.a-tag').click(function() {
        $(this).parent().next().next().next().next().slideToggle();
    });

    $('.add_activity_button').click(function() {
        $('.add_activity_form').slideDown();
        $(this).hide();
    });

    $('.fa').click(function() {
        $('.add_activity_form').slideUp();
        $('.add_activity_button').slideDown();
    });


  /* ------- show review form ----------- */
  $('.edit_review').click(function() {
      $('.edit-review').slideToggle();
  });

  /* ------- user dashboard ------- */
  $('.user-edit-button').click(function(){
      $('.user-info-to-hide').toggle();
      $('.hidden-form').toggle();
  });

  // handle star clicks
  $('#star-one').click(function() {
      $('#star-one').attr('src', '/assets/img/star-gold.svg');
      $('#star-two').attr('src', '/assets/img/star-empty.svg');
      $('#star-three').attr('src', '/assets/img/star-empty.svg');
      $('#star-four').attr('src', '/assets/img/star-empty.svg');
      $('#star-five').attr('src', '/assets/img/star-empty.svg');
  });

  $('#star-two').click(function() {
      $('#star-one').attr('src', '/assets/img/star-gold.svg');
      $('#star-two').attr('src', '/assets/img/star-gold.svg');
      $('#star-three').attr('src', '/assets/img/star-empty.svg');
      $('#star-four').attr('src', '/assets/img/star-empty.svg');
      $('#star-five').attr('src', '/assets/img/star-empty.svg');
  });

  $('#star-three').click(function() {
      $('#star-one').attr('src', '/assets/img/star-gold.svg');
      $('#star-two').attr('src', '/assets/img/star-gold.svg');
      $('#star-three').attr('src', '/assets/img/star-gold.svg');
      $('#star-four').attr('src', '/assets/img/star-empty.svg');
      $('#star-five').attr('src', '/assets/img/star-empty.svg');
  });

  $('#star-four').click(function() {
      $('#star-one').attr('src', '/assets/img/star-gold.svg');
      $('#star-two').attr('src', '/assets/img/star-gold.svg');
      $('#star-three').attr('src', '/assets/img/star-gold.svg');
      $('#star-four').attr('src', '/assets/img/star-gold.svg');
      $('#star-five').attr('src', '/assets/img/star-empty.svg');
  });

  $('#star-five').click(function() {
      $('#star-one').attr('src', '/assets/img/star-gold.svg');
      $('#star-two').attr('src', '/assets/img/star-gold.svg');
      $('#star-three').attr('src', '/assets/img/star-gold.svg');
      $('#star-four').attr('src', '/assets/img/star-gold.svg');
      $('#star-five').attr('src', '/assets/img/star-gold.svg');
  });

  // // handle star hovers
  // $('#star-one').hover(function() {
  //     $('#star-one').attr('src', '/assets/img/star-gold.svg');
  // }, function() {
  //     $('#star-one').attr('src', '/assets/img/star-empty.svg');
  // });
  //
  // $('#star-two').hover(function() {
  //     $('#star-one').attr('src', '/assets/img/star-gold.svg');
  //     $('#star-two').attr('src', '/assets/img/star-gold.svg');
  // }, function() {
  //     $('#star-one').attr('src', '/assets/img/star-empty.svg');
  //     $('#star-two').attr('src', '/assets/img/star-empty.svg');
  // });
  //
  // $('#star-three').hover(function() {
  //     $('#star-one').attr('src', '/assets/img/star-gold.svg');
  //     $('#star-two').attr('src', '/assets/img/star-gold.svg');
  //     $('#star-three').attr('src', '/assets/img/star-gold.svg');
  // }, function() {
  //     $('#star-one').attr('src', '/assets/img/star-empty.svg');
  //     $('#star-two').attr('src', '/assets/img/star-empty.svg');
  //     $('#star-three').attr('src', '/assets/img/star-empty.svg');
  // });
  //
  // $('#star-four').hover(function() {
  //     $('#star-one').attr('src', '/assets/img/star-gold.svg');
  //     $('#star-two').attr('src', '/assets/img/star-gold.svg');
  //     $('#star-three').attr('src', '/assets/img/star-gold.svg');
  //     $('#star-four').attr('src', '/assets/img/star-gold.svg');
  // }, function() {
  //     $('#star-one').attr('src', '/assets/img/star-empty.svg');
  //     $('#star-two').attr('src', '/assets/img/star-empty.svg');
  //     $('#star-three').attr('src', '/assets/img/star-empty.svg');
  //     $('#star-four').attr('src', '/assets/img/star-empty.svg');
  // });
  //
  // $('#star-five').hover(function() {
  //     $('#star-one').attr('src', '/assets/img/star-gold.svg');
  //     $('#star-two').attr('src', '/assets/img/star-gold.svg');
  //     $('#star-three').attr('src', '/assets/img/star-gold.svg');
  //     $('#star-four').attr('src', '/assets/img/star-gold.svg');
  //     $('#star-five').attr('src', '/assets/img/star-gold.svg');
  // }, function() {
  //     $('#star-one').attr('src', '/assets/img/star-empty.svg');
  //     $('#star-two').attr('src', '/assets/img/star-empty.svg');
  //     $('#star-three').attr('src', '/assets/img/star-empty.svg');
  //     $('#star-four').attr('src', '/assets/img/star-empty.svg');
  //     $('#star-five').attr('src', '/assets/img/star-empty.svg');
  // });
});
