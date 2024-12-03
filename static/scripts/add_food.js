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

document.getElementById('food-popup').addEventListener('popupHide', function() {
    tg.MainButton.hide();

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
        foodBlock.setAttribute('caloric', el.caloric);
        foodBlock.setAttribute('carbon', el.carbon);
        foodBlock.setAttribute('protein', el.protein);
        foodBlock.setAttribute('fat', el.fat);
        foodBlock.setAttribute('name', el.name);

        foodBlock.addEventListener('click', function() {
            show_food_details(this);
        });

        document.getElementById('food-list').appendChild(foodBlock);
    });
}


let searchTimeout;
const searchInput = document.getElementById('search');

searchInput.addEventListener('input', function() {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
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
        element.innerHTML = ((weight / 100) * originalValue).toFixed(2);
    });
});