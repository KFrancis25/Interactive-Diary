document.addEventListener('DOMContentLoaded', () => {
    const gridItems = document.querySelectorAll('.grid-item'); // Selecting all sticky notes
    const modal = document.getElementById('note-modal'); // Modal for diary entry
    const noteText = document.getElementById('note-text'); // Text area for diary entry
    const saveNoteButton = document.getElementById('save-note'); // Button to save the entry
    const closeModalButton = document.getElementById('close-modal'); // Button to close the modal

    let activeNoteId = null;

    // When a sticky note is clicked, open the modal and load saved data (if any)
    gridItems.forEach(item => {
        item.addEventListener('click', () => {
            activeNoteId = item.getAttribute('data-note'); // Get the ID of the clicked sticky note
            const savedNote = localStorage.getItem(`diary-note-${activeNoteId}`) || ''; // Retrieve saved note if available
            noteText.value = savedNote; // Set the value in the text area
            modal.style.display = 'block'; // Show the modal
        });
    });

    // Save the note to localStorage
    saveNoteButton.addEventListener('click', () => {
        if (activeNoteId) {
            localStorage.setItem(`diary-note-${activeNoteId}`, noteText.value); // Save the note to localStorage
            alert('Diary entry saved!'); // Notify the user
            modal.style.display = 'none'; // Hide the modal
        }
    });

    // Close the modal without saving
    closeModalButton.addEventListener('click', () => {
        modal.style.display = 'none'; // Hide the modal when "Close" is clicked
    });
});
