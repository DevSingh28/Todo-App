    const editForms = document.querySelectorAll('.edit-form');

    editForms.forEach(form => {
        const editInput = form.querySelector('.edit-input');
        const editToggleBtn = form.querySelector('.edit-toggle-btn');
        const editSubmitBtn = form.querySelector('.edit-submit-btn');

        editInput.style.display = 'none';
        editSubmitBtn.style.display = 'none';

        editToggleBtn.addEventListener('click', () => {
            if (editInput.style.display === 'none') {
                editInput.style.display = 'inline-block';
                editSubmitBtn.style.display = 'inline-block';
                editToggleBtn.style.display = 'none';
            } else {
                editInput.style.display = 'none';
                editSubmitBtn.style.display = 'none';
                editToggleBtn.style.display = 'inline-block';
            }
        });
    });
