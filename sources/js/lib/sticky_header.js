/* eslint-disable no-undef */
/* eslint-disable prefer-const */
/* eslint-disable func-names */
/* eslint-disable no-restricted-syntax */
/* eslint-disable no-prototype-builtins */
document.addEventListener('DOMContentLoaded', function(){
  $(window).scroll(function(){
    const HEADER_TOP = 100    
    if( $(window).scrollTop() > HEADER_TOP + 0 ) {
      $('.header').addClass("slideup")
    } else {
      $('.header').removeClass("slideup")
    }
  });
});