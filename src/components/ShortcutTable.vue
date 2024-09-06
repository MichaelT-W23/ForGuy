<template>
    <div class="center-container">
        <div class="header-container">
            <h1>{{ title }}</h1>
            <p>{{ description }}</p>
        </div>
        <div class="shortcut-table-container">
            <table>
                <thead>
                <tr>
                    <th>Shortcut</th>
                    <th>Description</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(item, index) in shortcuts" 
                    :key="item.id" 
                    :class="{'row-odd': index % 2 === 0, 'row-even': index % 2 !== 0}">
                    <td>{{ item.Shortcut }}</td>
                    <td v-html="createRouterLink(item.Action)"></td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>


<script setup>

import { createRouterLink } from "../utils/Markdown.vue";

const props = defineProps({
    title: String,
    description: String,
    shortcuts: Array
});

</script>


<style scoped>

table {
  width: 70%;
  border-collapse: separate; 
  border-spacing: 0;
  border: 1px solid black;
  margin-top: -8px;
}

th, td {
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
  padding: 8px;
  border-left: none;
  border-right: none;
  text-align: left;
}

th {
  background-color: #000080;
  color: #ffffff;
  border-top: none;
}

.row-odd {
  background-color: #ffffff;
}

.row-even {
  background-color: #f2f2f2;
}

tbody tr:first-of-type td {
  border-top: none;
}

.center-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 80%;
    margin: auto;
}

.header-container {
    align-self: flex-start;
    width: 100%;
    padding-left: 15.5%;
}

.shortcut-table-container {
    width: 100%;
    display: flex;
    justify-content: center;
}

p {
    word-wrap: break-word;
    margin-top: -13px;
    margin-bottom: 17px;
    padding-right: 31%;
}

@media (max-width: 700px) {
    .shortcut-table-container, .header-container {
        width: 100%;
        padding-left: 2%;
        padding-right: 2%;
    }

    p {
        padding-right: 8.5%;
    }

    table {
        width: 100%;
    }
}

</style>

