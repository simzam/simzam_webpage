function rotateOnClick() {
    const button = document.querySelector('.v-button');
    // const svg = button.querySelector('svg');

    // Toggle a class to rotate the button by 180 degrees
    button.classList.toggle('rotate180');
}
// Function to generate a random color in hexadecimal format
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// Function to change the background color of the root element to a random color with a smooth transition
function changeBackgroundColor() {
    const rootElement = document.documentElement;
    const newColor = getRandomColor();
    const currentColor = getComputedStyle(rootElement).getPropertyValue('--background-color') || '#ffffff';

    // Set the new color as a CSS variable for smooth transition
    rootElement.style.setProperty('--background-color', newColor);

    // Wait for a moment to allow the CSS variable to be applied
    setTimeout(() => {
        rootElement.style.backgroundColor = newColor;
    }, 0);
}

// Function to change the background color at random intervals
function changeColorAtRandomInterval() {
    changeBackgroundColor();

    // Generate a random interval between 1 and 3 seconds (1000-3000 milliseconds)
    const randomInterval = Math.floor(Math.random() * 2000) + 1000;

    // Schedule the next color change
    setTimeout(changeColorAtRandomInterval, randomInterval);
}

// Start the color-changing loop
changeColorAtRandomInterval();
