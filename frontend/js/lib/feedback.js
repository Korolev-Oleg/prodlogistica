import Popup from "popup-simple/src/main";

const popup = new Popup();

// Данные для яндекс формы
export const feedFrame = {
  aSrc: 'https://yastatic.net/q/forms-frontend-ext/_/embed.js',
  fSrc: 'https://forms.yandex.ru/u/5e977b9b52be132a001fbfe2/?iframe=1',
  fName: 'ya-form-5e977b9b52be132a001fbfe2',
};

/**
 * Генератор яндекс формы
 * @param popup - html объект в который втавляется форма
 */
export const generateForm = (popup) => {
  const attributes = popup.attributes;
  const formApi = document.createElement('script');
  const iframe = document.createElement('iframe');

  formApi.src = attributes['data-script'].value;
  formApi.type = 'text/javascript';
  formApi.id = 'yaFormApi';
  iframe.src = attributes['data-form-src'].value;
  iframe.frameBorder = "0";
  iframe.name = attributes['data-form-name'].value;
  iframe.id = 'yaIframe';
  iframe.width = `${getFormWidth()}`;

  // значения полей передаются через get запрос
  // if (params) iframe.src += `&${params}`;

  popup.getElementsByClassName('frame_content')[0].append(formApi, iframe);
};

popup.onOpen = () => {
  let id = popup.popup.attributes['id'].value;
  if (id === 'yandex__form') generateForm(popup.popup)
};

popup.onClose = () => {
  document.getElementsByClassName('frame_content')[0].innerHTML = '';
};

const getFormWidth = () => {
  if (window.innerWidth > window.innerHeight) return 473;
  return window.innerWidth * 0.90 - 19
};

popup.init();
