// static/js/auth.js

/**
 * Refresh access token using refresh token
 */
async function refreshAccessToken() {
    const refresh = localStorage.getItem("refresh");

    if (!refresh) {
        localStorage.clear();
        window.location.href = "/accounts/login/";
        return null;
    }

    const response = await fetch("/api/users/token/refresh/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh })
    });

    if (!response.ok) {
        localStorage.clear();
        window.location.href = "/accounts/login/";
        return null;
    }

    const data = await response.json();
    localStorage.setItem("access", data.access);
    return data.access;
}


/**
 * Fetch wrapper with auto-refresh
 */
async function fetchWithAuth(url, options = {}) {
    let token = localStorage.getItem("access");

    if (!token) {
        window.location.href = "/accounts/login/";
        return;
    }

    options.headers = {
        ...options.headers,
        Authorization: "Bearer " + token
    };

    let response = await fetch(url, options);

    if (response.status === 401) {
        const newAccess = await refreshAccessToken();
        if (!newAccess) return;

        options.headers.Authorization = "Bearer " + newAccess;
        response = await fetch(url, options);
    }

    return response;
}