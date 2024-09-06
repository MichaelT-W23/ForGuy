<template>
    <h1 class="job-header">{{ text.page }}</h1>
    <p class="job-description">{{ text.desc }}</p>
    <div v-for="tip in tips" :key="tip.Name" class="tip-section">
        <p class="tip-text">{{ tip.Tip }}: {{ tip.Name }}</p>
        <AccordionMenu :item="tip" :isOpen="allOpen"/>
        <p style="margin-bottom: 35px;"></p>
    </div>
    <p style="margin-bottom: 60px;"></p>
</template>


<script setup>
import { ref } from 'vue';
import AccordionMenu from "../../components/AccordionMenu.vue";

import AllData from "../../data/LinkedIn/LinkedInTips.json";
const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];
const tips = jsonData.value["LinkedInTips"];
const allOpen = ref(false);

</script>


<style scoped>

.job-header {
    margin-left: auto;
    margin-right: auto;
    border-bottom: 1.5px solid #d8dee4;
    width: 80%;
}

.job-description {
    margin-left: auto;
    margin-right: auto;
    width: 79.5%;
    font-size: 20px;
    margin-top: -14px;
    margin-bottom: 25px;
}

.tip-section {
    margin-bottom: 20px;
}

.tip-text {
    margin-left: auto;
    margin-right: auto;
    width: 80%;
    margin-bottom: 10px;
    font-size: 20px;
    font-weight: 600;
    color: #000062;
}

</style>