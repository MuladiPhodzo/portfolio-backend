    function toggleForm() {
        var form = document.getElementById('contact-form');
        // Toggle the form visibility
        if (form.style.display === 'none' || form.style.display === '') {
            form.style.display = 'block';
        } else {
            form.style.display = 'none';
        }
    }

