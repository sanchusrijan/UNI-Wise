console.log("Summarize JS loaded");

// ===== ELEMENTS =====
const documentList = document.getElementById("documentList");
const summarizeBtn = document.getElementById("summarizeBtn");
const statusPara = document.getElementById("status");
const summaryOutput = document.getElementById("summaryOutput");

const dropZone = document.getElementById("dropZone");
const fileInput = document.getElementById("fileInput");

// ===== STATE =====
let selectedDocumentId = null;

// ===== LOAD USER DOCUMENTS =====
async function loadDocuments() {
    try {
        const response = await fetchWithAuth("/api/users/getdocuments/");
        const data = await response.json();

        documentList.innerHTML = "";

        if (!data.files.length) {
            const li = document.createElement("li");
            li.innerText = "No documents uploaded";
            li.classList.add("empty");
            documentList.appendChild(li);
            return;
        }

        data.files.forEach(doc => {
            const li = document.createElement("li");
            li.innerText = doc.title;
            li.dataset.id = doc.id;

            li.onclick = () => selectDocument(doc.id, li);

            documentList.appendChild(li);
        });

    } catch (error) {
        console.error("Failed to load documents", error);
        statusPara.innerText = "Could not load documents";
    }
}

// ===== SELECT DOCUMENT =====
function selectDocument(docId, element) {
    selectedDocumentId = docId;

    document.querySelectorAll("#documentList li")
        .forEach(li => li.classList.remove("active"));

    element.classList.add("active");

    summarizeBtn.disabled = false;
    statusPara.innerText = "Document selected";
}

// ===== UPLOAD HANDLING =====
dropZone.onclick = () => fileInput.click();

dropZone.ondragover = (e) => {
    e.preventDefault();
    dropZone.classList.add("drag-over");
};

dropZone.ondragleave = () => {
    dropZone.classList.remove("drag-over");
};

dropZone.ondrop = async (e) => {
    e.preventDefault();
    dropZone.classList.remove("drag-over");

    const file = e.dataTransfer.files[0];
    if (file) {
        await uploadAndSelect(file);
    }
};

fileInput.onchange = async () => {
    if (fileInput.files.length) {
        await uploadAndSelect(fileInput.files[0]);
    }
};

// ===== UPLOAD + AUTO SELECT =====
async function uploadAndSelect(file) {
    statusPara.innerText = "Uploading document...";
    summaryOutput.innerText = "";

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetchWithAuth("/api/users/fileupload/", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        selectedDocumentId = data.id;
        summarizeBtn.disabled = false;

        statusPara.innerText = "Upload successful. Ready to summarize.";

        await loadDocuments();

    } catch (error) {
        console.error("Upload failed", error);
        statusPara.innerText = "Upload failed";
    }
}

// ===== SUMMARIZE =====
summarizeBtn.onclick = async () => {
    if (!selectedDocumentId) {
        statusPara.innerText = "Please select or upload a document";
        return;
    }

    statusPara.innerText = "Summarizing...";
    summaryOutput.innerText = "";

    try {
        const response = await fetchWithAuth(
            `/summarize/summarizedocument/${selectedDocumentId}/`,
            { method: "POST" }
        );

        const data = await response.json();

        summaryOutput.innerText = data.summary;
        statusPara.innerText = data.cached
            ? "Summary loaded from cache"
            : "Summary generated";

    } catch (error) {
        console.error("Summarization failed", error);
        statusPara.innerText = "Failed to summarize";
    }
};

// ===== INIT =====
loadDocuments();