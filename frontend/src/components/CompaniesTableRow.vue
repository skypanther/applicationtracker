<script setup>
const props = defineProps(['companyId', 'companyName', 'website', 'recruiterName', 'recruiterEmail', 'createdAt'])

const emit = defineEmits(['companySelected']);

function companySelected() {
    emit('companySelected', props.companyId);
}

const oddEven = props.companyId % 2 == 0 ? 'even' : 'odd';
</script>

<template>
    <tr :id="companyId" :class="oddEven" class="data-row" @click="companySelected">
        <td>{{ companyId }}</td>
        <td>{{ companyName }}</td>
        <td>{{ website }}</td>
        <td>{{ recruiterName }}</td>
        <td>{{ recruiterEmail }}</td>
        <td>{{ createdAt }}</td>
    </tr>
</template>