/* eslint-disable func-names */
/* eslint-disable prefer-const */
import Slideout from 'slideout';

// let largeDisplay = 991
const slideout = new Slideout({
  'panel': document.getElementsByClassName('content').item(0),
  'menu': document.getElementById('menu'),
  'padding': 256,
  'tolerance': 70,
  'fx': 'ease-in-out'
});
// // eslint-disable-next-line func-names
$('.toggle-button').on('click', function() {
  slideout.toggle()
});

$('.close-button').on('click', function() {
  slideout.toggle()
});
