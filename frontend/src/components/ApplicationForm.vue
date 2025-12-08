<script setup>
import { onMounted, ref, getCurrentInstance } from 'vue';

let globalProps = getCurrentInstance().appContext.config.globalProperties;

let props = defineProps(['jobApp']);
let buttonText = ref("Submit");
var newButtonVisible = false;
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
    if (newButtonVisible) {
        modifiedJobApp["job_app_id"] = parseInt(props.jobApp.job_app_id);
        // the button's visible so we're updating a record
        var url = `${globalProps.urlBase}/job_app/${modifiedJobApp.job_app_id}`
        var requestOptions = {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(modifiedJobApp)
        };
        updatedOrAddedJobAppId = modifiedJobApp.job_app_id;
    } else {
        console.log('here')
        var url = `${globalProps.urlBase}/job_app`
        var requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
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
            console.log('AppForm.vue', data);
            if (!newButtonVisible) {
                updatedOrAddedJobAppId = data.job_app_id
            }
        });
    setTimeout(() => {
        console.log('updatedOrAddedJobAppId', updatedOrAddedJobAppId);
        emit('jobAppUpdated', updatedOrAddedJobAppId);
    }, 100);
}

function clearForm() {
    emit('clearJobApp');
}

onMounted(() => {
    if (props.jobApp && props.jobApp.job_app_id != undefined) {
        buttonText.value = "Update";
        newButtonVisible = true;
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
                <label for="companyid">Company ID</label><br />
                <input id="companyid" aria-label="Company ID" v-model="jobApp.company_id" type=" text"
                    placeholder="Company ID" />
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
                <label for="stageId">Stage ID</label><br />
                <input id="stageId" aria-label="Stage ID" v-model="jobApp.stage_id" type=" text"
                    placeholder="Stage ID" />
            </div>

            <div class="form-field" id="companyFormButtonWrapper">
                <button class="companyFormButton" id="submitUpdateButton" type="button" @click.stop="submitOrUpdate">{{
                    buttonText
                }}</button>
                <button class="companyFormButton" id="newJobAppButton" type="button" @click.stop="clearForm"
                    v-if="newButtonVisible">New</button>
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