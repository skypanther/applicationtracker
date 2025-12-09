<script setup>
import { onMounted, ref, getCurrentInstance } from 'vue';

let globalProps = getCurrentInstance().appContext.config.globalProperties;

let props = defineProps(['jobApp', 'stages']);
let buttonText = ref("Add");
let companies = ref([]);
var clearButtonVisible = false;
var updatedOrAddedJobAppId = null;

const emit = defineEmits(['jobAppUpdated', 'clearJobApp']);

function submitOrUpdate() {
    let modifiedJobApp = {
        "job_title": props.jobApp.job_title,
        "company_id": props.jobApp.company_id,
        "source": props.jobApp.source,
        "source_url": props.jobApp.source_url,
        "stage_id": parseInt(props.jobApp.stage_id)
    };
    if (clearButtonVisible) {
        modifiedJobApp["job_app_id"] = parseInt(props.jobApp.job_app_id);
        // the button's visible so we're updating a record
        var url = `${globalProps.urlBase}/job_app/${modifiedJobApp.job_app_id}`
        var requestOptions = {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
            body: JSON.stringify(modifiedJobApp)
        };
        updatedOrAddedJobAppId = modifiedJobApp.job_app_id;
    } else {
        var url = `${globalProps.urlBase}/job_app`
        var requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
            body: JSON.stringify(modifiedJobApp)
        }
    }
    fetch(url, requestOptions)
        .then(response => {
            if (!response.ok) {
                console.error(response.status);
            }
            return response.json()
        })
        .then(data => {
            // console.log('AppForm.vue', data);
            if (!clearButtonVisible) {
                updatedOrAddedJobAppId = data.job_app_id
            }
        });
    let isEdited = true;
    setTimeout(() => {
        // console.log('updatedOrAddedJobAppId', updatedOrAddedJobAppId);
        emit('jobAppUpdated', updatedOrAddedJobAppId, isEdited);
    }, 100);
}

function clearForm() {
    emit('clearJobApp');
}

onMounted(() => {
    fetch(`${globalProps.urlBase}/company`)
        .then(response => response.json())
        .then(data => {
            companies.value = data;
        });

    if (props.jobApp && props.jobApp.job_app_id != undefined) {
        buttonText.value = "Update";
        clearButtonVisible = true;
    }
});

</script>

<template>
    <form method="post" id="companyEntryForm">
        <input type="hidden" :value="jobApp.company_id" />
        <div id="company-form-wrapper">
            <div class="form-field form-label">
                <strong>Application:</strong>
            </div>
            <div class="form-field">
                <label for="job_title">Job Title</label><br />
                <input id="job_title" aria-label="Web Site" v-model="jobApp.job_title" type=" text"
                    placeholder="Job Title" />
            </div>

            <div class="form-field">
                <label for="company">Company Name</label><br />
                <select v-model="jobApp.company_id" aria-placeholder="Select a company">
                    <option disabled value="">Please select one</option>
                    <option v-for="company in companies" :value="company.company_id">
                        {{ company.name }}
                    </option>
                </select>

            </div>

            <div class="form-field">
                <label for="source">Source</label><br />
                <input id="source" aria-label="Source" v-model="jobApp.source" type=" text" placeholder="Source" />
            </div>

            <div class="form-field">
                <label for="sourceUrl">Source URL</label><br />
                <input id="sourceUrl" aria-label="Source URL" v-model="jobApp.source_url" type=" text"
                    placeholder="Source URL" />
            </div>

            <div class="form-field">
                <label for="stageId">Stage</label><br />
                <select v-model="jobApp.stage_id" aria-placeholder="Select a stage">
                    <option disabled value="">Please select one</option>
                    <option v-for="stage in stages" :value="stage.stage_id">
                        {{ stage.name }}
                    </option>
                </select>
            </div>

            <div class="form-field" id="companyFormButtonWrapper">
                <button class="companyFormButton" id="submitUpdateButton" type="button" @click.stop="submitOrUpdate">{{
                    buttonText
                    }}</button>
                <button class="companyFormButton" id="clearJobAppButton" type="button" @click.stop="clearForm"
                    v-if="clearButtonVisible">Clear</button>
            </div>
        </div>
    </form>
</template>

<style scoped>
.form-label {
    padding-top: 15px;
    font-weight: bold;
    border-right: 1px solid #000;
    margin-right: 10px;
}
</style>