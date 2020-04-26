import Popup from "popup-simple/src/main";

const popupF = new Popup();
popupF.init();

const feedFrame = {
  aSrc: 'https://yastatic.net/q/forms-frontend-ext/_/embed.js',
  fSrc: 'https://forms.yandex.ru/u/5e977b9b52be132a001fbfe2/?iframe=1',
  fName: 'ya-form-5e977b9b52be132a001fbfe2',
};

const feedbackCreate = (obj, params) => {
  const formApi = document.createElement('script');
  const iframe = document.createElement('iframe');
  formApi.src = obj.aSrc;
  formApi.type = 'text/javascript';
  formApi.id = 'yaFormApi';
  iframe.src = obj.fSrc;
  iframe.frameBorder = "0";
  iframe.name = obj.fName;
  iframe.id = 'yaIframe';
  iframe.width = `${getFormWidth()}`;

  if (params) iframe.src += `&${params}`;

  yandex__form.append(formApi, iframe);
};

footer_mail.onclick = () => {
  popupF.openTarget(popupF);
};

popupF.onOpen = () => {
  feedbackCreate(feedFrame)
};

popupF.onClose = () => {
  yaFormApi.remove();
  yaIframe.remove();
};

const getFormWidth = () => {
  if (window.innerWidth > window.innerHeight) return 473;
  return window.innerWidth * 0.95
};
