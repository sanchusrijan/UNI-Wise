console.log("upload.js loaded");

const uploadForm = document.getElementById("uploadForm");
const fileInput = document.getElementById("fileInput");
const statusPara = document.getElementById("status");

uploadForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    if (!fileInput.files.length) {
        statusPara.innerText = "Please select a file";
        return;
    }

    const token = localStorage.getItem("access");
    if (!token) {
        statusPara.innerText = "Please login again";
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    statusPara.innerText = "Uploading...";

    try {
        const response = await fetch("/api/users/fileupload/", {
            method: "POST",
            headers: {
                "Authorization": "Bearer " + token
            },
            body: formData
        });

        if (!response.ok) {
            throw new Error("Upload failed");
        }

        const data = await response.json();

        statusPara.innerText = "Upload successful! Document ID: " + data.id;

        // Optional: redirect after upload
        setTimeout(() => {
            window.location.href = "/summarize/web/";
        }, 1500);

    } catch (error) {
        console.error(error);
        statusPara.innerText = "Upload error";
    }
});