import ('/static/modules/popupControl.js').then(module => {
    window.popup = new module.Popup(document.getElementById('food-popup'))
});

tg = Telegram.WebApp;
mealName = document.querySelector('input[name="meal_name"]').value;
tg.BackButton.show();

tg.onEvent('backButtonClicked', function() {
    if (window.popup.isShow) {
        window.popup.hide();
        return;
    }
    window.location.href = '/';
});

tg.MainButton.show();
tg.MainButton.setParams({
    text: 'Добавить еду',
    color: '#8a50ff',
});
tg.MainButton.onClick(function() {
    window.location.href = `/add_food?meal=${mealName}`
});


document.addEventListener('authComplete', function() {
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
        window.mealData = data;
    })
})