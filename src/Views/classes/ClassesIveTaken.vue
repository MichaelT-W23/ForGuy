<template>
    <main class="classes-ive-taken-page">
        <div class="top-section">
            <h1>{{ text.page }}</h1>
            <span class="expand-text" @click="toggleExplanation">{{ text.desc }}</span>
            <p class="description" v-if="explainOpen">{{ text.pageDescription }}</p>
            <div class="search-expand-wrapper">
                <input type="text" v-model="searchQuery" :placeholder="text.searchText" class="search-bar" />
                <button @click="toggleAll" class="expand-all-btn">{{ allOpen ? 'Close All' : 'Expand All' }}</button>
            </div>
        </div>
        <p style="margin-top: 20px;"></p>
        <p class="courses-found" v-if="searchQuery.length != 0">Found {{ totalMatchingCourses }} course{{ totalMatchingCourses === 1 ? '' : 's' }} that contain the term "<span style="color: darkblue">{{ searchQuery }}</span>" in their name or description.</p>
        <section v-for="(courses, semester) in semesterCourses" :key="semester" class="section">
            <h2 class="semester-header" v-if="courses.length > 0">{{ semester }}</h2>
            <div v-for="course in courses" :key="course.Name">
                <AccordionMenu :item="course" :isOpen="allOpen"/>
            </div>
        </section>
        <p class="graduation">{{ text.grad }}</p>
        <p style="margin-bottom: 100px;"></p>
    </main>
</template>


<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import AllData from "../../data/Classes/ClassesIveTaken.json";
import AccordionMenu from "../../components/AccordionMenu.vue";

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];
const searchQuery = ref('');
const allOpen = ref(false);
const explainOpen = ref(false);

const filterCourses = (courses) => {
    if (!searchQuery.value) return courses;
    return courses.filter(course => 
        course.Name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        course.Number.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        course.Description.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
};

const totalMatchingCourses = computed(() => {
    let count = 0;

    ['Freshman', 'Sophomore', 'Junior', 'Senior'].forEach(year => {
        ['First', 'Second'].forEach(semester => {
            const semesterKey = semester === 'First' ? 'First' : 'Second';
            const courses = jsonData.value[year]?.[semesterKey] || [];
            count += filterCourses(courses).length;
        });
    });

    return count;
});

const semesterCourses = computed(() => ({
    'Freshman - First Semester (Fall 2020)': filterCourses(jsonData.value["Freshman"]["First"]),
    'Freshman - Second Semester (Spring 2021)': filterCourses(jsonData.value["Freshman"]["Second"]),
    'Sophomore - First Semester (Fall 2021)': filterCourses(jsonData.value["Sophomore"]["First"]),
    'Sophomore - Second Semester (Spring 2022)': filterCourses(jsonData.value["Sophomore"]["Second"]),
    'Junior - First Semester (Fall 2022)': filterCourses(jsonData.value["Junior"]["First"]),
    'Junior - Second Semester (Spring 2023)': filterCourses(jsonData.value["Junior"]["Second"]),
    'Senior - First Semester (Fall 2023)': filterCourses(jsonData.value["Senior"]["First"]),
}));

const toggleAll = () => { allOpen.value = !allOpen.value; };
const toggleExplanation = () => { explainOpen.value = !explainOpen.value; };

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

.classes-ive-taken-page .top-section h1 {
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

.description {
    text-align: left; 
    margin-left: 10.3%;
    margin-right: 10.3%;
    font-size: 20px;
    margin-top: 6px;
    margin-bottom: -2px;
}

.courses-found {
    /* margin-top: 10px; */
    text-align: left; 
    margin-left: 11%;
    font-size: 20px;
    margin-top: -10px;
    margin-bottom: -10px;
}

.semester-header {
    text-align: left;
    margin-left: 10%; 
    margin-bottom: 5px;
    font-size: 25px;
}

.section {
    margin-bottom: 45px;
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

.graduation {
    text-align: center; 
    font-size: 25px; 
    margin-top: 55px;
    color: #007627;
}

</style>

