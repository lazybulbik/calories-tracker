tg = Telegram.WebApp;

tg.BackButton.show();
tg.onEvent('backButtonClicked', function() {
    window.history.back();
});

tg.MainButton.show();
tg.MainButton.setParams({
    text: 'Супер 👍',
    color: '#8a50ff',
});
tg.MainButton.onClick(function() {
    window.location.href = '/';
});

document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/get_plan', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'include'
    }).then(response => response.json())
    .then(data => {
        data['data'].forEach(element => {            
            let weakBlock = document.createElement('div');
            weakBlock.classList.add('weak-plan');

            if(data['data'].indexOf(element) % 2 != 0) {
                weakBlock.style.textAlign = 'right';
            }
    
            let header = document.createElement('h3');
            header.innerHTML = `Неделя ${element['weak']}`; 

            let calls = document.createElement('span');
            calls.classList.add('weak-nutrient');
            calls.innerHTML = `Каллории: ${element['callories']}`;

            let carbohydrates = document.createElement('span');
            carbohydrates.classList.add('weak-nutrient');
            carbohydrates.innerHTML = `Углеводы: ${element['carbs']}`;            

            let proteins = document.createElement('span');
            proteins.classList.add('weak-nutrient');
            proteins.innerHTML = `Белки: ${element['protein']}`;

            let fats = document.createElement('span');
            fats.classList.add('weak-nutrient');
            fats.innerHTML = `Жиры: ${element['fats']}`;

            weakBlock.appendChild(header);
            weakBlock.appendChild(calls);
            weakBlock.appendChild(carbohydrates);
            weakBlock.appendChild(proteins);
            weakBlock.appendChild(fats);
            document.getElementById('weaks-list').appendChild(weakBlock);
        });
    })
})