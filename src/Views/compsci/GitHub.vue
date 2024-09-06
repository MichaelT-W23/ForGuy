<template>
    <div class="container">
        <h1 class="gh-header">{{ text[0].title }}</h1>
        <p class="description">{{ text[0].desc }}</p>
        <img src="../../assets/GitHub.png" alt="GitHub" class="github-pic"/>
        
        <h2 class="gh-header-two">{{ text[1].title }}</h2>
        <p class="description-two">{{ text[1].desc }}</p>
        

        <h2 class="gh-header-two" style="margin-top: -3px;" ref="scrollLinksRef">{{ text[2].title }}</h2>
        <p class="description-two">{{ text[2].desc }}</p>
        <div v-for="link in scrollLinks" :key="link.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ link.id }}
                </span><span v-html="createRefContent(link)"></span></p>
        </div>

        <!-- How to create a GitHub account Section -->
        <h2 class="gh-header-two" ref="createGHAccount">{{ text[3].title }}</h2>
        <p class="description-two">{{ text[3].desc }}</p>

        <div v-for="point in setupGitHub" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

        <!-- How to create a GitHub Repository Section -->
        <h2 class="gh-header-two" ref="createGHRepo">{{ text[4].title }}</h2>
        <p class="description-two">{{ text[4].desc }}</p>

        <div v-for="point in createGitHubRepo" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

        <!-- How to create a Second GitHub account Section -->
        <h2 class="gh-header-two" ref="multipleGHAccounts">{{ text[5].title }}</h2>
        <p class="description-two">{{ text[5].desc }}</p>

        <div v-for="point in setupSecondGitHub" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

        <!-- How to create a Second GitHub Repository Section -->
        <h2 class="gh-header-two" ref="multipleDifferentAccount">{{ text[6].title }}</h2>
        <p class="description-two">{{ text[6].desc }}</p>

        <div v-for="point in createSecondGitHubRepo" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

        <!-- Git Commands -->
        <h2 class="gh-header-two" ref="GitCommands">{{ text[7].title }}</h2>
        <p class="description-two">{{ text[7].desc }}</p>

        <CmdTable tableName="" :items="gitCommands" class="cmd-table"></CmdTable>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

        <!-- General Tips for Working with GitHub -->
        <h2 class="gh-header-two" ref="GeneralTips">{{ text[8].title }}</h2>
        <p class="description-two">{{ text[8].desc }}</p>

        <div v-for="tip in generalTips" :key="tip.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ tip.id }}</span><span v-html="createHyperLink(tip.instruction)"></span></p>
            <span v-if="tip.Code"><CodeBlock :codeInfo="tip.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>  

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

        <!-- Three Main Commands -->
        <h2 class="gh-header-two" ref="ThreeCommands">{{ text[9].title }}</h2>
        <p class="description-two">{{ text[9].desc }}</p>

        <CmdTable tableName="" :items="threeCommands" class="cmd-table"></CmdTable>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

        <!-- Upload Existing Folder section -->
        <h2 class="gh-header-two" ref="ForkRepo">{{ text[10].title }}</h2>
        <p class="description-two">{{ text[10].desc }}</p>

        <div v-for="point in createFork" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>


        <!-- Reset To Previous Branch -->
        <h2 class="gh-header-two" ref="resetBranch">{{ text[11].title }}</h2>
        <p class="description-two">{{ text[11].desc }}</p>

        <div v-for="point in resetBranchSteps" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

        <!-- Reset to Single File -->
        <h2 class="gh-header-two" ref="ResetSingleFile">{{ text[12].title }}</h2>
        <p class="description-two">{{ text[12].desc }}</p>

        <div v-for="point in resetSingleFile" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>


        <!-- Upload Existing Folder section -->
        <h2 class="gh-header-two" ref="ExistingCmds">{{ text[13].title }}</h2>
        <p class="description-two">{{ text[13].desc }}</p>

        <div v-for="point in existingFolderPts" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <CmdTable tableName="" :items="existingFolderCmds" class="cmd-table"></CmdTable>
        
        <p></p>

        <div v-for="point in existingFolderPtsTwo" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <CmdTable tableName="" :items="existingFolderCmdsTwo" class="cmd-table"></CmdTable>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>
        



        <!-- CSC 450 Workflow -->
        <h2 class="gh-header-two" ref="CSC450Workflow">{{ text[14].title }}</h2>
        <p class="description-two" v-html="createDownloadLink(text[14].desc)"></p>

        <div v-for="point in csc450WorkflowPtsOne" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <CmdTable tableName="" :items="csc450WorkflowOne" class="cmd-table" style="margin-bottom: 30px"></CmdTable>


        <div v-for="point in csc450WorkflowPtsTwo" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <CmdTable tableName="" :items="csc450WorkflowTwo" class="cmd-table" style="margin-bottom: 30px"></CmdTable>

        <div v-for="point in csc450WorkflowPtsThree" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <CmdTable tableName="" :items="csc450WorkflowThree" class="cmd-table" style="margin-bottom: 30px"></CmdTable>

        <div v-for="point in csc450WorkflowPtsFour" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <CmdTable tableName="" :items="csc450WorkflowFour" class="cmd-table" style="margin-bottom: 30px"></CmdTable>

        <div v-for="point in csc450WorkflowPtsFive" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>


        <!-- Amotions Workflow -->
        <h2 class="gh-header-two" ref="AmotionsWorkflow">{{ text[15].title }}</h2>
        <p class="description-two">{{ text[15].desc }}</p>


        <CmdTable tableName="" :items="amotionsWorkflowOne" class="cmd-table"></CmdTable>

        <p class="centered-txt">{{ text[16].amotions }}</p>

        <CmdTable tableName="" :items="amotionsWorkflowTwo" class="cmd-table"></CmdTable>

        <p class="centered-txt">{{ text[17].amotions }}</p>

        <div v-for="point in amotionsPts" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <p class="centered-txt">{{ text[18].amotions }}</p>

        <div v-for="point in amotionsPtsTwo" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <p class="centered-txt">{{ text[19].amotions }}</p>

        <CmdTable tableName="" :items="amotionsWorkflowThree" class="cmd-table"></CmdTable>
        
        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

        <!-- Pull Changes From Main  -->
        <h2 class="gh-header-two" ref="MergeMain">{{ text[21].title }}</h2>
        <p class="description-two">{{ text[21].desc }}</p>


        <div v-for="point in pullChangesFromMain" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

        <!-- Resolve Merge Conflicts  -->
        <h2 class="gh-header-two" ref="MergeConflicts">{{ text[22].title }}</h2>
        <p class="description-two">{{ text[22].desc }}</p>

        <div v-for="point in resolveMergeConflicts" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>

        <span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

        <!-- Your Section Name  -->
        <h2 class="gh-header-two" ref="RemoveFile">{{ text[23].title }}</h2>
        <p class="description-two">{{ text[23].desc }}</p>

        <div v-for="point in removeFileFromGitHistory" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>

        
        <!-- Scroll Up To Top Button -->
        <p class="scroll-up-btn" @click="scrollToTop">{{ text[20].scrollToTop }}</p>
    
    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import AllData from '../../data/CompSci/GitHub.json';
import CmdTable from "../../components/CommandTable.vue";
import { createHyperLink, createDownloadLink } from "../../utils/Markdown.vue";
import CodeBlock from '../../components/Code/CodeBlock.vue';

const jsonData = ref(AllData);

const scrollLinks = jsonData.value["ScrollLinks"];
const setupGitHub = jsonData.value["SetupGitHub"];
const createGitHubRepo = jsonData.value["CreateGitHubRepo"];
const setupSecondGitHub = jsonData.value["SetupSecondGitHub"];
const createSecondGitHubRepo = jsonData.value["CreateSecondGitHubRepo"];
const gitCommands = jsonData.value["GitCommands"];
const generalTips = jsonData.value["GeneralTips"];
const threeCommands = jsonData.value["ThreeCommands"];
const createFork = jsonData.value["CreateFork"];
const resetBranchSteps = jsonData.value["ResetBranch"];
const resetSingleFile = jsonData.value["RevertSingleFile"];
const existingFolderPts = jsonData.value["ExistingFolderPts"];
const existingFolderCmds = jsonData.value["ExistingFolder"];
const existingFolderPtsTwo = jsonData.value["ExistingFolderPtsTwo"];
const existingFolderCmdsTwo = jsonData.value["ExistingFolderTwo"];
const csc450WorkflowPtsOne = jsonData.value["CSC450WorkflowPtsOne"];
const csc450WorkflowOne = jsonData.value["CSC450WorkflowOne"];
const csc450WorkflowPtsTwo = jsonData.value["CSC450WorkflowPtsTwo"];
const csc450WorkflowTwo = jsonData.value["CSC450WorkflowTwo"];
const csc450WorkflowPtsThree = jsonData.value["CSC450WorkflowPtsThree"];
const csc450WorkflowThree = jsonData.value["CSC450WorkflowThree"];
const csc450WorkflowPtsFour = jsonData.value["CSC450WorkflowPtsFour"];
const csc450WorkflowFour = jsonData.value["CSC450WorkflowFour"];
const csc450WorkflowPtsFive = jsonData.value["CSC450WorkflowPtsFive"];
const amotionsWorkflowOne = jsonData.value["AmotionsWorkflowOne"];
const amotionsWorkflowTwo = jsonData.value["AmotionsWorkflowTwo"];
const amotionsWorkflowThree = jsonData.value["AmotionsWorkflowThree"];
const amotionsPts = jsonData.value["AmotionsPts"];
const amotionsPtsTwo = jsonData.value["AmotionsPtsTwo"];
const pullChangesFromMain = jsonData.value["PullChangesFromMain"];
const resolveMergeConflicts = jsonData.value["ResolveMergeConflicts"];
const removeFileFromGitHistory = jsonData.value["RemoveFileFromGitHistory"];
const text = jsonData.value["Text"];

// Add refs here. Actual ref name from json file.
const scrollLinksRef = ref(null);
const createGHAccount = ref(null);
const createGHRepo = ref(null);
const multipleGHAccounts = ref(null);
const multipleDifferentAccount = ref(null);
const GitCommands = ref(null);
const GeneralTips = ref(null);
const ThreeCommands = ref(null);
const ForkRepo = ref(null);
const resetBranch = ref(null);
const ResetSingleFile = ref(null);
const ExistingCmds = ref(null);
const CSC450Workflow = ref(null);
const AmotionsWorkflow = ref(null);
const MergeMain = ref(null);
const MergeConflicts = ref(null);
const RemoveFile = ref(null);
const secondSix = ref(null);
const secondSeven = ref(null);
const secondNine = ref(null);
const secondTwentyThree = ref(null);
const secondGitHubSeven = ref(null);
const secondGitHubEight = ref(null);
const secondGitHubNine = ref(null);
const normalSix = ref(null);
const normalSeven = ref(null);
const normalNine = ref(null);
const normalTwentyThree = ref(null);
const normalGitHubSeven = ref(null);
const normalGitHubEight = ref(null);
const normalGitHubNine = ref(null);

const scrollToRef = (refName) => {
    const offset = 20;

    const refs = {
        scrollLinksRef,
        createGHAccount,
        createGHRepo,
        multipleGHAccounts,
        multipleDifferentAccount,
        GitCommands,
        GeneralTips,
        ThreeCommands,
        ForkRepo,
        resetBranch,
        ResetSingleFile,
        ExistingCmds,
        CSC450Workflow,
        AmotionsWorkflow,
        MergeMain,
        MergeConflicts,
        RemoveFile,
        secondSix,
        secondSeven,
        secondNine,
        secondTwentyThree,
        secondGitHubSeven,
        secondGitHubEight,
        secondGitHubNine,
        normalSix,
        normalSeven,
        normalNine,
        normalTwentyThree,
        normalGitHubSeven,
        normalGitHubEight,
        normalGitHubNine
    };

    const targetElement = refs[refName]?.value;

    if (targetElement) {
        const elementPosition = targetElement.getBoundingClientRect().top + window.scrollY;
        const offsetPosition = elementPosition - offset;

        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });

        history.replaceState(null, null, `#${refName}`);
    } else {
        console.warn("No target element found for refName:", refName);
    }
};

const scrollToTop = () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
};

const createRefContent = (refVal) => {
    return `<span><a href="#${refVal.ref}" class="scroll-down" data-ref-name="${refVal.ref}">${refVal.name}</a></span>`;
};

const processedTipContent = (tip) => {
    return tip.replace(/(Different for multiple accounts|Scroll back up to original step|Scroll back to links)\((.*?)\)/g, (match, phrase, refName) => {
        return `<a href="#${refName}" class="scroll-down" data-ref-name="${refName}">${phrase}</a>`;
    });
};

onMounted(() => {
    document.querySelectorAll('.scroll-down').forEach(element => {
        element.addEventListener('click', (event) => {
            event.preventDefault();
            const refName = event.target.getAttribute('data-ref-name');
            scrollToRef(refName);
        });
    });

    const handleHashChange = () => {
        const hash = window.location.hash.substring(1);

        if (hash) {
            scrollToRef(hash);
        }
    };

    handleHashChange();

    window.addEventListener('hashchange', handleHashChange);
});
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

.centered-txt {
    text-align: center; 
    font-size: 23.5px; 
    margin-top: 25px;
    margin-bottom: 25px;
    margin-right: 40px;
    cursor: pointer;
    color: black;
    font-weight: bold;
}

.description {
    margin-top: -8px;
    font-size: 19px;
    width: 690px;
}

.github-pic {
    width: 690px;
    height: 280px;
    margin-top: -5px;
}

.cmd-table {
    margin-top: -25px;
    width: 690px;
}

.gh-header-two {
    text-align: left;
    width: 690px;
}

.description-two {
    margin-top: -15px;
    font-size: 19px;
    width: 690px;
    margin-bottom: 27px;
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

:deep(.scroll-down) {
    text-decoration: none;
    color: blue;
    cursor: pointer;
}

:deep(.scroll-down:hover) {
    text-decoration: underline;
    color: darkblue;
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

.scroll-up-link {
    text-align: center; 
    font-size: 23.5px; 
    margin-top: 15px;
    margin-right: 40px;
    cursor: pointer;
    color: blue;
    margin-top: 25px;
    margin-bottom: 30px;
}

.scroll-up-btn {
    text-align: center; 
    font-size: 23.5px; 
    margin-top: 15px;
    margin-right: 40px;
    cursor: pointer;
    color: blue;
    margin-top: 50px;
    margin-bottom: 50px;
}

.scroll-up-btn:hover {
    color: darkblue;
    text-decoration: underline;
}

@media (max-width: 700px) {
    .gh-header {
        width: 490px;
    }
    
    .description {
        width: 490px;
    }

    .github-pic {
        width: 490px;
        height: 200px;
    }
    
    .cmd-table {
        width: 490px;
    }

    .gh-header-two {
        width: 490px;
    }

    .description-two {
        width: 490px;
    }

    .bullet-pt {
        width: 490px;
    }
}
</style>
