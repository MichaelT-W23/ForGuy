<template>
  <div class="contact-form">
    <h1>{{ text[0].title }}</h1>
    <p class="intro-text">{{ text[0].desc }}</p>

    <div class="form-group">
      <label for="name" class="form-label">{{ text[1].Header }}<span style="color: #EF0000;">*</span></label>
      <input autocomplete="off" type="text" id="name" name="name" v-model="userName" :placeholder="text[1].Placeholder"/>
    </div>

    <div class="form-group">
      <label for="email" class="form-label">{{ text[2].Header }}<span style="color: #EF0000;">*</span></label>
      <input type="email" id="email" name="email" v-model="userEmail" :placeholder="text[2].Placeholder" />
    </div>

    <div class="form-group">
      <label for="message" class="form-label">{{ text[3].Header }}<span style="color: #EF0000;">*</span></label>
      <textarea id="message" name="message" v-model="userMessage" class="square-text-area" :placeholder="text[3].Placeholder"></textarea>
    </div>

    <button 
      type="submit" 
      class="send-email-btn" 
      @click="submitForm" 
      :disabled="!isFormValid"
      :class="{'valid': isFormValid && !isButtonClicked, 
               'clicked': isButtonClicked, 
               'default': !isFormValid && !isButtonClicked
              }"
     >
        {{ buttonText }}
     </button>

     <div style="margin-bottom: 80px;"></div>
  </div>
</template>


<script setup>
import { ref, computed } from 'vue';
import AllData from '../data/Contact.json';
import emailjs from '@emailjs/browser';
import Swal from 'sweetalert2';

const jsonData = ref(AllData);
const text = jsonData.value["Contact"];

const userName = ref('');
const userEmail = ref('');
const userMessage = ref('');
const isButtonClicked = ref(false);
const buttonText = ref(text[4].submit); 

emailjs.init('bCe2UFI1L7SfXITtA');

const isFormValid = computed(() => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return userName.value.trim() !== '' &&
         userEmail.value.match(emailRegex) &&
         userMessage.value.trim() !== '';
});

const submitForm = () => {
  if (!isFormValid.value) return;

  isButtonClicked.value = true;
  buttonText.value = text[4].sending; //sending ...

  const templateParams = {
    subject: "New message from CS Website",
    website: "CS Website",
    from_name: userName.value,
    from_email: `Email: ${userEmail.value}`,
    message: userMessage.value
  };

  const serviceID = 'service_feq974e';
  const templateID = 'template_cowiwh7';

  emailjs.send(serviceID, templateID, templateParams)
    .then((response) => {
      Swal.fire(text[5].successMsg, text[5].successDesc, 'success');
      userName.value = '';
      userEmail.value = '';
      userMessage.value = '';
      return response;
    })
    .catch((err) => {
      Swal.fire(text[6].errorMsg, text[6].errorDesc, 'error');
      console.error('Failed to send email:', err);
      throw err;
    })
    .finally(() => {
      isButtonClicked.value = false;
      buttonText.value = 'Submit';
    })
};

</script>


<style scoped>

.contact-form {
  display: flex;
  flex-direction: column;
  max-width: 600px;
  width: 90%;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 1rem;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 9px; 
}
  
input[type="text"],
input[type="email"],
.square-text-area {
  width: 100%;
  border: 1.75px solid #ccc;
  padding: 12px;
  margin-top: 8px;
  box-sizing: border-box;
  font-family: Arial, sans-serif;
}

input[type="text"]::placeholder,
input[type="email"]::placeholder,
.square-text-area::placeholder {
  font: arial;
  font-size: 14.25px;
  color: #999;
}
  
.square-text-area {
  height: 200px;
  resize: none;
}
  
.send-email-btn {
  width: 100%;
  color: white;
  cursor: pointer;
  border: none;
  padding: 10px;
  margin-top: 5px;
  font-size: 16.5px;
}
  
/* Disabled button */
.send-email-btn.default {
  background-color: gray;
}
  
/* Valid form */
.send-email-btn.valid {
  background-color: blue; 
}
  
/* Valid form and hovered over */
.send-email-btn.valid:hover {
  background-color: darkblue;
}
  
/* Sending... */
.send-email-btn.clicked {
  background-color: #00A643;
}

h1 {
  align-self: flex-start;
  margin-top: 5px;
}

.intro-text {
  margin-top: -15px;
  margin-bottom: 16px;
  font-size: 19px;
}

.form-label {
  font-size: 17px;
}

#name, #email, #message {
  font-size: 15.25px;
}

</style>
  
  
