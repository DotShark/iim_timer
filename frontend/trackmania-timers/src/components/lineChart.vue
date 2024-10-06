<template>
    <div>
        <canvas ref="chart"></canvas>
    </div>
</template>

<script>
export default {
    props: ['chartData'],  // Les données pour le graphique sont passées en tant que prop
        mounted() {
    const ctx = this.$refs.chart.getContext('2d');
    new Chart(ctx, {
        type: 'line',  // Type de graphique (line dans ce cas)
        data: {
            labels: this.chartData.labels,  // Les étiquettes pour l'axe des X
            datasets: [{
                label: 'Performances des joueurs',
                data: this.chartData.data,  // Les données pour l'axe des Y
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
        });
    }
}
</script>

<style scoped>
canvas {
    max-width: 100%;
    height: 400px;  // Taille du graphique
}
</style>
