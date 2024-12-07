import('/static/modules/popupControl.js').then(module => {
    window.popup = new module.Popup(document.getElementById('food-popup'))
});

tg = Telegram.WebApp;
mealName = document.querySelector('input[name="meal_name"]').value;

tg.BackButton.show();
tg.onEvent('backButtonClicked', function() {
    if (window.popup.isShow) {
        window.popup.hide();
        tg.MainButton.hide();
        return;
    }
    window.location.href = `/meal_time?meal=${mealName}`
});

tg.onEvent('mainButtonClicked', function() {
    window.navigator.vibrate(80);
    tg.MainButton.showProgress();

    weight = document.getElementById('weight').value ? document.getElementById('weight').value : 100;
    fetch('/api/add_food', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            date: new Date().toLocaleDateString('ru-RU'),
            product: {
                name: window.curentPopupData.name,
                calories: parseInt(window.curentPopupData.caloric),
                carbs: parseFloat(window.curentPopupData.carbon), 
                proteins: parseFloat(window.curentPopupData.protein),
                fats: parseFloat(window.curentPopupData.fat),
                weight: parseFloat(weight),
            },
            meal_time: mealName

        }),
        credentials: 'include'
    })
    .then(response => response.json())
    .then(data => {
        tg.MainButton.setParams({
            text: 'Добавлено!',
            color: '#2ecc71',
        });

        setTimeout(() => {
            window.popup.hide()
        }, 500);
    })

    document.getElementById('search').value = '';
    setRecentFood();
})

document.getElementById('food-popup').addEventListener('popupHide', function() {
    tg.MainButton.hide();
    tg.MainButton.hideProgress();

    delete window.curentPopupData;
    document.getElementById('weight').value = '';
});

function show_food_details(el) {
    document.getElementById('food-name-popup').innerHTML = el.getAttribute('name');
    document.getElementById('caloric-popup').innerHTML = el.getAttribute('caloric');
    document.getElementById('carbon-popup').innerHTML = el.getAttribute('carbon');
    document.getElementById('protein-popup').innerHTML = el.getAttribute('protein');
    document.getElementById('fat-popup').innerHTML = el.getAttribute('fat');

    window.curentPopupData = {
        name: el.getAttribute('name'),
        caloric: el.getAttribute('caloric'),
        carbon: el.getAttribute('carbon'),
        protein: el.getAttribute('protein'),
        fat: el.getAttribute('fat'),
    }

    window.popup.show(50);

    tg.MainButton.show();
    tg.MainButton.setParams({
        text: 'Добавить',
        color: '#8a50ff',
    });
}

function fill_list(data) {
    document.getElementById('food-list').innerHTML = '';
    if (data.length == 0) {
        const foodBlock = document.createElement('div');
        foodBlock.innerHTML = `
            <h4 style="text-align: center;">Ничего не найдено 😥</h4>
        `;
        document.getElementById('food-list').appendChild(foodBlock);
    }
    data.forEach(el => {
        const foodBlock = document.createElement('div');
        foodBlock.className = 'food-block';
        foodBlock.innerHTML = `
            <h4>${el.name}</h4>
            <span class="mini-subtitle">К:${el.caloric} 🍝:${el.carbon} 🥚:${el.protein} 🥑:${el.fat}</span>
        `;
        foodBlock.setAttribute('caloric', el.caloric ? el.caloric : 0);
        foodBlock.setAttribute('carbon', el.carbon ? el.carbon : 0);
        foodBlock.setAttribute('protein', el.protein ? el.protein : 0);
        foodBlock.setAttribute('fat', el.fat ? el.fat : 0);
        foodBlock.setAttribute('name', el.name);

        foodBlock.addEventListener('click', function() {
            show_food_details(this);
        });

        document.getElementById('food-list').appendChild(foodBlock);
    });
}

function setRecentFood() {
    document.getElementById('food-list').innerHTML = '';
    fetch('/api/get_recent_food', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'include'
    }).then(response => response.json())
    .then(data => {
        document.getElementById('food-list').innerHTML = '<h4 style="margin-bottom: 5%; margin-top: -5%;">Недавние продукты</h4>';
        data['data'][0].forEach(el => {
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

            foodBlock.addEventListener('click', function() {
                show_food_details(this);
            });

            document.getElementById('food-list').appendChild(foodBlock);
        });
    });
}


let searchTimeout;
const searchInput = document.getElementById('search');

searchInput.addEventListener('input', function() {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
        if(searchInput.value == '') {
            setRecentFood();
            return;
        }

        fetch(`/api/search?food_name=${searchInput.value}`)
        .then(response => response.json())
        .then(data => fill_list(data.data))
    }, 500);
});


document.getElementById('weight').addEventListener('input', function() {
    const weight = parseFloat(this.value) || 0;
    const nutrients = ['caloric', 'carbon', 'protein', 'fat'];
    nutrients.forEach(nutrient => {
        const element = document.getElementById(`${nutrient}-popup`);
        const originalValue = window.curentPopupData[nutrient];

        if(nutrient == 'caloric') {
            element.innerHTML = ((weight / 100) * originalValue).toFixed(0);
        } else {
            element.innerHTML = ((weight / 100) * originalValue).toFixed(1);
        }
    });
});


document.addEventListener('authComplete', function() {
    setRecentFood();
});