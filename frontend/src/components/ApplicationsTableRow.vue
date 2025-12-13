<script setup>
const props = defineProps(['companyId', 'jobAppId', 'jobTitle', 'stageId', 'companyName', 'website', 'recruiterName', 'recruiterEmail', 'createdAt', 'stages'])

const emit = defineEmits(['jobAppSelected']);

function jobAppSelected() {
    emit('jobAppSelected', props.jobAppId);
}

function getStageName(stage_id) {
    const stage = props.stages.find(obj => obj.stage_id == stage_id)
    if (!stage) {
        return stage_id;
    }
    return stage.name;
}

const oddEven = props.jobAppId % 2 == 0 ? 'even' : 'odd';
</script>

<template>
    <tr :id="jobAppId" :class="oddEven" class="data-row" @click="jobAppSelected">
        <td>{{ jobAppId }}</td>
        <td>{{ companyName }}</td>
        <td>{{ jobTitle }}</td>
        <td>{{ getStageName(stageId) }}</td>
        <td>{{ website }}</td>
        <td>{{ recruiterName }}</td>
        <td>{{ recruiterEmail }}</td>
        <td>{{ createdAt }}</td>
    </tr>
</template>