<template>
  <div class="menu-overlay">
    <div class="header">
      <span class="views-text">Views</span>
      <span class="material-icons close-icon" @click="closeMenu">close</span>
    </div>
    <div v-for="(menuItem, index) in menuItems" :key="index" class="menu-item">
      <div @click="menuItem.route ? navigateTo(menuItem.route) : toggleSubMenu(index)" class="menu-text">
        <span v-if="menuItem.icon" class="material-icons menu-icon" :class="{ 'active-text': activeIndex === index }">{{ menuItem.icon }}</span>
        <span :class="{ 'active-text': activeIndex === index }">{{ menuItem.text }}</span>
        <span v-if="menuItem.subMenu" class="material-icons expand-icon" @click.stop="toggleSubMenu(index)" :class="{ 'active-icon': activeIndex === index }">
          {{ activeIndex === index ? 'expand_less' : 'expand_more' }}
        </span>
      </div>
      <div v-if="menuItem.subMenu && activeIndex === index" class="sub-menu">
        <div v-for="(subItem, subIndex) in menuItem.subMenu" :key="subIndex" @click.stop="navigateTo(subItem.link)">
          <span class="material-symbols-outlined" style="margin-right: 8.5px">{{ subItem.icon }}</span>
          {{ subItem.text }}
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { menuItems } from './MenuItems.vue';
import { useRouter } from 'vue-router';

const emit = defineEmits(['close-menu']);
const router = useRouter();
const activeIndex = ref(null);

const closeMenu = () => {
  emit('close-menu');
};

const toggleSubMenu = (index) => {
  if (activeIndex.value === index) {
    activeIndex.value = null;
  } else {
    activeIndex.value = index;
  }
};

const navigateTo = (link) => {
  router.push(link);
  closeMenu();
};

const handleKeydown = (event) => {
  if (event.key === 'Escape') {
    closeMenu();
  }
};

onMounted(() => {
  window.addEventListener('keydown', handleKeydown);
});

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown);
});

</script>


<style scoped>
.menu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 80vw;
  height: 100vh;
  background-color: teal;
  z-index: 10;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  width: calc(100% - 40px);
  box-sizing: border-box;
}

.views-text {
  font-size: 30px;
  color: #ffd483;
}

.close-icon {
  cursor: pointer;
  font-size: 30px;
  color: white;
  margin-right: -40px;
}

.close-icon:hover {
  color: red;
}

.menu-item {
  color: white;
  cursor: pointer;
  border-top: 0.85px solid white;
  border-bottom: 0.85px solid white;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  box-sizing: border-box;
}

.menu-text:hover {
  background-color: #00C0C0;
}

.menu-text {
  display: flex;
  align-items: center;
  padding: 10px 20px;
  font-size: 1.5em;
  width: 100%;
  box-sizing: border-box;
}

.material-icons.menu-icon, .expand-icon {
  margin-right: 10px;
}

.active-text, .active-icon {
  color: #ffd483;
}

.expand-icon {
  transition: transform 0.3s;
  font-size: 30px;
  margin-left: auto;
  margin-right: 0px;
  box-sizing: border-box;
}

.sub-menu {
  width: 100%;
  background-color: rgba(0, 148, 148, 0.85);
  padding: 5px 20px;
  box-sizing: border-box;
}

.sub-menu:hover {
  background-color: rgba(0, 148, 148, 0.85);
}

.sub-menu div {
  display: flex;
  align-items: center;
  font-size: 1.07em;
  padding: 5px 0;
  margin-bottom: 6px;
  box-sizing: border-box;
}

.sub-menu div:hover {
  color: #ffd483;
}

</style>

