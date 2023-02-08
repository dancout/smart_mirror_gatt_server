// Adapted from https://www.geeksforgeeks.org/how-to-load-the-contents-of-a-text-file-into-a-javascript-variable/
let deviceName = document.getElementById('DeviceName')

let files = input.files;

if (files.length == 0) return;

const file = files[0];

let reader = new FileReader();

reader.onload = (e) => {
    const file = e.target.result;

    // This is a regular expression to identify carriage
    // Returns and line breaks
    const lines = file.split(/\r\n|\n/);
    // We need the second line of constants.py and after the equals sign
    deviceName.innerHTML = lines[1].split(' = ')[1];

};

reader.onerror = (e) => alert(e.target.error.name);

reader.readAsText(file);
