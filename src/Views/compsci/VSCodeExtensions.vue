<template>
    <h1>{{ text.page }}</h1>
    <p class="description">{{ text.desc }}</p>
    <button @click="toggleAll" class="expand-all-btn">{{ allOpen ? 'Close All' : 'Expand All' }}</button>
    <div class="extension-section">
        <h2>{{ text.header2 }}</h2>
        <p>{{ text.desc2 }}<a :href="emailStr" class="email-btn">{{ text.email }}</a></p>
        <div class="extension-menu">
            <div v-for="extension in extensions" :key="extension.Name" class="extension-item">
                <AccordionMenu :item="extension" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <p style="margin-bottom: 100px;"></p>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import AllData from "../../data/CompSci/VSCodeExtensions.json";
import AccordionMenu from "../../components/AccordionMenu.vue";
import { bodyContent } from "../../components/ExtensionEmail.vue";

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];
const extensions = jsonData.value["Extensions"];
const allOpen = ref(false);


const emailTo = ""; //TODO
const subject = "VSCode Extension Download Links";
const emailStr = `mailto:${emailTo}?subject=${subject}&body=${bodyContent}`;


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

.extension-section {
    margin-bottom: 55px;
}

.extension-menu {
    margin-top: -5px;
}

.extension-item {
    margin-bottom: 12px;
}

.email-btn {
    color: #007AFF;
    cursor: pointer;
    text-decoration: none;
}

.email-btn:hover {
    color: #0000D7;
    text-decoration: underline;
}

</style>