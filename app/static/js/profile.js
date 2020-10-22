function checkForm() {
  if (textarea.value.length) {
    file.disabled = true;
  } else if (file.value) {
    console.log(file.value);
    textarea.disabled = true;
  } else {
    file.disabled = false;
    textarea.disabled = false;
  }
}