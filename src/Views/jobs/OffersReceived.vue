<template>
    <h1>{{ text.page }}</h1>
    <p class="description">{{ text.desc1 }}</p>
    <button @click="toggleAll" class="expand-all-btn">{{ allOpen ? 'Close All' : 'Expand All' }}</button>
    <div class="job-section">
        <h2>{{ text.header2 }}</h2>
        <p>{{ text.desc2 }}</p>
        <div class="job-menu">
            <div v-for="internship in internships" :key="internship.Name" class="job-item">
                <AccordionMenu :item="internship" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>{{ text.header3 }}</h2>
        <p>{{ text.desc3 }}</p>
        <div class="job-menu">
            <div v-for="job in fullTimeJobs" :key="job.Name" class="job-item">
                <AccordionMenu :item="job" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>{{ text.header4 }}</h2>
        <p>{{ text.desc4 }}</p>
        <div class="job-menu">
            <div v-for="interview in interviews" :key="interview.Name" class="job-item">
                <AccordionMenu :item="interview" :isOpen="allOpen" />
            </div>
        </div>
    </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import AllData from "../../data/jobs/OffersReceived.json";
import AccordionMenu from "../../components/AccordionMenu.vue";

const jsonData = ref(AllData);
const text = jsonData.value["text"][0];
const internships = jsonData.value["internships"];
const fullTimeJobs = jsonData.value["fullTime"];
const interviews = jsonData.value["interviews"];
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