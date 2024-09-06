import { createRouter, createWebHistory } from 'vue-router';

//Home 
import Home from '../Views/Home.vue';

//Jobs 
import WhereToApply from '../Views/jobs/WhereToApply.vue';
import ResumeTemplate from '../Views/jobs/ResumeTemplate.vue';
import HowToGetAJob from '../Views/jobs/HowToGetAJob.vue';
import OffersReceived from '../Views/jobs/OffersReceived.vue';
import InterviewTips from '../Views/jobs/InterviewTips.vue';
import CareerPathAdvice from '../Views/jobs/CareerPathAdvice.vue';

//Linkedin 
import WhatIsLinkedin from '../Views/linkedin/WhatIsLinkedin.vue';
import SetupProfile from '../Views/linkedin/SetupProfile.vue';
import SetupJobAlerts from '../Views/linkedin/SetupJobAlerts.vue';
import LinkedinTips from '../Views/linkedin/LinkedinTips.vue';
import Contacts from '../Views/linkedin/Contacts.vue';

//Classes 
import ClassRecommendations from '../Views/classes/ClassRecommendations.vue';
import CSCDescriptions from '../Views/classes/CSCDescriptions.vue';
import ClassesIveTaken from '../Views/classes/ClassesIveTaken.vue';
import ClassesToAvoid from '../Views/classes/ClassesToAvoid.vue';
import CompSciMinor from '../Views/classes/CompSciMinor.vue';
import Certifications from '../Views/classes/Certifications.vue';

//Comp Sci
import VisualStudioCode from '../Views/compsci/VisualStudioCode.vue';
import GitHubView from '../Views/compsci/GitHub.vue';
import VSCodeSettings from '../Views/compsci/VSCodeSettings/VSCodeSettings.vue';
import VSCodeExtensions from '../Views/compsci/VSCodeExtensions.vue';
import VSCodeShortcuts from '../Views/compsci/VSCodeShortcuts.vue';
import UIDesignTips from '../Views/compsci/UIDesignTips.vue';
import SetupProjects from '../Views/compsci/SetupProjects.vue'
import CompSciTips from '../Views/compsci/CompSciTips.vue';

//Other 
import GeneralTips from '../Views/other/GeneralTips.vue';
import AppsToDownload from '../Views/other/AppsToDownload.vue';
import CsStuffILike from '../Views/other/CsStuffILike.vue';
import TerminalCommands from '../Views/other/TerminalCommands.vue';
import KeyboardShortcuts from '../Views/other/KeyboardShortcuts.vue';
import Memes from '../Views/other/memes.vue';
import UncwPics from '../Views/other/UncwPictures.vue';

//Contact
import ContactMe from '../Views/contact.vue';

//Image View to display images
import ImageView from '../Views/ImageView.vue';

//Search Results view for when return in pressed when the SearchBar is open
import SearchResults from '../Views/SearchResults.vue';

//other/inaccessible
import RickRoll from '../Views/other/inaccessible/RickRoll.vue';
import FormatCode from '../Views/other/inaccessible/FormatCode.vue';


//The routes 
const routes = [
    {
        path: '/',
        component: Home
    },
    {
        path: '/Jobs/WhereToApply',
        component: WhereToApply
    },
    {
        path: '/Jobs/ResumeTemplate',
        component: ResumeTemplate
    },
    {
        path: '/Jobs/OffersReceived',
        component: OffersReceived
    },
    {
        path: '/Jobs/InterviewTips',
        component: InterviewTips
    },
    {
        path: '/Jobs/HowToGetAJob',
        component: HowToGetAJob
    },
    {
        path: '/Jobs/CareerPathAdvice',
        component: CareerPathAdvice
    },
    {
        path: '/LinkedIn/WhatIsLinkedIn',
        component: WhatIsLinkedin
    },
    {
        path: '/LinkedIn/SetupProfile',
        component: SetupProfile
    },
    {
        path: '/LinkedIn/SetupJobAlerts',
        component: SetupJobAlerts
    },
    {
        path: '/LinkedIn/LinkedinTips',
        component: LinkedinTips
    },
    {
        path: '/LinkedIn/Contacts',
        component: Contacts
    },
    {
        path: '/Classes/ClassRecommendations',
        component: ClassRecommendations
    },
    {
        path: '/Classes/CSCDescriptions',
        component: CSCDescriptions
    },
    {
        path: '/Classes/ClassesIveTaken',
        component: ClassesIveTaken
    },
    {
        path: '/Classes/ClassesToAvoid',
        component: ClassesToAvoid
    },
    {
        path: '/Classes/CompSciMinor',
        component: CompSciMinor
    },
    {
        path: '/Classes/Certifications',
        component: Certifications
    },
    {
        path: '/CompSci/VisualStudioCode',
        component: VisualStudioCode
    },
    {
        path: '/CompSci/GitHub',
        component: GitHubView
    },
    {
        path: '/CompSci/VSCodeSettings',
        component: VSCodeSettings
    },
    {
        path: '/CompSci/VSCodeExtensions',
        component: VSCodeExtensions
    },
    {
        path: '/CompSci/VSCodeShortcuts',
        component: VSCodeShortcuts
    },
    {
        path: '/CompSci/UIDesignTips',
        component: UIDesignTips
    },
    {
        path: '/CompSci/SetupProjects',
        component: SetupProjects
    },
    {
        path: '/CompSci/SetupProjects/:section',
        name: 'CompSci',
        component: SetupProjects,
        props: true
    },
    {
        path: '/CompSci/CompSciTips',
        component: CompSciTips
    },
    {
        path: '/Other/GeneralTips',
        component: GeneralTips
    },
    {
        path: '/Other/AppsToDownload',
        component: AppsToDownload
    },
    {
        path: '/Other/CompSciStuff',
        component: CsStuffILike
    },
    {
        path: '/Other/TerminalCommands',
        component: TerminalCommands
    },
    {
        path: '/Other/KeyboardShortcuts',
        component: KeyboardShortcuts
    },
    {
        path: '/Other/Memes',
        component: Memes
    },
    {
        path: '/Other/UncwPics',
        component: UncwPics
    },
    {
        path: '/ContactMe',
        component: ContactMe
    },
    {
        path: '/WhatIsThis',
        component: RickRoll
    },
    {
        path: '/FormatCode',
        component: FormatCode
    },
    {
        path: '/image-view/:Name/:Description/:Pic',
        name: 'ImageView',
        component: ImageView,
        props: true
    },
    {
        path: '/SearchResults/:SearchQuery',
        name: 'SearchResults',
        component: SearchResults,
        props: true
    }
]

const router = createRouter({
    history: createWebHistory('/ForGuy/'),
    routes
});

export default router;