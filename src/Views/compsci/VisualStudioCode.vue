<template>
    <div class="image-container">
        <img src="../../assets/VisualStudio.png" alt="Visual Studio Code Pic" />
    </div>
    <div class="info-container">
        <h1>{{ text.Header }}</h1>
        <p v-html="text.Body"></p>

        <h1>{{ text.Links }}</h1>
        <ul class="links-list">
            <li v-for="link in links" :key="link.Name">
                <a v-if="link.WebLink" :href="link.WebLink" @click="scrollToTop" class="link">{{ link.Name }}</a>
                <router-link v-if="link.Link" :to="link.Link" @click="scrollToTop" class="link">{{ link.Name }}</router-link>
            </li>
        </ul>
    </div>
    <p style="margin-bottom: 60px;"></p>
</template>


<script setup>
import { ref } from 'vue';
import AllData from "../../data/CompSci/VisualStudioCode.json";

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];
const links = jsonData.value["Links"];

const scrollToTop = () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
};

</script>


<style scoped>
.image-container {
    position: relative;
    width: 100%;
    height: 400px;
}

.info-container {
    margin-top: -5px;
}

img {
    width: 100%; 
    height: 100%;
    display: block;
}

h1 {
    margin-left: 100px;
}

p {
    margin-left: 101px;
    font-size: 20px;
    margin-top: -14px;
    width: 80%;
}

.links-list {
    list-style-type: none;
    padding-left: 0;
    margin-left: 112px;
    margin-top: -18px;
}

.link {
    text-decoration: none;
    color: blue;
    font-size: 20px;
}

.links-list li {
    margin-bottom: 6px;
}

.link::before {
    content: "• ";
    color: black;
    text-decoration: none;
}

.link:hover {
    color: purple;
}

.link:hover::before {
     color: black;
}

@media (max-width: 700px) {
    img, .overlay {
        height: 70%;
    }

    .info-container {
        margin-top: -120px;
    }

    h1, .links-list {
        margin-left: 25px;
    }
    
    p {
        margin-left: 26px;
        width: 90%;
    }
}

</style>
