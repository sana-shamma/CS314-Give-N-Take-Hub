var form = document.getElementById('contactForm');
/*------------------------------------- check item name----------------------------------------------*/ 
form.addEventListener('submit', function(event) {
  var ItemName = document.getElementById('ItemName').value.trim(); 
  /* check ItemName name field is not empty or very large*/
  if (ItemName.length < 1 || ItemName.length > 100) {
    event.preventDefault();
    document.getElementById('ItemName').classList.add('is-invalid');
    if (ItemName.length < 1){
      document.getElementById('ItemName').nextElementSibling.textContent = 'Please enter item name';}
    else{
      document.getElementById('ItemName').nextElementSibling.textContent = 'Item name must be less than 100 characters';
    }
  } else {
    document.getElementById('ItemName').classList.remove('is-invalid');
    document.getElementById('ItemName').nextElementSibling.textContent = '';
  }
});
/*--------------------------------------------------------------------------------------------------*/ 
/*------------------------------------- check owner name----------------------------------------------*/ 
form.addEventListener('submit', function(event) {
    var owner = document.getElementById('owner').value.trim();
    /* check owner field is not empty or very large*/ 
    if (owner.length < 1 || owner.length > 255) {
      event.preventDefault();
      document.getElementById('owner').classList.add('is-invalid');
      if (owner.length < 1){
        document.getElementById('ownername-error').textContent = 'Please enter owner';
      } else {
        document.getElementById('ownername-error').textContent = 'Owner name must be less than 255 characters';
      }
    } 
    /* check if owner name contains only letters */
    else if (!/^[a-zA-Z\s]+$/.test(owner)) {
      event.preventDefault();
      document.getElementById('owner').classList.add('is-invalid');
      document.getElementById('ownername-error').textContent = 'Owner name can only contain letters';
    } else {
      document.getElementById('owner').classList.remove('is-invalid');
      document.getElementById('ownername-error').textContent = '';
    }
  });
/*---------------------------------------------------------------------------------------------------*/ 
/*------------------------------------- check phone number--------------------------------------------*/ 
form.addEventListener('submit', function(event) {
    var phone = document.getElementById('phoneNumber').value.trim();
    /* check phone number length */
    var phoneRegex = /^\d{10}$/; // matches 10 digits
    if (!phoneRegex.test(phone)) {
      event.preventDefault();
      document.getElementById('phone-error').textContent = 'Please enter a valid 10-digit phone number';
    } else {
      document.getElementById('phone-error').textContent = '';
    }
  });
/*-----------------------------------------------------------------------------------------------------*/ 
/*------------------------------------- check Selecting sharing type-----------------------------------*/ 
  form.addEventListener('submit', function(event) {
    var selectedValue = this.value;
    if (selectedValue === '') {
      event.preventDefault();
      thdocument.getElementById('sharingType').classList.add('is-invalid');
      document.getElementById('requesttype-error').textContent = 'Please choose a request type';
    } else {
      document.getElementById('sharingType').classList.remove('is-invalid');
      document.getElementById('requesttype-error').textContent = '';
    }
  });
/*----------------------------------------------------------------------------------------------------*/ 
/*------------------------------------- check all required fields----------------------------------------------*/ 
  function validateForm() {
    var isFormValid = true;
    // Get all required input fields
    var inputElements = document.querySelectorAll('input[required], select[required], textarea[required]');
    // Loop through each input field and check if it has a value
    for (var i = 0; i < inputElements.length; i++) {
      if (!inputElements[i].value.trim()) {
        inputElements[i].classList.add('is-invalid');
        isFormValid = false;
      } else {
        inputElements[i].classList.remove('is-invalid');
      }
    }
    // Show error message if form is not valid
    var requiredFieldsError = document.getElementById('requiredfields-error');
    if (!isFormValid) {
      requiredFieldsError.textContent = 'Please fill in all required fields';
    } else {
      requiredFieldsError.textContent = '';
    }
    // Return whether the form is valid or not
    return isFormValid;
  }
/*----------------------------------------------------------------------------------------------------*/ 