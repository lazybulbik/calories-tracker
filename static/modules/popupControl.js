export class Popup {
    constructor(el, zIndex = 1) {
        this.element = el;
        this.element.style.position = 'fixed';
        this.element.style.left = '0';
        this.element.style.bottom = '-100%';
        this.element.style.width = '100%';
        this.element.style.height = '100%';
        this.element.style.zIndex = zIndex;
        this.element.style.transition = 'all 0.3s ease-in-out';
    }

    show(degree = 100) {
        degree = `${100 - degree}%`;
        this.element.style.bottom = 0;
        this.element.style.height = degree;
    }

    hide() {
        this.element.style.bottom = '-100%';
        this.element.style.height = '0';
    }
}