<template>
  <div class="center-container">
    <div class="content-container">
      <h1 class="header">{{ header }}</h1>
      <p class="description">{{ description }}</p>
      <div class="info-bar">
        <span class="page-number">{{ currentPage }}/{{ numOfPages }}</span>
        <button @click="downloadResumeDocx" ref="downloadButton">Download DOCX</button>
      </div>
      <div class="pdf-page-container" @scroll="updateCurrentPage">
        <img v-for="(pic, index) in resumePics" :src="pic" :key="`page-${index}`" alt="PDF Page" class="pdf-page-image"/>
      </div>
    </div>
  </div>
  <p style="margin-bottom: 40px;"></p>
</template>


<script setup>
import { ref } from 'vue';
import AllData from '../../data/jobs/ResumeTemplateText.json'
import ResumePic1 from "../../assets/Resume/Template1.png";
import ResumePic2 from "../../assets/Resume/Template2.png";

const resumePics = ref([ResumePic1, ResumePic2]);
const currentPage = ref(1);
const numOfPages = 2;
const downloadButton = ref(null);

const jsonData = ref(AllData);
const info = jsonData.value["information"];

const header = info[0].title;
const description = info[0].description;


function downloadResumeDocx() {
  //Can't use local path for security reasons 
  const docxUrl = '/download/ResumeTemplate.docx';
  const link = document.createElement('a');
  link.href = docxUrl;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);

  downloadButton.value.innerText = 'Downloaded!';

  setTimeout(() => {
    downloadButton.value.innerText = "Download DOCX";
  }, 2000); 
}


function updateCurrentPage(event) {
  const container = event.target;
  const scrollPosition = container.scrollTop + container.offsetHeight;
  const pageHeight = container.scrollHeight / numOfPages;
  currentPage.value = Math.min(numOfPages, Math.round(scrollPosition / pageHeight));
}

</script>


<style scoped>

.center-container {
  display: flex;
  justify-content: center;
  width: 100%;
}

.content-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 700px;
}

.header, .description {
  align-self: flex-start;
  margin: 0;
  padding: 0;
}

.header {
  margin-top: 20px;
}

.description {
  margin-top: 3px;
  font-size: 18px;
}

.pdf-page-container {
  width: 700px;
  max-height: 800px;
  overflow-y: auto;
  border: 1.5px solid #000000;
  margin-bottom: 0;
}

.pdf-page-image {
  width: 100%;
  display: block;
  border-bottom: 1px solid black;
}

.info-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: gray;
  width: 703.5px;
  padding: 10px;
  box-sizing: border-box;
  margin-top: 15px;
}

.page-number {
  font-size: 22px;
  color: #D5D5D5;
  font-weight: 525;
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


@media (max-width: 700px) {

  .content-container {
    width: 91%;
  }

  .pdf-page-container {
    width: 100%;
  }

  .info-bar {
    width: 100.61%;
  }

}

</style>
