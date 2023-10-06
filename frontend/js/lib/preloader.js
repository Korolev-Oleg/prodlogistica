/**
 * Preloader function
 */
$(window).on('load', function onload() {
  const $preloader = $('.preloader');
  const svgAnm = $preloader.find('.svg_anm');
  svgAnm.fadeOut();
  $preloader.delay(1).fadeOut('fast');
  setWhiteCoverWidth()
});

/**
 * function get max page height and set this to #white-cover block
 */
function setWhiteCoverWidth(){
  let body = document.body,
      html = document.documentElement;

  let pageHeight = Math.max( body.scrollHeight, body.offsetHeight,
                             html.clientHeight, html.scrollHeight, html.offsetHeight );
  document.getElementById('white-cover').style.height = String(pageHeight) + 'px'
}
