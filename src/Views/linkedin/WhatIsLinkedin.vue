<template>
    <div class="image-container">
        <img src="../../assets/linkedIn.png" alt="LinkedIn Pic" />
        <div class="overlay"></div>
    </div>
    <div class="info-container">
        <h1>{{ info.Header }}</h1>
        <p v-html="info.Body"></p>
    </div>
    <p></p>
</template>


<script setup>
import { ref } from 'vue';
import AllData from "../../data/LinkedIn/WhatIsLinkedIn.json";

const jsonData = ref(AllData);
const info = jsonData.value["Info"][0];

</script>


<style scoped>

.image-container {
    position: relative;
    width: 100%;
    height: 400px;
}

.info-container {
    margin-top: -5px;
}

img {
    width: 100%; 
    height: 100%;
    display: block;
}

.overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(8, 0, 255, 0.059);
}

h1 {
    margin-left: 100px;
}

p {
    margin-left: 101px;
    font-size: 20px;
    margin-top: -14px;
    width: 80%;
}

@media (max-width: 700px) {

    img, .overlay {
        height: 70%
    }

    .info-container {
        margin-top: -120px;
    }


    h1 {
        margin-left: 25px;
    }
    
    p {
        margin-left: 26px;
        width: 90%;
    }
}

</style>
