tg = Telegram.WebApp;

tg.BackButton.hide();

let currentStep = 1;
const totalSteps = 3;

function hide_el(el) {
    el.style.opacity = '0';
    setTimeout(() => {
        el.style.display = 'none';
    }, 300);
}

function show_el(el) {
    el.style.opacity = '0';
    setTimeout(() => {
        el.style.display = 'flex';
    }, 300);
    setTimeout(() => {
        el.style.opacity = '1';
    }, 300);
}

function next_step() {
    const next_step = document.getElementById(`step_${currentStep + 1}`)
    hide_el(document.getElementById(`step_${currentStep}`))
    show_el(next_step)
    currentStep++;

    if (currentStep > 1) {
        tg.BackButton.show();
    }
    tg.MainButton.hide();
}

function prev_step() {
    const prev_step = document.getElementById(`step_${currentStep - 1}`)
    hide_el(document.getElementById(`step_${currentStep}`))
    show_el(prev_step)
    currentStep--;

    tg.MainButton.hide();

    if (currentStep == 1) {
        tg.BackButton.hide();

        height = document.getElementById('height').value;
        weight = document.getElementById('weight').value;
        birthday = document.getElementById('birthday').value;

        if (height != '' && weight != '' && birthday != '') {
            tg.MainButton.show();
            tg.MainButton.setParams({
                text: 'Далее',
                color: '#8a50ff',
            });
            tg.MainButton.onClick(next_step);
        }
    }
}

function step1Check() {
    height = document.getElementById('height').value;
    weight = document.getElementById('weight').value;
    birthday = document.getElementById('birthday').value;
    any_selected_gender = document.querySelectorAll('.checkbox-btn.selected').length > 0;

    if (height != '' && weight != '' && birthday != '' && any_selected_gender) {
        tg.MainButton.show();
        tg.MainButton.setParams({
            text: 'Далее',
            color: '#8a50ff',
        });
        tg.MainButton.onClick(next_step);
    } else {
        tg.MainButton.hide();
    }
}

function save_data() {
    hide_el(document.getElementById(`step_${currentStep}`))
    show_el(document.getElementById('end'))
    currentStep++;

    tg.MainButton.hide();
    tg.BackButton.hide();
}

tg.onEvent('backButtonClicked', prev_step);


// handlers

document.addEventListener('input', function(event) {
    if (event.target.type === 'number') {
        event.target.value = event.target.value.replace(/[^0-9]/g, '');
    }

    step1Check();
});

document.querySelectorAll('.checkbox-btn').forEach(button => {
    button.addEventListener('click', function() {
        document.querySelectorAll('.checkbox-btn').forEach(btn => {
            btn.classList.remove('selected');
        });
        this.classList.add('selected');

        step1Check();
    });
});

document.querySelectorAll('.option-btn').forEach(button => {
    button.addEventListener('click', function() {
        stepRelation = this.classList[1];

        document.querySelectorAll(`.option-btn .${stepRelation}`).forEach(btn => {
            btn.classList.remove('selected');
        });
        this.classList.add('selected');

        if (currentStep < totalSteps) {
            next_step();
        } else {
            tg.MainButton.show();
            tg.MainButton.setParams({
                text: 'Составить план ✅',
                color: '#8a50ff',
            });
            tg.MainButton.onClick(save_data);
        }
    });
});