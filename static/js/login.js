
const loginForm = document.getElementById("loginForm");
const statusPara = document.getElementById("status");

loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!email || !password) {
        statusPara.innerText = "Please enter email and password";
        return;
    }

    statusPara.innerText = "Logging in...";

    try {
        const response = await fetch("/api/users/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        if (!response.ok) {
            throw new Error("Invalid credentials");
        }

        const data = await response.json();

        localStorage.setItem("access", data.access);
        localStorage.setItem("refresh", data.refresh);

        statusPara.innerText = "Login successful";
        window.location.href = "/users/home/";

    } catch (error) {
        statusPara.innerText = "Login failed. Check credentials.";
        console.error(error);
    }
});

const registerBtn = document.getElementById("registerBtn");

if (registerBtn) {
    registerBtn.addEventListener("click", () => {
        window.location.href = "/accounts/register/";
    });
}