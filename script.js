// Helper function to redirect to different pages
function redirectTo(page) {
    window.location.href = page;
}

// Login Form Logic
const loginForm = document.getElementById('login-form');
if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = document.getElementById('login-email').value;
        localStorage.setItem('user-email', email);
        redirectTo('index.html');
    });
}

// Signup Form Logic
const signupForm = document.getElementById('signup-form');
if (signupForm) {
    signupForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('signup-name').value;
        const email = document.getElementById('signup-email').value;
        localStorage.setItem('user-name', name);
        localStorage.setItem('user-email', email);
        redirectTo('index.html');
    });
}

// Account Page Logic
const userNameSpan = document.getElementById('user-name');
if (userNameSpan) {
    const userName = localStorage.getItem('user-name');
    userNameSpan.textContent = userName || 'Guest';
}

const logoutButton = document.getElementById('logout-button');
if (logoutButton) {
    logoutButton.addEventListener('click', () => {
        localStorage.clear();
        redirectTo('login.html');
    });
}

// Diary Grid Logic (For Home Page)
const diaryGrid = document.getElementById('diary-grid');
if (diaryGrid) {
    for (let i = 1; i <= 8; i++) {
        const tile = document.createElement('div');
        tile.classList.add('grid-item');
        tile.textContent = `Page ${i}`;
        tile.addEventListener('click', () => openNoteModal(i));
        diaryGrid.appendChild(tile);
    }
}

const noteModal = document.querySelector('.note-modal');
const noteHeading = document.getElementById('note-heading');
const noteText = document.getElementById('note-text');
const saveButton = document.getElementById('save-button');
const closeButton = document.getElementById('close-button');

let activeTileId = null;

function openNoteModal(id) {
    activeTileId = id;
    const savedHeading = localStorage.getItem(`heading-${id}`) || '';
    const savedNote = localStorage.getItem(`note-${id}`) || '';

    noteHeading.value = savedHeading;
    noteText.value = savedNote;
    noteModal.classList.remove('hidden');
}

saveButton.addEventListener('click', () => {
    const heading = noteHeading.value;
    const note = noteText.value;

    if (activeTileId !== null) {
        localStorage.setItem(`heading-${activeTileId}`, heading);
        localStorage.setItem(`note-${activeTileId}`, note);
        alert('Note saved!');
        noteModal.classList.add('hidden');
    }
});

closeButton.addEventListener('click', () => {
    noteModal.classList.add('hidden');
});


const maleButton = document.querySelector('.male');
const femaleButton = document.querySelector('.female');

maleButton.addEventListener('click', () => {
    maleButton.classList.add('active');
    femaleButton.classList.remove('active');
});

femaleButton.addEventListener('click', () => {
    femaleButton.classList.add('active');
    maleButton.classList.remove('active');
});

const form = document.querySelector('.info-form');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const birthdateInput = document.getElementById('birthdate');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const userInfo = {
        name: nameInput.value,
        email: emailInput.value,
        password: passwordInput.value,
        birthdate: birthdateInput.value,
    };
    console.log('User Information:', userInfo);
    alert('Information saved successfully!');
});

function redirectToHome() {
    window.location.href = 'demo.html'; // Redirects to home page
}

// const gridItems = document.querySelectorAll('.grid-item');

// // Add a click event to each grid tile
// gridItems.forEach((item, index) => {
//     item.addEventListener('click', () => {
//         alert(`You clicked on Page ${index + 1}`);
//     });
// });

// const gridItems = document.querySelectorAll('.grid-item');
// const modal = document.getElementById('note-modal');
// const noteText = document.getElementById('note-text');
// const saveNoteButton = document.getElementById('save-note');
// const closeModalButton = document.getElementById('close-modal');

// let activeNoteId = null;

// // Open the modal when a sticky note is clicked
// gridItems.forEach(item => {
//     item.addEventListener('click', () => {
//         activeNoteId = item.getAttribute('data-note');
//         const savedNote = localStorage.getItem(`note-${activeNoteId}`) || '';
//         noteText.value = savedNote;
//         modal.style.display = 'block';
//     });
// });

// // Save the note to localStorage
// saveNoteButton.addEventListener('click', () => {
//     if (activeNoteId) {
//         localStorage.setItem(`note-${activeNoteId}`, noteText.value);
//         alert('Note saved!');
//         modal.style.display = 'none';
//     }
// });

// // Close the modal without saving
// closeModalButton.addEventListener('click', () => {
//     modal.style.display = 'none';
// });

document.addEventListener('DOMContentLoaded', () => {
    const gridItems = document.querySelectorAll('.grid-item');
    const modal = document.getElementById('note-modal');
    const noteText = document.getElementById('note-text');
    const saveNoteButton = document.getElementById('save-note');
    const closeModalButton = document.getElementById('close-modal');

    let activeNoteId = null;

    // Open the modal when a sticky note is clicked
    gridItems.forEach(item => {
        item.addEventListener('click', () => {
            activeNoteId = item.getAttribute('data-note');
            const savedNote = localStorage.getItem(`note-${activeNoteId}`) || '';
            noteText.value = savedNote;
            modal.style.display = 'block';
        });
    });

    // Save the note to localStorage
    saveNoteButton.addEventListener('click', () => {
        if (activeNoteId) {
            localStorage.setItem(`note-${activeNoteId}`, noteText.value);
            alert('Note saved!');
            modal.style.display = 'none';
        }
    });

    // Close the modal without saving
    closeModalButton.addEventListener('click', () => {
        modal.style.display = 'none';
    });
});
