<template>
    <router-link :to="resultPage.Link" class="no-style-link">
        <div class="search-card">
            <h2 class="title"><span>{{ resultPage.Title }}</span></h2>
            
            <div v-for="result in resultPage.MatchedResults" :key="result.title">
                <div v-for="(value, key) in result" :key="key">
                    <div class="result">
                        <span>•  <span v-html="value"></span></span>
                    </div>
                </div>
            </div>

        </div>
    </router-link>
</template>


<script setup>

const props = defineProps({
  resultPage: {
    type: Object,
    required: true,
    default: () => ({})
  }
});

</script>


<style scoped>

.search-card {
    padding: 0px 30px 10px 30px; /* Top, right, bottom, left */
    border: 1px solid #727272;
    border-radius: 5px;
    width: 600px;
    margin: 20px auto;
    position: relative;
    overflow: hidden;
    background: white;
    transition: background-color 0.3s;
}
  
.search-card:hover {
    border: 1px solid blue;
    cursor: pointer;
}

.search-card:hover .title span {
    color: darkblue;
}

.no-style-link {
    text-decoration: none; 
    color: inherit; 
    display: inline;
}

.title span {
    border-bottom: 1px solid #ccc;
    padding-bottom: 1px;
    display: inline-block;
    width: 100%;
}

.search-card .result {
    margin-bottom: 20px; 
    margin-right: 16px;
}

.title {
    margin-bottom: 20px;
}

.search-card div {
    margin-bottom: 7px;
}

.search-card p {
    padding: 0px 15px 0px 0px;
}

@media (max-width: 700px) {
    .search-card {
        width: 425px;
    }
}

</style>

  
  
  