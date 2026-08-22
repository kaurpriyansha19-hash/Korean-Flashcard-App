let currentCards = [];
let currentIndex = 0;

async function loadCards(category = 'All') {
    try {
        const url = category === 'All' ? '/api/cards' : `/api/cards?category=${category}`;
        const response = await fetch(url);
        currentCards = await response.json();
        currentIndex = 0;

        document.getElementById('card').classList.remove('flipped');
        
        if (currentCards.length > 0) {
            displayCard();
        } else {
            showEmptyState();
        }
    } catch (error) {
        console.error('Error fetching cards:', error);
    }
}

function displayCard() {
    const card = currentCards[currentIndex];
    document.getElementById('cardCategory').textContent = card.category;
    document.getElementById('koreanWord').textContent = card.korean;
    document.getElementById('englishWord').textContent = card.english;
    document.getElementById('cardTracker').textContent = `Card ${currentIndex + 1} of ${currentCards.length}`;
}

function showEmptyState() {
    document.getElementById('cardCategory').textContent = 'None';
    document.getElementById('koreanWord').textContent = 'No Cards';
    document.getElementById('englishWord').textContent = 'No cards found in this category';
    document.getElementById('cardTracker').textContent = '0 of 0';
}

function flipCard() {
    document.getElementById('card').classList.toggle('flipped');
}

function nextCard() {
    if (currentCards.length === 0) return;
    document.getElementById('card').classList.remove('flipped');
    setTimeout(() => {
        currentIndex = (currentIndex + 1) % currentCards.length;
        displayCard();
    }, 150);
}

function prevCard() {
    if (currentCards.length === 0) return;
    document.getElementById('card').classList.remove('flipped');
    setTimeout(() => {
        currentIndex = (currentIndex - 1 + currentCards.length) % currentCards.length;
        displayCard();
    }, 150);
}

function shuffleCards() {
    if (currentCards.length === 0) return;
    document.getElementById('card').classList.remove('flipped');
    setTimeout(() => {
        currentIndex = Math.floor(Math.random() * currentCards.length);
        displayCard();
    }, 150);
}

function speakKorean(event) {
    event.stopPropagation();
    if ('speechSynthesis' in window && currentCards.length > 0) {
        const text = currentCards[currentIndex].korean;
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'ko-KR';
        utterance.rate = 0.8;
        window.speechSynthesis.speak(utterance);
    } else {
        alert('Text-to-speech is not supported in this browser.');
    }
}

document.getElementById('categoryFilter').addEventListener('change', (e) => {
    loadCards(e.target.value);
});

document.getElementById('addCardForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const korean = document.getElementById('inputKorean').value.trim();
    const english = document.getElementById('inputEnglish').value.trim();
    const category = document.getElementById('inputCategory').value;

    try {
        const response = await fetch('/api/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ korean, english, category })
        });

        if (response.ok) {
            const modalElement = document.getElementById('addModal');
            const modalInstance = bootstrap.Modal.getInstance(modalElement);
            modalInstance.hide();

            document.getElementById('addCardForm').reset();
            const currentSelectedCategory = document.getElementById('categoryFilter').value;
            loadCards(currentSelectedCategory);
        } else {
            alert('Failed to save flashcard.');
        }
    } catch (error) {
        console.error('Error adding card:', error);
    }
});

document.addEventListener('DOMContentLoaded', () => {
    loadCards();
});