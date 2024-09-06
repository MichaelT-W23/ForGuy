<template>
    <main class="where-to-apply-page">
        <div class="top-section">
            <h1>{{ text.page }}</h1>
            <span class="expand-text" @click="toggleExplanation">{{ text.toggleQuestion }}</span>
            <p class="companies-found" v-if="explainOpen">{{ text.toggleDescription }}</p>
            <div class="search-expand-wrapper">
                <input type="text" v-model="searchQuery" :placeholder="text.searchText" class="search-bar" />
                <button @click="toggleAll" class="expand-all-btn">{{ allOpen ? 'Close All' : 'Expand All' }}</button>
            </div>
            <p class="companies-found" v-if="searchQuery.length != 0">Found {{ filteredCompanies.length }} companies in "{{ searchQuery }}"</p>
            <p style="margin-bottom: 20px;" v-else></p>
        </div>
        <div v-for="company in filteredCompanies" :key="company.Name">
            <AccordionMenu :item="company" :isOpen="allOpen"/>
        </div>
        <p style="margin-bottom: 60px;"></p>
    </main>
</template>


<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import AllData from "../../data/jobs/WhereToApply.json";
import AccordionMenu from "../../components/AccordionMenu.vue";

const jsonData = ref(AllData);
const text = jsonData.value["text"][0];
const searchQuery = ref('');
const allOpen = ref(false);
const explainOpen = ref(false);

const filteredCompanies = computed(() => {
    if (!searchQuery.value) {
        return jsonData.value["Companies"];
    }

    return jsonData.value["Companies"].filter(company =>
        company.Location.toLowerCase().includes(searchQuery.value.toLowerCase().trim())
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

//When view changes set back to default background color
onUnmounted(() => {
    document.body.style.backgroundColor = '';
    document.documentElement.style.backgroundColor = '';
});

</script>


<style scoped>

html {
  background-color: white;
}

.where-to-apply-page .top-section h1 {
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
    cursor: pointer;
}

.companies-found {
    margin-top: 5px;
    text-align: left; 
    margin-left: 10.18%;
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

