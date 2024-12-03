export class Popup {
    constructor(el, zIndex = 1) {
        this.element = el;
        this.element.style.position = 'fixed';
        this.element.style.left = '0';
        this.element.style.bottom = '-100%';
        this.element.style.width = '100%';
        this.element.style.height = '100%';
        this.element.style.zIndex = zIndex + 1;
        this.element.style.display = 'flex';
        this.element.style.transition = 'all 0.3s linear';
        this.popupBackdrop = null;
        this.isShow = false;
    }

    show(degree = 100) {
        // degree = `${100 - degree}%`;
        degree = `${degree}%`;
        this.element.style.bottom = 0;
        this.element.style.height = degree;

        this.popupBackdrop = document.createElement('div');
        this.popupBackdrop.style.position = 'fixed';
        this.popupBackdrop.style.left = '0';
        this.popupBackdrop.style.top = '0';
        this.popupBackdrop.style.width = '100%';
        this.popupBackdrop.style.height = '100%';
        this.popupBackdrop.style.zIndex = this.element.style.zIndex - 1;
        this.popupBackdrop.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        this.popupBackdrop.addEventListener('click', () => {
            this.hide();
        });
        document.body.appendChild(this.popupBackdrop);
        this.isShow = true;
    }

    hide() {
        if (this.popupBackdrop) {
            this.popupBackdrop.remove();
            this.popupBackdrop = null;
        }
        this.isShow = false;

        this.element.style.bottom = '-100%';
        this.element.style.height = '0';

        this.element.dispatchEvent(new Event('popupHide'));
    }
}