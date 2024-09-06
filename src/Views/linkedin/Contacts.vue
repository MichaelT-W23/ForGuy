<template>
    <div class="container">
        <div v-if="showEmailCopied" class="email-copied-message">Email Copied!</div>
        <h1 class="contact-header">{{ text.page }}</h1>
        <p class="description" v-html="createDownloadLink(text.desc)"></p>
        <div class="contacts-container">
            <div v-for="contact in contacts" :key="contact.Company" class="contact-section">
                <ContactCard :contact="contact" @emailCopied="emailCopied"></ContactCard>
            </div>
        </div>
        <p style="margin-bottom: 60px;"></p>
    </div>
</template>


<script setup>
import { ref } from 'vue';
import AllData from "../../data/LinkedIn/Contacts.json";
import ContactCard from "../../components/ContactCard.vue";
import { createDownloadLink } from "../../utils/Markdown.vue"


const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];
const contacts = jsonData.value["Contacts"];

const showEmailCopied = ref(false);

const emailCopied = () => {
  showEmailCopied.value = true;
  setTimeout(() => {
    showEmailCopied.value = false;
  }, 2000);
};

</script>


<style scoped>

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.contact-header {
    text-align: left;
    border-bottom: 1.5px solid #d8dee4;
    padding-bottom: 7px;
    width: 690px;
}

.description {
    margin-top: -8px;
    font-size: 19px;
    width: 690px;
}

.contacts-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.contact-section {
    margin-top: -19px;
}

/* Remove line 3, modify line 8, delete 25-33, and this class
if you want to remove email copy functionality */
.email-copied-message {
    position: fixed;
    left: 50%;
    transform: translateX(-50%);
    bottom: 20px;
    background-color: #333;
    color: #fff;
    padding: 10px;
    border-radius: 8px;
    text-align: center;
    z-index: 9999;
    width: 150px;
    max-width: 80%; 
}

@media (max-width: 700px) {
    .contact-header {
        width: 490px;
    }
    
    .description {
        width: 490px;
    }

    .contact-section {
        width: 400px;
        margin-right: 70px;
    }
}

</style>
