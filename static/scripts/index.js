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
    hide_el(document.getElementById('block-screen'));

    const date = new Date();
    const day = `0${date.getDate()}`.slice(-2);
    const month = `0${date.getMonth() + 1}`.slice(-2);
    const year = date.getFullYear();
    const currentDate = `${day}.${month}.${year}`;
    fetch(`/api/get_user_data?date=${currentDate}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'include'
    }).then(response => response.json())
    .then(data => {
        window.mealData = data['meals'];

        need_calls = data['data']['daily_plan']['callories'];
        need_carbs = data['data']['daily_plan']['carbs'];
        need_proteins = data['data']['daily_plan']['protein'];
        need_fats = data['data']['daily_plan']['fats'];

        if (data['meals']) {
            curent_calls = data['meals']['callories'];
            curent_carbs = data['meals']['carbs'];
            curent_proteins = data['meals']['protein'];
            curent_fats = data['meals']['fats'];
        } else {
            curent_calls = 0;
            curent_carbs = 0;
            curent_proteins = 0;
            curent_fats = 0;
        }

        document.getElementById('calories').innerHTML = `${curent_calls}/${need_calls}`;
        document.getElementById('carbs').innerHTML = `${curent_carbs}/${need_carbs}`;
        document.getElementById('proteins').innerHTML = `${curent_proteins}/${need_proteins}`;
        document.getElementById('fats').innerHTML = `${curent_fats}/${need_fats}`;

        document.getElementById('calories-bar').style.width = `${(curent_calls / need_calls) * 100}%`;
        document.getElementById('carbs-bar').style.width = `${(curent_carbs / need_carbs) * 100}%`;
        document.getElementById('proteins-bar').style.width = `${(curent_proteins / need_proteins) * 100}%`;
        document.getElementById('fats-bar').style.width = `${(curent_fats / need_fats) * 100}%`;
    })
})