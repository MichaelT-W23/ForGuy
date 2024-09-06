<script>

export const menuItems = [
    {
        text: "Home",
        icon: "home",
        route: "/",
    },
    {
        text: "Jobs",
        icon: "work",
        subMenu: [
            { text: "Where To Apply",        icon: "work",         link: "/Jobs/WhereToApply" },
            { text: "Resume Template",       icon: "description",  link: "/Jobs/ResumeTemplate" },
            { text: "How To Get a Job",      icon: "lightbulb",    link: "/Jobs/HowToGetAJob" },
            { text: "Offers I've Received",  icon: "handshake",    link: "/Jobs/OffersReceived" },
            { text: "Interview Tips",        icon: "group",        link: "/jobs/InterviewTips" },
            { text: "Career Path Advice",    icon: "explore",      link: "/Jobs/CareerPathAdvice" }
        ]
    },
    {
        text: "LinkedIn",
        icon: "handshake",
        subMenu: [
            { text: "What Is LinkedIn?",  icon: "person_add",      link: "/LinkedIn/WhatIsLinkedin" },
            { text: "Setup a Profile",    icon: "account_circle",  link: "/LinkedIn/SetupProfile" },
            { text: "Setup Job Alerts",   icon: "notifications",   link: "/LinkedIn/SetupJobAlerts" },
            { text: "LinkedIn Tips",      icon: "psychology",      link: "/LinkedIn/LinkedinTips" },
            { text: "Contacts",           icon: "person",          link: "/LinkedIn/Contacts" }
        ]
    },
    {
        text: "Classes",
        icon: "co_present",
        subMenu: [
            { text: "Class Recommendations",  icon: "thumb_up",       link: "/Classes/ClassRecommendations" },
            { text: "Classes I've Taken",     icon: "co_present",     link: "/Classes/ClassesIveTaken" }, //interactive_space, wysiwyg
            { text: "CSC Descriptions",       icon: "description",    link: "/Classes/CSCDescriptions" },
            { text: "Classes To Avoid",       icon: "cancel",         link: "/Classes/ClassesToAvoid" },
            { text: "Comp Sci Minor",         icon: "dvr",            link: "/Classes/CompSciMinor" },
            { text: "Useful Certifications",  icon: "editor_choice",  link: "/Classes/Certifications" }
        ] 
    },
    {
        text: "Comp Sci",
        icon: "laptop_mac",
        subMenu: [
            { text: "Visual Studio Code",  icon: "laptop_mac",         link: "/CompSci/VisualStudioCode" },
            { text: "GitHub",              icon: "hub",                link: "/CompSci/GitHub" },
            { text: "VSCode Settings",     icon: "settings",           link: "/CompSci/VSCodeSettings" },
            { text: "UI/UX Design Tips",   icon: "brush",              link: "/CompSci/UIDesignTips" },
            { text: "VSCode Extensions",   icon: "extension",          link: "/CompSci/VSCodeExtensions" },
            { text: "VSCode Shortcuts",    icon: "rocket_launch",      link: "/CompSci/VSCodeShortcuts" },
            { text: "Setup Projects",      icon: "construction",       link: "/CompSci/SetupProjects" },
            { text: "Comp Sci Tips",       icon: "device_hub",         link: "/CompSci/CompSciTips" } 
        ]
    },
    {
        text: "Other",
        icon: "folder",
        subMenu: [
            { text: "General Tips",        icon: "self_improvement",  link: "/Other/GeneralTips" },
            { text: "Apps To Download",    icon: "phone_iphone",      link: "/Other/AppsToDownload" },
            { text: "CS Stuff I Like",     icon: "favorite",          link: "/Other/CompSciStuff" },
            { text: "Terminal Commands",   icon: "terminal",          link: "/Other/TerminalCommands" },
            { text: "Keyboard Shortcuts",  icon: "bolt",              link: "/Other/KeyboardShortcuts" },
            { text: "Memes",               icon: "comedy_mask",       link: "/Other/Memes" },
            { text: "UNCW Pictures",       icon: "photo_camera",      link: "/Other/UncwPics" }
        ]
    },
    {
        text: "Contact",
        icon: "mail",
        route: "/ContactMe"
    }
];

</script>