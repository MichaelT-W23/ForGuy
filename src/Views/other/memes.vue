<template>
    <div class="meme-page">
      <h1>{{ text.page }}</h1>
      <p>{{ text.desc }}</p>
  
      <div
        class="meme-container"
        v-for="(meme, index) in memeObjects"
        :key="index"
      >
        <div class="meme-text">
          {{ index + 1 }}. <span v-html="createHyperLink(meme.text)"></span>
        </div>
        <div v-if="meme.image || meme.video" class="image-container">
          <img
            v-if="meme.image"
            :src="meme.image"
            alt="Meme Picture"
            @click="openGalleryView(index)"
          />

          <div class="horizontal-video-container">
            <video
                v-if="meme.video"
                class="centered-video"
                controls
                @click="openGalleryView(index)"
            >
            <source :src="meme.video" type="video/mp4" />
                Your browser does not support the video tag.
            </video>
           </div>

          <span class="hidden-text">{{ meme.transcription }}</span>
        </div>
      </div>
  
      <transition name="fade">
        <GalleryView
          v-if="isGalleryViewOpen"
          :items="memeObjects"
          :initialIndex="currentMemeIndex"
          :isOpen="isGalleryViewOpen"
          @close="isGalleryViewOpen = false"
        />
      </transition>

    </div>
</template>
  

<script setup>
import { ref } from 'vue';
import { memeObjects } from '../../components/Memes.vue';
import AllData from '../../data/Other/Memes.json';
import { createHyperLink } from '../../utils/Markdown.vue';
import GalleryView from '../GalleryView.vue';
  
const jsonData = ref(AllData);
const text = jsonData.value['Text'][0];
  
const isGalleryViewOpen = ref(false);
const currentMemeIndex = ref(0);

const openGalleryView = (index) => {
    currentMemeIndex.value = index;
    isGalleryViewOpen.value = true;
};

</script>


<style scoped>
.meme-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.meme-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 400px;
  margin-bottom: 35px;
}

.meme-text {
  font-size: 18px;
}

.image-container {
  position: relative;
  width: 400px;
}

.image-container:hover {
  cursor: pointer;
}

.hidden-text {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 200px;
  left: 0;
  z-index: -1; /* Set to 1 if you want text to highlight when searched */
  pointer-events: none;
  color: transparent;
  background: transparent;
  border: none;
}

img {
  width: 100%;
  border: 2px solid black;
  margin-top: 8px;
  display: block;
}

p {
  margin-top: -15px;
  font-size: 20px;
}

.horizontal-video-container {
  position: relative;
  width: 400px;
  width: 100%;
  border: 2px solid black;
  margin-top: 8px;
  display: block;
}

.centered-video {
  display: block;
  max-width: 100%;
  height: auto;
}

.hidden-video-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: -1; /* Set to 1 if you want text to highlight when searched */
  color: transparent;
  background: transparent;
}

</style>
