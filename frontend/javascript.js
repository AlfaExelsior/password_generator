function generatePassword() {
  const length = document.getElementById('length').value;
  const url = `http://127.0.0.1:5000/generate_password/${length}`; 

  fetch(url)
    .then(response => response.json())
    .then(data => {
      document.getElementById('password').textContent = `{${data.password}}`; 
    });
}