/* eslint-disable no-undef */
// import ymaps from 'ymaps';

function loadYamapsScript() {
  const yamapsAPI = document.createElement('script');
  yamapsAPI.src = 'https://api-maps.yandex.ru/2.1/?apikey=d7ff3169-1b40-44a9-bed3-e2401872434d&lang=ru_RU';
  yamapsAPI.type = 'text/javascript';
  document.head.appendChild(yamapsAPI);
}

export function initYamaps(){
  try {
    /* eslint-disable-next-line no-use-before-define */
    ymaps.ready(init);
    /* eslint-disable-next-line no-inner-declarations */
    function init(){
      const map = new ymaps.Map('map', {
        center: [55.59102192, 37.62740939],
        zoom: 14,
        height: 315-20
      });
      map.geoObjects
        .add(new ymaps.Placemark([55.59102192, 37.62740939], {
            balloonContent: '<strong>ПРОДЛОГИСТИКА ЮГ</strong>'
        }, {
            preset: 'islands#icon',
            iconColor: '#31ac53'
        }))
    }
  } catch (e){
    if (e.name === 'ReferenceError'){
      return false
    }
  }
  return ymaps
}

let YAMAPS_READY = false;
$('.tabs-slider').on('beforeChange', function(event, slick, _currentSlide, nextSlide){
  if (nextSlide === 2 && !YAMAPS_READY) {
    loadYamapsScript()
    const interval = setInterval(() => {
      YAMAPS_READY = initYamaps();
      if (YAMAPS_READY) clearInterval(interval);
    }, 100)
  }
});

