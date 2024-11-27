tg = window.Telegram.WebApp;
import('/static/modules/popupControl.js').then(module => {
    window.popup = new module.Popup(document.getElementById('popup'))
})

tg.BackButton.hide();

function hide_el(el) {
    el.style.opacity = '0';
    setTimeout(() => {
        el.style.display = 'none';
    }, 300);
}

document.addEventListener('authComplete', () => {
    console.log('authComplete');
    hide_el(document.getElementById('block-screen'));
})