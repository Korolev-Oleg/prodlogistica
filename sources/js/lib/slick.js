import "slick-carousel/slick/slick"

$(document).ready(function(){
  $('.tabs-slider').slick({
    dots: true,
    // infinite: true,
    speed: 125,
    fade: true,
    cssEase: 'linear',
    draggable: false
  });

  $('.clients-slider').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1800,
    // centerMode: true,
    infinite: true,
    speed: 300,
    responsive: [
    {
      breakpoint: 1140,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 1,
        centerMode: false
      }
    },
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        centerMode: false
      }
    },
    {
      breakpoint: 767,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        centerMode: false
      }
    },
    {
      breakpoint: 540,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1,
        centerMode: false
      }
    }]
  });
});
