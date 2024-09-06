<template>
    <div class="container">
        <h1>Paste Your Code below</h1>
        <textarea v-model="inputText" placeholder="Enter text here"></textarea>
        <div class="dropdown-submit-container">
            <div class="dropdown-container">
                <select v-model="langSelection">
                    <option disabled value="">Select Language</option>
                    <option v-for="option in firstOptions" :key="option">{{ option }}</option>
                </select>
                <select v-model="formatSelection">
                    <option disabled value="">Select Format</option>
                    <option v-for="option in secondOptions" :key="option">{{ option }}</option>
                </select>
            </div>
            <button :disabled="isSubmitDisabled" :class="{ disabled: isSubmitDisabled }" @click="handleSubmit">Submit</button>
        </div>
    </div>
    <div style="margin-top: 50px"></div>

    <div class="input-submit-container">
        <h1>Test Your Code Here</h1>
        <div class="input-button-row">
            <input v-model="codeInfoText" placeholder="Paste code here" />
            <button @click="submitCodeInfo">Submit</button>
        </div>
    </div>

    <div style="margin-top: 20px"></div>

    <CodeBlock :codeInfo="codeInfo"></CodeBlock>

    <div style="margin-top: 50px"></div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import CodeBlock from '../../../components/Code/CodeBlock.vue';

const inputText = ref(localStorage.getItem('inputText') || '');
const langSelection = ref(localStorage.getItem('langSelection') || '');
const formatSelection = ref(localStorage.getItem('formatSelection') || '');

const codeInfo = ref({
    Name: '',
    Description: '',
    Language: '',
    FormatCode: '',
    CopyCode: '',
});

const codeInfoText = ref('');

const firstOptions = ['Python', 'Java', 'Swift', 'HTML', 'Javascript', 'JSON', 'CSS'];
const secondOptions = ['FormatCode', 'CopyCode', 'Both'];

const isSubmitDisabled = computed(() => {
    return !inputText.value || !langSelection.value || !formatSelection.value;
});

watch(inputText, (newVal) => {
    localStorage.setItem('inputText', newVal);
});

watch(langSelection, (newVal) => {
    localStorage.setItem('langSelection', newVal);
});

watch(formatSelection, (newVal) => {
    localStorage.setItem('formatSelection', newVal);
});

const handleSubmit = () => {
    if (!isSubmitDisabled.value) {
      languagesSelected(inputText.value, formatSelection.value);
    }
};

const languagesSelected = (code, format) => {
  if (format == 'FormatCode') {
    copyToClipboard(getFormattedString(code));
  } else if (format == 'CopyCode') {
    copyToClipboard(getCopyString(code));
  } else {
    copyToClipboard(getBothStrings(code));
  }
};


const getFormattedString = (str) => {
  if (str.includes("\\'")) {
    alert("Code cannot contain an escaped single quote -> \\'. Modify your code.");
    throw new Error("STOP PROGRAM: Single quote found.");
  }

  return str.replace(/\\n/g, '\\\\n')
            .replace(/(?<!\\)\n/g, '\\n')
            .replace(/\\\"/g, '\\\\\\"')
            .replace(/(?<!\\)"/g, '\\"')
            .replace(/\t/g, '    ')
            .replace(/\\\./g, '\\\\.')
            .replace(/\\\(/g, '\\\\(');
};


const getCopyString = (str) => {
  if (str.includes("\\'")) {
    alert("Code cannot contain an escaped single quote -> \\'. Modify your code.");
    throw new Error("STOP PROGRAM: Single quote found.");
  }

  return str.replace(/\\n/g, '\\\\n')
            .replace(/(?<!\\)\n/g, '\\n')
            .replace(/\\\"/g, '\\\\\\"')
            .replace(/(?<!\\)"/g, '\\"')
            .replace(/\t/g, '\\t')
            .replace(/\\\./g, '\\\\.')
            .replace(/\\\(/g, '\\\\(');
};


const getBothStrings = (str) => {
    const formattedString = getFormattedString(str);
    const copyString = getCopyString(str);
    return `"FormatCode": "${formattedString}",\n"CopyCode": "${copyString}"`;
};

const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text).then(() => {
        alert('Text copied to clipboard!');
    }).catch(err => {
        console.error('Error copying text: ', err);
    });
};

const convertRawStringToSingleString = (rawString) => {
    return rawString.replace(/(?<!\\)\\n/g, '\n')
                    .replace(/\\t/g, '\t')
                    .replace(/\\"/g, '\"')
                    .replace(/\\\\/g, '\\');
}

const submitCodeInfo = () => {
    const escapedText = convertRawStringToSingleString(codeInfoText.value);

    codeInfo.value = {
        Name: "",
        Description: "",
        Language: `${langSelection.value}`,
        FormatCode: escapedText,
        CopyCode: escapedText
    };
};

</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

textarea {
  margin-bottom: 10px;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 700px;
  height: 400px;
  font-size: 16px;
}

.dropdown-submit-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 700px;
  margin-bottom: 10px;
}

.dropdown-container {
  display: flex;
  gap: 10px;
}

select {
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

button {
  padding: 12px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

button.disabled {
  background-color: gray;
  cursor: not-allowed;
}

button:hover:not(.disabled) {
  background-color: #0056b3;
}

.input-submit-container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  margin-top: 20px;
}

.input-button-row {
  display: flex;
  gap: 10px;
  align-items: center;
}

input {
  width: 500px;
  height: 25px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

input::placeholder {
  color: #ccc;
}

input + button {
  padding: 8px 16px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

input + button:hover {
  background-color: #0056b3;
}

.input-submit-container > h1 {
  margin-bottom: 10px;
}

</style>
