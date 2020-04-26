$(window).on('load', function onload() {
  const $preloader = $('.preloader');
  const svgAnm = $preloader.find('.svg_anm');
  svgAnm.fadeOut();
  $preloader.delay(1).fadeOut('fast');
});