<template>
    <div class="uncw-pics-page">
      <h1>{{ text.page }}</h1>
      <p>{{ text.desc }}</p>
  
      <div
        class="uncw-pics-container"
        v-for="(pic, index) in uncwPics"
        :key="index"
      >
        <div class="uncw-pic-text">{{ index + 1 }}. {{ pic.text }}</div>
        <div v-if="pic.video" class="vertical-video-container">
          <video
            controls
            @click="openGalleryView(uncwPics, index)"
          >
            <source :src="pic.video" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
        <img
          v-else
          :src="pic.image"
          alt="Uncw Picture"
          @click="openGalleryView(uncwPics, index)"
        />
      </div>
  
      <h1>{{ text.header2 }}</h1>
      <p>{{ text.desc2 }}</p>
  
      <div
        class="uncw-pics-container"
        v-for="(pic, index) in NorthCarolinaPics"
        :key="index"
      >
        <div class="uncw-pic-text">{{ index + 1 }}. {{ pic.text }}</div>
        <div v-if="pic.video">
          <video
            class="horizontal-video-container"
            controls
            @click="openGalleryView(NorthCarolinaPics, index)"
          >
            <source :src="pic.video" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
        <img
          v-else
          :src="pic.image"
          alt="Uncw Picture"
          @click="openGalleryView(NorthCarolinaPics, index)"
        />
      </div>
  
      <h1>{{ text.header3 }}</h1>
      <p>{{ text.desc3 }}</p>
  
      <div
        class="uncw-pics-container"
        v-for="(pic, index) in TexasPics"
        :key="index"
      >
        <div class="uncw-pic-text">{{ index + 1 }}. {{ pic.text }}</div>
        <div v-if="pic.video">
          <video
            class="horizontal-video-container"
            controls
            @click="openGalleryView(TexasPics, index)"
          >
            <source :src="pic.video" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
        <img
          v-else
          :src="pic.image"
          alt="Uncw Picture"
          @click="openGalleryView(TexasPics, index)"
        />
      </div>
  
      <transition name="fade">
        <GalleryView
          v-if="isGalleryViewOpen"
          :items="galleryItems"
          :initialIndex="currentItemIndex"
          :isOpen="isGalleryViewOpen"
          @close="isGalleryViewOpen = false"
        />
      </transition>

    </div>
</template>
  

<script setup>
import { ref } from 'vue';
import { uncwPics, NorthCarolinaPics, TexasPics } from "../../components/UncwPics.vue";
import AllData from "../../data/Other/UncwPics.json";
import GalleryView from "../GalleryView.vue";

const jsonData = ref(AllData);
const text = jsonData.value['Text'][0];

const isGalleryViewOpen = ref(false);
const currentItemIndex = ref(0);
const galleryItems = ref([]);

const openGalleryView = (items, index) => {
  galleryItems.value = items;
  currentItemIndex.value = index;
  isGalleryViewOpen.value = true;
};

</script>


<style scoped>
.uncw-pics-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.uncw-pics-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 400px;
  margin-bottom: 35px;
}

.uncw-pics-container:hover {
  cursor: pointer;
}

.horizontal-video-container {
  width: 600px;
  border: 2px solid black;
  margin-top: 8px;
}

.vertical-video-container {
  width: 400px;
  height: 575px;
  margin-top: 8px;
  overflow: hidden;
  position: relative;
  border: 2px solid black;
}

.vertical-video-container video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.uncw-pic-text {
  font-size: 18px;
}

img {
  width: 400px;
  border: 2px solid black;
  margin-top: 8px;
}

p {
  margin-top: -15px;
  font-size: 20px;
}

</style>
