import "slick-carousel/slick/slick"

$(document).ready(function(){
  $('.tabs-slider').slick({
    dots: true,
    // infinite: true,
    customPaging: (slider, i) => {
      var html;
      html = '<button class="tab">';
      html += slider.$slides[i].children[0].children[0].getAttribute('title');
      html += '</button>';
      html += '<div class="slick-corner"></div>';
      return html;
    },
    speed: 125,
    fade: true,
    cssEase: 'linear',
    draggable: false,
    initialSlide: 1
  });

  $('.clients-slider').slick({
    slidesToShow: 5,
    slidesToScroll: 2,
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
        centerMode: false
      }
    },
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 4,
        centerMode: false
      }
    },
    {
      breakpoint: 767,
      settings: {
        slidesToShow: 4,
        centerMode: false
      }
    },
    {
      breakpoint: 540,
      settings: {
        slidesToShow: 3,
        centerMode: false
      }
    }]
  });
});
