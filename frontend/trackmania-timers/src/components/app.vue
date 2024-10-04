<template>
<div class="container mx-auto">
    <h1 class="text-2xl font-bold mb-4">Trackmania Timers</h1>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
    <Timer v-for="timer in timers" :key="timer.id" :track="timer.track" :time="timer.time" />
    </div>
</div>
</template>

<script>
import Timer from './components/Timer.vue';
import { getTimers } from './services/timerService.js';

export default {
data() {
    return {
        timers: []
    };
},
components: {
    Timer
},
async created() {
    try {
        this.timers = await getTimers();
    } catch (error) {
        console.error('Erreur lors du chargement des timers', error);
    }
}
};
</script>
