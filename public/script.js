const fonts = {
    bold: {'a': '𝗮', 'b': '𝗯', 'c': '𝗰', ...},  // Match Python implementation
    italic: {'a': '𝘢', 'b': '𝘣', 'c': '𝘤', ...},
    // Add other styles
};

function transformText(text, style) {
    return text.split('').map(c => fonts[style][c] || c).join('');
}

function generateStyles() {
    const input = document.getElementById('inputText').value;
    const output = Object.entries(fonts).map(([style, _]) => 
        `${style.toUpperCase()}:\n${transformText(input, style)}`
    ).join('\n\n');
    document.getElementById('results').textContent = output;
}
