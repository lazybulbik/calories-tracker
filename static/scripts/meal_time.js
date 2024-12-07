import ('/static/modules/popupControl.js').then(module => {
    window.popup = new module.Popup(document.getElementById('food-popup'))
    window.neuroPopup = new module.Popup(document.getElementById('neuro-popup'))
});

tg = Telegram.WebApp;
mealName = document.querySelector('input[name="meal_name"]').value;
tg.BackButton.show();

tg.onEvent('backButtonClicked', function() {
    if (window.neuroPopup.isShow) {
        window.neuroPopup.hide();
        return;
    }
    if (window.popup.isShow) {
        window.popup.hide();
        return;
    }
    window.location.href = '/';
});

// base 

tg.MainButton.show();
tg.MainButton.setParams({
    text: 'Добавить еду',
    color: '#8a50ff',
});

tg.MainButton.onClick(function() {
    window.location.href = `/add_food?meal=${mealName}`
});


function fillList(data) {
    document.getElementById('food-list').innerHTML = '';
    data.forEach(el => {
        const foodBlock = document.createElement('div');
        foodBlock.className = 'food-block';
        foodBlock.innerHTML = `
            <h4>${el.name}</h4>
            <span class="mini-subtitle">К:${el.calories} 🍝:${el.carbs} 🥚:${el.proteins} 🥑:${el.fats}</span>
        `;
        foodBlock.setAttribute('caloric', el.calories);
        foodBlock.setAttribute('carbon', el.carbs);
        foodBlock.setAttribute('protein', el.proteins);
        foodBlock.setAttribute('fat', el.fats);
        foodBlock.setAttribute('name', el.name);
        foodBlock.setAttribute('id', el.id);

        foodBlock.addEventListener('contextmenu', function(event) {
            event.preventDefault();
            window.navigator.vibrate(80);
            tg.showPopup({
                'title': "Удаление продукта",
                'message': "Вы действительно хотите удалить продукт?",
                'buttons': [{
                    'id': `delete-${foodBlock.getAttribute('id')}`,
                    'type': 'destructive',
                    'text': 'Удалить'
                },
                {
                    'id': 'cancel',
                    'type': 'cancel'
                }]
            })
        });

        document.getElementById('food-list').appendChild(foodBlock);
    });
}

// events

document.getElementById('upload-image').addEventListener('change', function() {
    document.getElementById('neuro-block').style.backgroundImage = 'radial-gradient(circle, #edff2c, #ffdc3b, #ffbc5c, #ffa37b, #ff9494)';
    setTimeout(() => {
        document.getElementById('neuro-block').style.backgroundImage = 'radial-gradient(circle, #2cff47, #81ff54, #adff65, #cfff7b, #e8ff94);'
    }, 500);
});

tg.onEvent('popupClosed', function(data) {
    if(data.button_id.startsWith('delete-')) {
        productId = data.button_id.replace('delete-', '');
        fetch(`/api/delete_food`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                food_id: productId,
                date: new Date().toLocaleDateString('ru-RU'),
                meal_time: mealName
            }),
            credentials: 'include'
        }).then(response => response.json())
        .then(data => {
            fillList(data['data'])
        })
    }
})


document.addEventListener('authComplete', function() {
    meal_names = {
        'breakfast': 'Завтрак',
        'lunch': 'Обед',
        'dinner': 'Ужин',
        'snack': 'Перекус'
    }
    document.getElementById('meal-name').innerHTML = meal_names[mealName];

    const date = new Date().toLocaleDateString('ru-RU')
    fetch(`/api/get_user_data?date=${date}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'include'
    }).then(response => response.json())
    .then(data => {
        window.mealData = data;
        fillList(data['data']['meal'][mealName]);
    })
})