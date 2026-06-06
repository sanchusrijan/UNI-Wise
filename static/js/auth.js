async function refreshAccessToken() {
    const refresh = localStorage.getItem("refresh");
    if (!refresh) {
        return null;
    }
    try {
        const response = await fetch("/api/users/token/refresh/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ refresh })
        });
        if (!response.ok) {
            return null;
        }
        const data = await response.json();
        localStorage.setItem("access", data.access);
        return data.access;
    } catch (error) {
        console.error("Token refresh failed:", error);
        return null;
    }
}

async function fetchWithAuth(url, options = {}) {
    let access = localStorage.getItem("access");
    if (!access) {
        access = await refreshAccessToken();
        if (!access) {
            logoutUser();
            return;
        }
    }
    options.headers = {
        ...(options.headers || {}),
        "Authorization": "Bearer " + access
    };
    let response = await fetch(url, options);
    if (response.status === 401) {
        const newAccess = await refreshAccessToken();
        if (!newAccess) {
            logoutUser();
            return;
        }
        options.headers.Authorization = "Bearer " + newAccess;
        response = await fetch(url, options);
    }
    return response;
}

async function initializeAuth() {
    const access = localStorage.getItem("access");
    const refresh = localStorage.getItem("refresh");
    if (!refresh) {
        redirectToLogin();
        return;
    }
    if (!access) {
        const newAccess = await refreshAccessToken();
        if (!newAccess) {
            logoutUser();
        }
    }
}

function redirectToLogin() {
    window.location.href = "/accounts/login/";
}

function logoutUser() {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    redirectToLogin();
}

document.addEventListener("DOMContentLoaded", () => {
    initializeAuth();
});