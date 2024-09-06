<template>
  <div class="container">
    <div class="content">
      <div class="text-content">
        <h1 class="pic-name">{{ info.Name }}</h1>
        <p class="description" v-html="highlightLinkText(info.Description)"></p>
      </div>
      <img :src="imagePath" :alt="info.Name" class="picture"/>
    </div>
  </div>
</template>


<script setup>
import { useRoute } from 'vue-router';
import { highlightLinkText } from '../utils/Markdown.vue';

const route = useRoute();

const info = {
  Name: route.params.Name,
  Description: route.params.Description.replace("&&&&", "'"), //Include ' in actual string
  Pic: route.params.Pic,
};

const imagePath = new URL(`../assets/${info.Pic}`, import.meta.url).href;

</script>


<style scoped>

.container {
  display: flex;
  justify-content: center; 
  width: 100%;
  height: 100vh;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 700px;
}

.text-content {
  text-align: left;
  width: 100%;
}

.description {
  margin-top: -12px;
  font-size: 18px;
}

.picture {
  border: 1.5px solid #000000;
  width: 700px; 
  max-height: 900px;
  overflow-y: auto;
  margin-top: -5px;
  margin-bottom: 60px;
}

@media (max-width: 715px) {
  .content {
    width: 480px;
  }

  .picture {
    width: 480px; 
  }
}

</style>
