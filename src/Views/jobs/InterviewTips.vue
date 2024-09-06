<template>
    <div class="container">
        <h1 class="tip-header">{{ text.page }}</h1>
        <p class="description">{{ text.desc }}</p>
        <div class="tips-container">
            <div v-for="tip in tips" :key="tip.id" class="tip-section">
                <p class="tip-text" :data-index="tip.id"><span class="invisible-index">{{ tip.id }}</span></p>
                <p class="text-section" v-html="createRouterLink(tip.tip)"></p>
            </div>
        </div>
        <p style="margin-bottom: 60px;"></p>
    </div>
</template>


<script setup>
import { ref } from 'vue';
import AllData from "../../data/jobs/InterviewTips.json";
import { createRouterLink } from "../../utils/Markdown.vue";

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];
const tips = jsonData.value["Tips"];

</script>


<style scoped>

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.tip-header {
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

.tips-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.tip-section {
    margin-bottom: 5px;
    width: 575px;
}

.tip-text {
    position: relative;
    width: auto;
    font-size: 21px;
    font-weight: 500;
}

.tip-text::before {
    content: attr(data-index);
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: darkblue;
    color: white;
    border-radius: 50%;
    width: 25px;
    height: 25px;
    margin-left: -35px;
    position: absolute;
    top: 0;
    transform: translateY(-50%);
    font-size: 14px;
}

.text-section {
    font-size: 19.5px;
    word-wrap: break-word; 
    overflow-wrap: break-word; 
    margin-top: -13px;
}

.invisible-index {
  z-index: -1;
  position: absolute;
  font-size: 0;
}

@media (max-width: 700px) {
    .tip-header {
        width: 490px;
    }
    
    .description {
        width: 490px;
    }

    .tip-section {
        width: 375px;
    }
}

</style>
