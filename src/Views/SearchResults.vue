<template>
    <div class="container">
        <h1 class="search-header">Search Results</h1>
        
        <p class="description">The search term <span style="color: darkblue">"{{ searchQuery }}"</span> 
        appears in the following pages: <span><strong style="color: darkblue">{{ totalCount }} time{{ totalCount === 1 ? '' : 's' }}</strong></span></p>

        <SearchCard v-for="item in searchResults" :key="item.Title" :resultPage="item" />
        
        <!-- If no results were found show this image and text -->
        <img :src="ShrugPhoto" alt="No results" class="shrug-photo" v-if="totalCount === 0">
        <p class="no-results-txt" v-if="totalCount === 0">No Results! Better luck next time!</p>

        <p style="margin-bottom: 60px;"></p>
    </div>
</template>


<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import SearchData from "../data/SearchData.json";
import SearchCard from "../components/SearchResultCard.vue";
import ShrugPhoto from '../assets/Shrug.png';
  
const route = useRoute();
const searchQuery = ref(route.params.SearchQuery || '');
const searchResults = ref([]);
const totalCount = ref(0);

// Replaces html < and > with &lt; and &gt; to be searchable
function escapedSearchQuery(query) {
    return query
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
}

function highlightString(text, searchQuery) {
    const searchLength = searchQuery.length;
    let highlightedText = '';
    let idx = 0;
    let count = 0;
    const lowerText = text.toLowerCase();
    const lowerSearchQuery = searchQuery.toLowerCase();
    
    while (idx < text.length) {
        const nextFind = lowerText.indexOf(lowerSearchQuery, idx);

        if (nextFind === -1) {
            highlightedText += text.substring(idx);
            break;
        }
        
        highlightedText += text.substring(idx, nextFind) +
                         `<span style="background-color: yellow">${text.substring(nextFind, nextFind + searchLength)}</span>`;
                         
        idx = nextFind + searchLength;
        count++;
    }

    return { highlightedText, count };
}

//searchInResults was above.
function searchJson(data, searchQuery) {
    const allMatches = [];
    let totalHighlights = 0;
    
    data.forEach(item => {
        let matchedResults = [];
        let localCount = 0;
        
        if (item.Results) {
            item.Results.forEach(result => {
                let resultMatched = false; 
                
                const newResult = {};
                
                for (const key in result) {
                    const value = result[key];
                    
                    if (typeof value === 'string' && value.toLowerCase().includes(searchQuery.toLowerCase())) {
                        const { highlightedText, count } = highlightString(value, searchQuery);
                        newResult[key] = highlightedText;
                        localCount += count;
                        resultMatched = true;
                    }
                }
                
                if (resultMatched) {
                    matchedResults.push(newResult);
                }
            });
            
            if (matchedResults.length > 0) {
                allMatches.push({
                    Title: item.Title,
                    Link: item.Link,
                    MatchedResults: matchedResults
                });
                
                totalHighlights += localCount;
            }
        }
    });
    
    totalCount.value = totalHighlights;
    return allMatches;
}

onMounted(() => {
    const escapedQuery = escapedSearchQuery(searchQuery.value);
    searchResults.value = searchJson(SearchData, escapedQuery);
});

watch(() => route.params.SearchQuery, (newSearchQuery) => {
    searchQuery.value = newSearchQuery;
    const escapedQuery = escapedSearchQuery(searchQuery.value);
    searchResults.value = searchJson(SearchData, escapedQuery);
});

</script>


<style scoped>

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.shrug-photo {
    width: 400px; 
    margin-top: 20px; 
    margin-left: 200;
    border: 0.5px solid black;
}

.no-results-txt {
    font-size: 22px;
    color: darkblue;
    margin-top: 10px;
}

.search-header {
    text-align: left;
    border-bottom: 1.5px solid #d8dee4;
    padding-bottom: 7px;
    width: 690px;
}

.description {
    margin-top: -8px;
    font-size: 19px;
    width: 690px;
    margin-bottom: 4px;
}

@media (max-width: 700px) {
    .search-header, .description {
        width: 490px;
    }
}

</style>