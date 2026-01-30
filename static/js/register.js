const form = document.getElementById("registerForm");
const status = document.getElementById("status");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    status.innerText = "Registering...";

    try {
        const response = await fetch("/api/users/register/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name,
                email,
                password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Registration failed");
        }

        status.innerText = "Registration successful. Redirecting...";

        setTimeout(() => {
            window.location.href = "/accounts/login/";
        }, 1500);

    } catch (error) {
        status.innerText = error.message;
    }
});