<template>
  <div v-if="isOpen" class="overlay" @keydown="handleKeydown" tabindex="0">
    <button class="close-btn" @click="closeGalleryView">
      <div class="icon-container">
        <span class="material-symbols-outlined">close</span>
      </div>
    </button>
    <div class="image-container">
      <div class="image-background">
        <transition name="fade">
          <template v-if="currentItemType === 'image'">
            <img :src="currentItem" alt="Displayed Image" />
          </template>
          <template v-else-if="currentItemType === 'video'">
            <video controls>
              <source :src="currentItem" type="video/mp4" />
              Your browser does not support the video tag.
            </video>
          </template>
        </transition>
        <p v-if="caption" class="caption">{{ caption }}</p>
      </div>
      <button class="nav-btn left" @click="prevItem">
        <span class="material-symbols-outlined chevron">chevron_left</span>
      </button>
      <button class="nav-btn right" @click="nextItem">
        <span class="material-symbols-outlined chevron">chevron_right</span>
      </button>
    </div>
    <div class="controls">
      <button
        v-for="(item, index) in items"
        :key="index"
        :class="{'active': index === currentIndex}"
        @click="currentIndex = index"
      ></button>
    </div>
  </div>
</template>


<script setup>
import { ref, computed, onMounted } from 'vue';

const props = defineProps({
  items: Array,
  initialIndex: Number,
  isOpen: Boolean,
});

const emit = defineEmits(['close']);

const currentIndex = ref(props.initialIndex);

const closeGalleryView = () => {
  emit('close');
};

const currentItem = computed(() => {
  const item = props.items[currentIndex.value];
  return item.image || item.video;
});

const currentItemType = computed(() => {
  const item = props.items[currentIndex.value];
  return item.image ? 'image' : 'video';
});

const caption = computed(() => props.items[currentIndex.value].text);

const handleKeydown = (event) => {
  if (event.key === 'ArrowRight') {
    nextItem();
  } else if (event.key === 'ArrowLeft') {
    prevItem();
  } else if (event.key === 'Escape') {
    closeGalleryView();
  }
};

const nextItem = () => {
  if (currentIndex.value < props.items.length - 1) {
    currentIndex.value += 1;
  } else {
    currentIndex.value = 0;
  }
};

const prevItem = () => {
  if (currentIndex.value > 0) {
    currentIndex.value -= 1;
  } else {
    currentIndex.value = props.items.length - 1;
  }
};

onMounted(() => {
  document.querySelector('.overlay').focus();
});

</script>


<style scoped>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: black;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.overlay:focus {
  outline: none;
}

.close-btn {
  position: absolute;
  top: 20px;
  right: 40px;
  background: none;
  border: none;
  padding: 0;
  z-index: 1001;
  cursor: pointer;
}

.icon-container {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: transparent;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  transition: background-color 0.3s ease;
}

.icon-container:hover {
  background-color: gray;
}

.icon-container .material-symbols-outlined {
  font-size: 24px;
  color: white;
}

.image-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.image-container img {
  max-width: 100%;
  height: 80vh;
}

.image-container video {
  max-width: 100%;
  max-height: 80vh;
}

.nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.nav-btn.left {
  left: 40px;
}

.nav-btn.right {
  right: 40px;
}

.nav-btn:hover {
  background-color: gray;
}

.chevron {
  font-size: 40px;
  color: white;
}

.controls {
  position: absolute;
  bottom: 20px;
  left: 20px;
  display: flex;
  gap: 8px;
}

.controls button {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: none;
  background-color: grey;
  cursor: pointer;
}

.controls button.active {
  background-color: white;
}

.caption {
  color: #999;
  margin-top: 10px;
  text-align: center;
  font-size: 16.5px;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s ease-in-out;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

@media (max-width: 680px) {
  .image-container img {
    max-width: 400px;
    height: 60vh;
  }

  .nav-btn.left {
    left: 20px;
  }
  
  .nav-btn.right {
    right: 20px;
  }

  .close-btn {
    right: 20px;
  }

  .icon-container {
    width: 30px;
    height: 30px;
  }

  .icon-container .material-symbols-outlined {
    font-size: 20px;
  }
}

</style>
