<template>
    <div>
      <h1 class="header">{{ text.page }}</h1>
      <p class="description">{{ text.desc }}</p>
      <div class="bar">
        <span class="settings-header">{{ text.header }}</span>
        <button @click="downloadJson" ref="downloadButton">{{ text.downloadBtn }}</button>
        <button @click="copyJson" ref="copyButton">{{ text.copyBtn }}</button>
      </div>
      <div v-if="isWideScreen">
        <div class="json-container">
          <pre v-html="highlightedJson"></pre>
        </div>
      </div>
      <div v-else>
        <img src="./Settings.jpg" class="settings-pic">
      </div>
    </div>
</template>


<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import Prism from 'prismjs';
import AllData from '../../../data/CompSci/settings.json';
import 'prismjs/components/prism-json';
import 'prismjs/themes/prism-coy.css';
import './custom.css';
import { settings } from '../../../data/CompSci/settings.vue';
//import 'prismjs/themes/prism-solarizedlight.css';

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];

const copyButton = ref(null);
const downloadButton = ref(null);


const windowWidth = ref(window.innerWidth);

const updateWidth = () => {
  windowWidth.value = window.innerWidth;
};

onMounted(() => {
  window.addEventListener('resize', updateWidth);
});

onUnmounted(() => {
  window.removeEventListener('resize', updateWidth);
});

const isWideScreen = computed(() => windowWidth.value >= 875);


const copyJson = () => {
  navigator.clipboard.writeText(settings)
      .then(() => {
          copyButton.value.innerText = 'Copied!';
          setTimeout(() => copyButton.value.innerText = "Copy JSON", 2000); 
      })
      .catch(err => {
          console.error('Failed to copy JSON: ', err);
      });
};

const downloadJson = () => {
  const blob = new Blob([settings], { type: 'application/json' });
  const link = document.createElement('a');

  link.href = URL.createObjectURL(blob);
  link.download = 'settings.json';

  document.body.appendChild(link);
  link.click();

  document.body.removeChild(link);
  URL.revokeObjectURL(link.href);
    
  downloadButton.value.innerText = 'Downloaded!';

  setTimeout(() => {
    downloadButton.value.innerText = "Download JSON";
  }, 2000); 
}

const highlightedJson = computed(() => {
  return Prism.highlight(settings, Prism.languages.json, 'json');
});

</script>


<style scoped>

.header, .description {
  margin: 0 auto; 
  max-width: 70%; 
  box-sizing: border-box;
}

.header {
  margin-top: 15px;
  padding-left: 1px; 
}

.description {
  font-size: 18.5px;
  padding-left: 2px; 
  margin-top: 6.3px;
}

.bar {
  background-color: gray;
  padding: 10px;
  display: flex;
  justify-content: flex-end; 
  gap: 10px;
  margin: 20px auto 0 auto; 
  max-width: 70%; 
  box-sizing: border-box; 
}
  
.settings-header {
  flex-grow: 1;
  font-size: 34px;
  color: #D5D5D5;
  margin-left: 10px;
  font-weight: 525;
}

.json-container {
  margin: 0 auto; 
  max-width: 70%; 
  box-sizing: border-box; 
}

button {
  background-color: #CDB100;
  color: white;
  padding: 8px 18px;
  font-size: 14.5px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #AF9800;
}

pre {
  background-color: #282C34;
  padding: 10px;
  margin-top: 0; 
  box-sizing: border-box; 
}

@media (max-width: 875px) {

  .header {
    max-width: 87%; 
  }

  .description {
    max-width: 87%; 
  }

  .json-container {
    display: none;
  }
  
  .settings-pic {
    max-width: 90%;
    margin: 0 auto; 
    margin-bottom: 30px;
  }

  .bar {
    max-width: 90%;
  }

  button {
    padding: 4px 9px;
    font-size: 14.5px;
  }

}

</style>
