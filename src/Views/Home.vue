<template>
    <img src="../assets/uncw.jpg" alt="UNCW pic" />
    <div class="info-container">
        <div v-for="section in homeSections" :key="section.header">
            <div class="section-container">
                <h1>{{ section.Header }}</h1>
                <p v-html="formatParagraph(section.Body)"></p>
            </div>
        </div>
    </div>
    <p style="margin-bottom: 100px"></p>     
</template>


<script setup>
import { ref } from 'vue';
import { createHyperLink, createRouterLink, createDownloadLink } from '../utils/Markdown.vue';
import AllData from '../data/Home.json';

const jsonData = ref(AllData);
const homeSections = jsonData.value["Home"];

//Allows for formatted hyperlinks and router links
const formatParagraph = (body) => {
    return createDownloadLink(createHyperLink(createRouterLink(body)));
}

</script>


<style scoped>

h1 {
    margin-left: 150px;
}

p {
    margin-left: 151px;
    font-size: 20px;
    margin-top: -14px;
    width: 80%;
}

.section-container {
    margin-bottom: 40px;
}

@media (max-width: 1000px) {

    h1 {
        margin-left: 60px;
    }

    p {
        margin-left: 61px;
        width: 85%;
    }
}


@media (max-width: 700px) {

    h1 {
        margin-left: 25px;
    }
    
    p {
        margin-left: 26px;
        width: 90%;
    }
}

</style>
