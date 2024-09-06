<template>
    <div class="centered">
        <h1 class="title">You've been Rick rolled! 🎉😼😼💯🔥🔥</h1>
        <video class="horizontal-video-container" controls>
            <source src="/RickRoll.mp4" type="video/mp4" />
            Your browser does not support the video tag.
        </video>
    </div>
</template>


<style scoped>

.centered {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.title {
    width: 80%;
}

.horizontal-video-container {
    width: 63%;
    height: 63%;
    margin-bottom: 100px;
    border: 1.5px solid gray;
}

</style>