function parseHashParams() {
    const hash = window.location.hash.substr(1); // Убираем #
    const params = {};
    hash.split('&').forEach(pair => {
        const [key, value] = pair.split('=');
        params[decodeURIComponent(key)] = decodeURIComponent(value);
    });
    return params;
}

fetch('/api/auth', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        data_check_string: parseHashParams()
    }),
    credentials: 'include'
}).then(response => response.json())
.then(data => {
    if (data['status'] == 'need_register') {
        window.location.href = '/register'
    }
})