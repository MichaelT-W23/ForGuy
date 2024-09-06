<template>
    <div class="loading-container">
        <div class="spinner"></div>
        <span class="txt">Loading<span class="dots">{{ dots }}</span></span>
    </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const dots = ref('');

const addDots = () => {
    const dotsCount = dots.value.length;
    
    if (dotsCount < 3) {
        dots.value += '.';
    } else {
        dots.value = '';
    }
}

onMounted(() => {
  const interval = setInterval(addDots, 500);

  onUnmounted(() => {
    clearInterval(interval);
  });
});

</script>




<style scoped>
.spinner {
    border: 5px solid rgba(128, 128, 128, 0.3);
    border-top: 5px solid #777;
    border-radius: 50%;
    width: 85px;
    height: 85px;
    animation: spin 1s linear infinite;
    margin: 0 auto;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}

.loading-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 120px;
}

.txt {
    font-size: 21px;
    position: relative;
    top: 10px;
    margin-right: 14px;
}

.dots {
    display: inline-block;
    position: absolute;
    left: 100%;
    white-space: nowrap;
}

</style>

