<template>
  <div class="container">
    <div class="aligned-container">
      <div class="text-container">
        <h2 v-if="codeInfo.Name" class="code-name">{{ codeInfo.Name }}</h2>
        <p v-if="codeInfo.Description" class="description" v-html="highlightLinkText(codeInfo.Description)"></p>
      </div>
      <div class="code-block" :style="{ backgroundColor: codeBlockBackgroundColor }">
        <div class="copy-bar">
          <span class="language-name">{{ codeInfo.DisplayLang || codeInfo.Language }}</span>
          <span class="material-icons copy-icon" 
               :class="{'icon-done': copyIcon === 'done'}" 
               :style="{ color: copyIcon === 'done' ? '#00FF4D' : getLanguageColor }"
               @click="copyCode"
           >{{ copyIcon }}</span>
        </div>
        <pre><code v-html="highlightedCode"></code></pre>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watchEffect } from 'vue';
import { highlightLinkText } from '../../utils/Markdown.vue'
import Prism from 'prismjs';
import 'prismjs/components/prism-python';
import 'prismjs/components/prism-java';
import 'prismjs/components/prism-javascript';
import 'prismjs/components/prism-swift';
import 'prismjs/components/prism-fxml';
import 'prismjs/components/prism-json';
import 'prismjs/components/prism-sh';
import 'prismjs/components/prism-customswift';
import 'prismjs/components/prism-swiftcustom';
import 'prismjs/components/prism-customsql';
import 'prismjs/components/prism-customproperties';
import 'prismjs/themes/prism-coy.css';
import './custom.css';

const props = defineProps({
  codeInfo: {
    type: Object,
    default: () => ({
      Name: "",
      Description: "",
      Language: "",
      DisplayLang: "",
      FormatCode: "",
      CopyCode :""
    }),
    required: true,
  },
});

const copyIcon = ref('content_copy');

const copyCode = () => {
  navigator.clipboard.writeText(props.codeInfo.CopyCode)
    .then(() => {
      copyIcon.value = 'done';
      setTimeout(() => copyIcon.value = 'content_copy', 2000);
    })
    .catch(err => {
      console.error("Failed to copy code to clipboard! ", err)
    });
};

const highlightedCode = computed(() => {
  if (props.codeInfo.Language === null) {
    return `<span style="color: #C1C1C1;">${props.codeInfo.FormatCode}</span>`;
  }

  const language = props.codeInfo.Language.toLowerCase();
  
  const prismLanguage = Prism.languages[language] || Prism.languages.plain;
  return Prism.highlight(props.codeInfo.FormatCode, prismLanguage, language);
});

const getLanguageColor = computed(() => {
  const language = props.codeInfo.DisplayLang || props.codeInfo.Language;
  
  const colors = {
    python: '#3572A5',
    java: '#C6821E',
    javascript: '#f1e05a',
    typescript: '#3178c6',
    angular: '#dd0031',
    swift: '#F05138',
    ruby: '#701516',
    vue: '#41b883',
    css: '#563d7c',
    html: '#E34C26',
    react: '#61DAFB',
    json: '#FF9A00'
  };

  const colorKey = language.toLowerCase().trim();
  return colors[colorKey] || "#DFC200";
});

const codeBlockBackgroundColor = computed(() => {
  return /customswift|swift/.test(props.codeInfo.Language.toLowerCase().trim()) ? '#18171B' : '#282C34';
});

watchEffect(() => {
  document.documentElement.style.setProperty('--dynamic-width', props.codeInfo.Name === '' ? '640px' : '700px');
});

</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    width: 100%;
}

.aligned-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: var(--dynamic-width);
}

.text-container, .code-block {
    width: 100%;
}

.code-name {
    margin-left: 4px;
    font-size: 23px;
}

.description {
    margin-top: -15px;
    margin-left: 4px;
    font-size: 17px;
}

.code-block {
    width: var(--dynamic-width);
    margin: 20px 0;
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: #282C34;
    color: white;
    margin-top: -5px;
}

.language-name {
    color: #D5D5D5;
    font-size: 10px;
}

.copy-icon {
    cursor: pointer;
    font-size: 22px;
}

.copy-icon:hover {
    filter: brightness(80%);
}

.icon-done {
    color: #00FF4D;
}

.icon-done:hover {
    color: #00FF4D;
}

.copy-bar {
    position: sticky;
    display: flex;
    justify-content: space-between;
    background-color: gray;
    padding: 5px;
}

.language-name {
  flex-grow: 1;
  font-size: 20px;
  margin-left: 6px;
}

code {
  background-color: inherit;
  border-radius: 3px;
  font-size: 14px;
  margin-left: 16px;
  line-height: 20px;
  white-space: pre;
  display: block;
  overflow-x: auto;
  padding-right: 16px;
}

@media (max-width: 700px) {
    .aligned-container {
        width: 500px;
    }

    .copy-bar {
        justify-content: start;
    }

    .language-name {
        flex-grow: 0;
        margin-right: 10px;
    }

    .copy-icon {
        order: -1;
    }
}
</style>
