<template>
    <ShortcutTable 
        :title="text.Title" 
        :description="text.Description" 
        :shortcuts="shortcuts">
    </ShortcutTable>
    <p style="margin-bottom: 100px;"></p>
</template>


<script setup>
import { ref } from 'vue';
import AllData from '../../data/Other/KeyboardShortcuts.json';
import ShortcutTable from '../../components/ShortcutTable.vue';

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];
const shortcuts = jsonData.value["Shortcuts"];

</script>