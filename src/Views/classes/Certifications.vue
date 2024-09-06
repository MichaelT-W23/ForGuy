<template>
    <h1>{{ text.page }}</h1>
    <p class="description">{{ text.desc1 }}</p>
    <button @click="toggleAll" class="expand-all-btn">{{ allOpen ? 'Close All' : 'Expand All' }}</button>
    <div class="job-section">
        <h2>{{ text.header2 }}</h2>
        <p>{{ text.desc2 }}</p>
        <div class="job-menu">
            <div v-for="cloudCert in cloudCertifications" :key="cloudCert.Name" class="job-item">
                <AccordionMenu :item="cloudCert" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>{{ text.header3 }}</h2>
        <p>{{ text.desc3 }}</p>
        <div class="job-menu">
            <div v-for="skillCerts in skillCertifications" :key="skillCerts.Name" class="job-item">
                <AccordionMenu :item="skillCerts" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>{{ text.header4 }}</h2>
        <p>{{ text.desc4 }}</p>
        <div class="job-menu">
            <div v-for="mlCert in mlCertifications" :key="mlCert.Name" class="job-item">
                <AccordionMenu :item="mlCert" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>{{ text.header5 }}</h2>
        <p>{{ text.desc5 }}</p>
        <div class="job-menu">
            <div v-for="academicCert in academicCertifications" :key="academicCert.Name" class="job-item">
                <AccordionMenu :item="academicCert" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>{{ text.header6 }}</h2>
        <p>{{ text.desc6 }}</p>
        <div class="job-menu">
            <div v-for="tip in generalTips" :key="tip.Name" class="job-item">
                <AccordionMenu :item="tip" :isOpen="allOpen" />
            </div>
        </div>
    </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import AllData from "../../data/Classes/UsefulCertifications.json";
import AccordionMenu from "../../components/AccordionMenu.vue";

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];
const cloudCertifications = jsonData.value["Cloud Certifications"];
const skillCertifications = jsonData.value["Certifications for Essential Skills"];
const mlCertifications = jsonData.value["Machine Learning Certifications"];
const academicCertifications = jsonData.value["Academic Certifications and Degrees"];
const generalTips = jsonData.value["GeneralTips"];

const allOpen = ref(false);

const toggleAll = () => {
    allOpen.value = !allOpen.value;
};

onMounted(() => {
    document.body.style.backgroundColor = 'white';
    document.documentElement.style.backgroundColor = 'white';
});

onUnmounted(() => {
    document.body.style.backgroundColor = '';
    document.documentElement.style.backgroundColor = '';
});

</script>


<style scoped> 

.expand-all-btn {
    padding: 5px 40px;
    border-radius: 5px;
    background-color: #007AFF;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 16px;
    margin-left: 9.5%;
}

.expand-all-btn:hover {
    background-color: #0068DF;
}

h1, h2 {
    text-align: left;
    margin-left: 9.5%;
}

.description {
    margin-bottom: 20px;
}

p {
    text-align: left;
    margin-left: 9.5%;
    margin-top: -15px;
    font-size: 18px;
    width: 80%; 
}

.job-section {
    margin-bottom: 55px;
}

.job-menu {
    margin-top: -5px;
}

.job-item {
    margin-bottom: 12px;
}

</style>