<script setup>
import { ref } from 'vue'

const count = ref(0)
defineProps(['title']);
</script>

<template>
  <div>
    <h1>Company</h1>
  </div>
</template>