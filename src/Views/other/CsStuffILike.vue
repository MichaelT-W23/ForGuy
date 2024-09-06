<template>
    <div class="container">
        <h1 class="gh-header">{{ text.page }}</h1>
        <p class="description">{{ text.desc }}</p>

        <h2 class="gh-header-two">{{ text.header2 }}</h2>
        <p class="description-two">{{ text.desc2 }}</p>

        <div v-for="point in csStuff" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(point.description)"></span>
            </p>
        </div>

        <h1 class="header-three">{{ text.header3 }}</h1>
        <p class="description-three">{{ text.desc3 }}</p>

        <div v-for="code in codeSyntax" :key="code.Name" class="code-blocks">
            <CodeBlock :codeInfo="code"></CodeBlock>
        </div>

        <p class="scroll-up-btn" @click="scrollToTop">{{ text.scrollToTop }}</p>

    </div>
</template>


<script setup>
import { ref } from 'vue';
import AllData from '../../data/Other/CsStuffILike.json';
import CodeBlock from '../../components/Code/CodeBlock.vue';
import { createHyperLink } from "../../utils/Markdown.vue";

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];

const csStuff = jsonData.value["CsStuff"];
const codeSyntax = jsonData.value["Code"];

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
};

</script>


<style scoped>

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.gh-header {
    text-align: left;
    border-bottom: 1.5px solid #d8dee4;
    padding-bottom: 7px;
    width: 690px;
}

.description {
    margin-top: -8px;
    font-size: 19px;
    width: 690px;
}

.bullet-pt {
    display: flex;
    align-items: flex-start;
    margin-top: -10px;
    margin-left: 20px;
    margin-bottom: 24px;
    font-size: 19px;
    width: 690px;
}

.bullet-pt-span {
    background-color: darkblue;
    border-radius: 50%;
    color: white;
    font-size: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 24px;
    height: 24px;
    min-width: 24px;
    margin-right: 10px;
    user-select: none;
    margin-bottom: 10px;
}

.gh-header-two {
    text-align: left;
    width: 690px;
}

.description-two {
    margin-top: -15px;
    font-size: 19px;
    width: 690px;
}

.header-three {
    margin-top: 40px;
    margin-bottom: -10px;
}

.description-three {
    /* margin-top: -15px; */
    font-size: 21px;
    margin-bottom: 10px;
}

.scroll-up-btn {
    text-align: center; 
    font-size: 23.5px; 
    margin-top: 25px;
    margin-bottom: 75px;
    margin-right: 40px;
    cursor: pointer;
    color: blue;
}

.scroll-up-btn:hover {
    color: darkblue;
    text-decoration: underline;
}


@media (max-width: 700px) {

    .gh-header, .description, .gh-header-two, .description-two {
        width: 100%;
        text-align: left;
        padding-left: 30px;
    }

    .bullet-pt {
        width: 92%;
    }

    .description-three {
        margin-right: 10px;
        margin-left: 10px;
    }

}

</style>