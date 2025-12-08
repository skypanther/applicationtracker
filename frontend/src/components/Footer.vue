<script setup>
import { store } from '../store.js'
</script>

<template>
    <div class="footer">
        <div>Total Applications: {{ store.applicationsCount }}</div>
        <div>Total Companies: {{ store.companiesCount }}</div>
    </div>
</template>

<style scoped>
.footer {
    display: flex;
    column-gap: 3em;
}
</style>