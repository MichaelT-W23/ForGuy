<template>
  <div class="accordion-menu">
    <div class="accordion-title" @click="toggleAccordion">
      <h2>{{ item.Name }}</h2>
      <span v-if="!isOpen"><span class="material-icons" id="open">add_circle</span></span>
      <span v-else><span class="material-icons" id="close">cancel</span></span>
    </div>
    <div class="accordion-content" v-if="isOpen">
      <ul>
        <li v-for="(entry, index) in filteredEntries" :key="index">

          <!-- entry[0] is the underlined attribute name. If it's an array don't add : -->
          <b style="margin-right: 3px;"><u>{{ entry[0] }}</u>{{ typeof entry[1] === 'string' ? ':' : ""}}</b>

          <!-- Display it if it's just a string -->
          <span v-if="typeof entry[1] === 'string'" v-html="entry[1]"></span>
          <ul class="menu-attribute" v-else>
            <li v-for="(item, idx) in entry[1]" :key="`item-${idx}`" v-html="item" class="menu-items"></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</template>


<script setup>
import { ref, computed, watchEffect, toRefs } from 'vue';
import {
  highlightLinkText,
  createHyperLink,
  createRouterLink,
  createRouterLinkWithProps
} from '../utils/Markdown.vue';

const props = defineProps({
  item: Object,
  isOpen: Boolean
});

const { item, isOpen: isOpenProp } = toRefs(props);
const isOpen = ref(isOpenProp.value);

watchEffect(() => {
  isOpen.value = isOpenProp.value;
});

const toggleAccordion = () => {
  isOpen.value = !isOpen.value;
};

const shouldDisplay = (key) => {
  const excludedKeys = ['Name'];
  return !excludedKeys.includes(key);
};

const formatEntry = (value) => {

  if (typeof value === 'string') {

    if ((value.includes('(http://') || value.includes('(https://'))) {
      return createHyperLink(value);
    }

    if (!value.includes("@[")) { //RouterLinksWithProps can contain link in prop string.
      value = highlightLinkText(value);
    }


    value = createRouterLink(value);
    value = createRouterLinkWithProps(value);
  
  }

  return value;

};

const filteredEntries = computed(() => {
  return Object.entries(item.value)
    .filter(([key, value]) => value && shouldDisplay(key))
    .map(([key, value]) => {

      if (Array.isArray(value)) {
        value = value.map(formatEntry);
      } else {
        value = formatEntry(value);
      }

      return [key, value];

    });
});

</script>


<style scoped>
.accordion-menu {
  border: 1px solid #ccc;
  border-radius: 5px;
  margin: 10px auto;
  padding: 10px; 
  background-color: #f0f0f0;
  width: 80%; 
  max-width: none; 
}

.accordion-title h2 {
  cursor: pointer;
  margin: 0;
  display: inline-block;
  font-size: 22px; 
}

.accordion-title span {
  vertical-align: middle;
  float: right;
  font-weight: bold;
}

.accordion-content {
  margin-top: 20px;
  font-size: 18.5px;
}

.menu-attribute {
  margin-top: 10px; /* Changes vertical spacing of menu */
}

.menu-items {
  list-style-type: disc;
  margin-left: 23px;
  margin-top: -4px;
}

.accordion-content ul {
  padding: 0;
  list-style-type: none;
}

.accordion-content li {
  margin-bottom: 13px;
}

#open, #close {
  vertical-align: middle;
  color: teal;
  font-size: 28px;
  cursor: pointer;
}

</style>
