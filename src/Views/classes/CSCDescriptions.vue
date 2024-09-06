<template>
    <main class="csc-descriptions-page">
        <div class="top-section">
            <h1>{{ text.page }}</h1>
            <span class="expand-text" @click="toggleExplanation">{{ text.desc }}</span>
            <p class="courses-found" v-if="explainOpen">{{ text.pageDescription }}</p>
            <div class="search-expand-wrapper">
                <input type="text" v-model="searchQuery" :placeholder="text.searchText" class="search-bar" />
                <button @click="toggleAll" class="expand-all-btn">{{ allOpen ? 'Close All' : 'Expand All' }}</button>
            </div>
            <p class="courses-found" v-if="searchQuery.length != 0">Found {{ filteredCourses.length }} course{{ filteredCourses.length == 1 ? '' : 's' }} that contain the term "<span style="color: darkblue">{{ searchQuery }}</span>" in their name or description.</p>
            <p style="margin-bottom: 20px;" v-else></p>
        </div>
        <div v-for="course in filteredCourses" :key="course.Name">
            <AccordionMenu :item="course" :isOpen="allOpen"/>
        </div>
        <p style="margin-bottom: 50px;"></p>
    </main>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import AllData from "../../data/Classes/CSCDescriptions.json";
import AccordionMenu from "../../components/AccordionMenu.vue";

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];
const searchQuery = ref('');
const allOpen = ref(false);
const explainOpen = ref(false);

const filteredCourses = computed(() => {
    if (!searchQuery.value) {
        return jsonData.value["Courses"];
    }

    return jsonData.value["Courses"].filter(course =>
        course.Description.toLowerCase().includes(searchQuery.value.toLowerCase().trim()) ||
        course.Name.toLowerCase().includes(searchQuery.value.toLowerCase().trim()) ||
        course.Number.toLowerCase().includes(searchQuery.value.toLowerCase().trim()) 
    );
});

const toggleAll = () => {
    allOpen.value = !allOpen.value;
};

const toggleExplanation = () => {
    explainOpen.value = !explainOpen.value;
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

html {
  background-color: white;
}

.csc-descriptions-page .top-section h1 {
    text-align: left;
    margin-left: 10%;
    margin-bottom: 4px;
    background-color: white;
}

.expand-text {
    color: #007AFF;
    margin-top: 5px;
    text-align: left; 
    margin-left: 10.18%; 
    font-size: 18.5px;
}

.expand-text:hover {
    color: #0000D7;
}

.courses-found {
    margin-top: 5px;
    text-align: left; 
    margin-left: 10.18%;
    margin-right: 10.18%;
    margin-bottom: 2px;
    font-size: 20px;
}

.search-expand-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    width: 80%;
    margin: 0 auto; 
}

.search-bar {
    flex-grow: 1;
    padding: 10px 20px;
    border-radius: 20px;
    border: 1px solid #333; 
    color: #333; 
    background-color: #fff; 
    margin-right: 10px; 
    margin-top: 12px;
}

.expand-all-btn {
    padding: 10px 20px;
    border-radius: 20px;
    background-color: #007AFF;
    color: white;
    border: none;
    cursor: pointer;
    margin-top: 12px;
}

.expand-all-btn:hover {
    background-color: #0068DF;
}

</style>

