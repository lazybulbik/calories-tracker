function parseHashParams() {
    const hash = window.location.hash.substr(1); // Убираем #
    const params = {};
    hash.split('&').forEach(pair => {
        const [key, value] = pair.split('=');
        params[decodeURIComponent(key)] = decodeURIComponent(value);
    });
    return params;
}

async function authenticate() {
    const response = await fetch('/api/auth', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            data_check_string: parseHashParams()
        }),
        credentials: 'include'
    });

    const data = await response.json();

    if (data['status'] === 'need_register') {
        window.location.href = '/register';
    }

    if (data['status'] === 'ok') {
        setTimeout(() => {
            let event = new Event('authComplete')
            document.dispatchEvent(event);
        }, 500);
    }
}

authenticate();
