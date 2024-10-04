<template>
<div class="timer bg-gray-800 text-white p-4 rounded-lg">
    <h2 class="text-xl font-bold">Timer pour {{ track }}</h2>
    <p>{{ time }}</p>
</div>
</template>

<script>
export default {
    props: {
        track: {
            type: String,
            required: true
        },
        time: {
            type: Number,
            required: true
        }
    }
}
</script>

<style scoped>
.timer {
    font-family: 'Roboto', sans-serif;
}
</style>
