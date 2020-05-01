/* eslint-disable no-undef */
/* eslint-disable prefer-const */
/* eslint-disable func-names */
/* eslint-disable no-restricted-syntax */
/* eslint-disable no-prototype-builtins */

function debug(action, a, b) {
  console.log(
    action,
    `start: ${a}`,
    `current: ${b}`,
  )
}

let startScroll = window.pageYOffset - window.pageYOffset % 100;
document.addEventListener('DOMContentLoaded', function(){
  $(window).scroll(function(){
    let HEADER_TOP = 100;
    if( $(window).scrollTop() > HEADER_TOP ) {
      $('.header').addClass("slideup")
    } else {
      $('.header').removeClass("slideup")
    }

    let offset = 30;
    if (window.pageYOffset >= 0){
      if (window.pageYOffset - offset >= startScroll){
        $('.header-main').addClass("slideup");
        debug(' + hide', startScroll, window.pageYOffset);
        startScroll = window.pageYOffset;

      } else if (window.pageYOffset + offset <= startScroll) {
        $('.header-main').removeClass("slideup");
        debug(' - show', startScroll, window.pageYOffset);
        startScroll = window.pageYOffset;
      }
    }
  });
});
