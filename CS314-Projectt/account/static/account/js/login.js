var form = document.getElementById('login-form');
/* ----------------------------------------check password--------------------------------------------*/ 
form.addEventListener('submit', function(event) {
    var password = document.getElementById('password').value.trim();
    /* check password field is not empty or very large*/
    if (password.length < 1 || password.length > 255) {
      event.preventDefault();
      document.getElementById('password').classList.add('is-invalid');
      if (password.length < 1){
        document.getElementById('password-error').textContent = 'Please enter password';}
      else{
        document.getElementById('password-error').textContent = 'Password must be less than 255 characters';
      }
    } else {
      document.getElementById('password').classList.remove('is-invalid');
      document.getElementById('password-error').textContent = '';
    }
  });
/* ------------------------------------------------------------------------------------------------*/ 
/* -----------------------------------------check email--------------------------------------------*/ 
form.addEventListener('submit', function(event) {
    var email = document.getElementById('email').value.trim();
    /* check user email field is not empty or very large*/
    if (email.length < 1 || email.length > 255) {
      event.preventDefault();
      document.getElementById('email').classList.add('is-invalid');
      if (email.length < 1){
        document.getElementById('email-error').textContent = 'Please enter email';}
      else{
        document.getElementById('email-error').textContent = 'Email must be less than 255 characters';
      }
    } else {
      document.getElementById('email').classList.remove('is-invalid');
      document.getElementById('email-error').textContent = '';
    }
  });
/* ------------------------------------------------------------------------------------------------*/ 
