<template>
    <component :is="isMobile ? MobileNavBar : NavBar" />
    <router-view />
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import NavBar from './components/NavBar.vue';
import MobileNavBar from './components/MobileNavBar.vue';

const isMobile = ref(window.innerWidth <= 700);

const updateWindowSize = () => {
  isMobile.value = window.innerWidth <= 700;
};

onMounted(() => {
  window.addEventListener('resize', updateWindowSize);
});

onUnmounted(() => {
  window.removeEventListener('resize', updateWindowSize);
});

</script>


<style>

body, html {
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
}

img {
  width: 100%; 
  height: auto;
  display: block;
}

</style>