<template>
    <div>
      <header>
        <div class="top-menu" @mouseover="showMenu = true" @mouseout="hideMenu">
          <div class="menu-items" v-show="!isSearchBarOpen">  
            <div
              class="menu-item"
              v-for="(menuItem, index) in menuItems"
              :key="index"
              @mouseover="menuItem.subMenu ? showSubMenu(index) : null; 
                          hoveredOver = menuItem.subMenu ? true : false"

              @mouseout="menuItem.subMenu ? hideSubMenu : null; 
                         hoveredOver = false"   
              @click="handleMenuClick(menuItem.route)"
            >
              <span>{{ menuItem.text }}
                <i class="material-icons" :style="{ opacity: menuItem.subMenu ? 1 : 0, width: menuItem.subMenu ? 1 : 0}">
                  {{ activeSubMenuIndex === index && hoveredOver && menuItem.subMenu ? 'expand_less' : 'expand_more' }}
                </i>
              </span>
              <div
                class="sub-menu"
                v-if="menuItem.subMenu"
                v-show="showMenu && activeSubMenuIndex === index"
                @mouseover="showSubMenu(index)"
                @mouseout="hideSubMenu"
              >
                <ul>
                  <li v-for="(subMenuItem, subIndex) in menuItem.subMenu" :key="subIndex" class="sub-menu-item">
                    <router-link 
                      :to="subMenuItem.link" 
                      class="sub-menu-link"
                      @click="hideSubMenu" 
                    >
                      <span class="material-symbols-outlined">{{ subMenuItem.icon }}</span>
                      <span>{{ subMenuItem.text }}</span>
                    </router-link>
                  </li>
                </ul>
              </div>
            </div>
              <span v-if="!isSearchBarOpen"
                class="material-icons" 
                @click="toggleSearchBar" 
                style="flex-shrink: 0; margin-top: 3.25px">
                search
              </span>
            </div>
            <div class="overlay" v-if="isSearchBarOpen"></div>
          <SearchBar v-if="isSearchBarOpen" @close-search="isSearchBarOpen = false" @remove-overlay="handleRemoveOverlay"></SearchBar>
        </div>
      </header>
    </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import router from '../router';
import SearchBar from './SearchBar.vue';
import { menuItems } from './MenuItems.vue';

const showMenu = ref(false);
const activeSubMenuIndex = ref(null);
const hoveredOver = ref(false);
const isSearchBarOpen = ref(false);

const showSubMenu = (index) => {
  activeSubMenuIndex.value = index;
};

const hideSubMenu = () => {
  activeSubMenuIndex.value = null;
};

const hideMenu = () => {
  showMenu.value = false;
};

const toggleSearchBar = (event) => {
  isSearchBarOpen.value = !isSearchBarOpen.value;
  event.stopPropagation();
};

const handleMenuClick = (link) => {
  router.push(link);
};

const closeSearchOnOutsideClick = (event) => {
  if (event.target.closest('.overlay')) { //Used to be ! .top-menu
    isSearchBarOpen.value = false;
  }
};

const handleRemoveOverlay = (isVisible) => {
  const overlay = document.querySelector('.overlay');
  overlay.style.backgroundColor = isVisible ? 'rgba(0, 0, 0, 0.6)' : 'rgba(0, 0, 0, 0)';
}

onMounted(() => {
  window.addEventListener('click', closeSearchOnOutsideClick);
});

onUnmounted(() => {
  window.removeEventListener('click', closeSearchOnOutsideClick);
});

</script>


<style scoped>

.overlay {
  position: fixed;
  top: 60.24px;
  left: 0;
  width: 100%;
  height: calc(100% - 40px);
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 1;
}

.top-menu {
  background-color: teal;
  color: #fff;
  padding: 10px 0;
  min-height:40px;
}

.menu-items {
  display: flex;
  justify-content: space-between;
  max-width: 800px;
  margin: 0 auto;
}

.menu-item {
  position: relative;
  cursor: pointer;
  /* padding: 10px 15px; top right bottom left*/
  padding: 2.5px 11px 10px 14px;
  transition: background-color 0.3s ease;
}

.menu-item:hover {
  color: #ffd483;
  background-color: #009494; 
  border-radius: 3px; 
} 

.sub-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: teal;
  padding: 0px 10px; 
  border-radius: 0 0 5px 5px;
  z-index: 1;
  white-space: nowrap; 
  min-width: 100%; 
}

.sub-menu-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.sub-menu-link {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: #fff;
  width: 100%;
  padding: 5px 0;
  padding-left: 2px;
  padding-right: 2px;
}

.sub-menu-link:hover {
  background-color: #009494; 
}

.material-symbols-outlined {
  margin-right: 8px; 
  margin-top: -1.7px; 
}

.menu-item:hover .sub-menu {
  display: block;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px; 
  padding: 5px 0; 
  font-size: 17px;
}

a {
  text-decoration: none;
  color: #fff;
}

a:hover {
  color:#ffd483;
}

.material-icons {
  transform: translateY(5.1px); 
}

.material-icons:hover {
  color: #ffd483;
  cursor: pointer;
}

</style>