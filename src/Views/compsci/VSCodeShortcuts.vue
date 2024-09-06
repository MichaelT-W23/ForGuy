<template>
    <div v-for="shortcutSet in shortcutSets" :key="shortcutSet.title">
      <ShortcutTable
        :title="shortcutSet.title"
        :description="shortcutSet.description"
        :shortcuts="shortcutSet.shortcuts"
      ></ShortcutTable>
      <p style="margin-bottom: 25px;"></p>
    </div>
    <p style="margin-bottom: 100px;"></p>
</template>


<script setup>
import { ref } from "vue";
import AllData from '../../data/CompSci/VSCodeShortcuts.json';
import ShortcutTable from '../../components/ShortcutTable.vue';

const jsonData = ref(AllData);

const shortcutSets = Object.keys(jsonData.value).map(key => ({
    title: jsonData.value[key].Title,
    description: jsonData.value[key].Description,
    shortcuts: jsonData.value[key].Shortcuts,
}));

</script>
