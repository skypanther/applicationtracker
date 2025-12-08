<script setup>
const props = defineProps(['companyId', 'jobAppId', 'jobTitle', 'companyName', 'website', 'recruiterName', 'recruiterEmail', 'createdAt'])

const emit = defineEmits(['jobAppSelected']);

function jobAppSelected() {
    emit('jobAppSelected', props.jobAppId);
}

const oddEven = props.jobAppId % 2 == 0 ? 'even' : 'odd';
</script>

<template>
    <tr :id="jobAppId" :class="oddEven" class="data-row" @click="jobAppSelected">
        <td>{{ jobAppId }}</td>
        <td>{{ companyName }}</td>
        <td>{{ jobTitle }}</td>
        <td>{{ website }}</td>
        <td>{{ recruiterName }}</td>
        <td>{{ recruiterEmail }}</td>
        <td>{{ createdAt }}</td>
    </tr>
</template>