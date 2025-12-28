document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('quiz-form');
    const loadingOverlay = document.getElementById('loading-overlay');
    const fileInput = document.querySelector('input[type="file"]');
    const fileLabel = document.querySelector('.file-upload-label span');

    // Handle file input change to show filename
    if (fileInput) {
        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                fileLabel.textContent = e.target.files[0].name;
            } else {
                fileLabel.textContent = 'Choose PDF File';
            }
        });
    }

    // Handle form submission
    if (form) {
        form.addEventListener('submit', (e) => {
            // Show loading state
            loadingOverlay.classList.remove('hidden');
            
            // Add a small delay to allow the UI to update/files to start uploading visually if needed
            // The form will submit naturally, causing a page reload with results.
            // If we were using AJAX, we would preventDefault here.
        });
    }

    // Smooth scroll to results if they exist
    const results = document.getElementById('results-section');
    if (results) {
        results.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
});
