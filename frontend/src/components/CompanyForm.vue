<script setup>
import { onMounted, ref, getCurrentInstance } from 'vue';

let globalProps = getCurrentInstance().appContext.config.globalProperties;

let props = defineProps(['company']);
let buttonText = ref("Submit");
var newButtonVisible = false;

const emit = defineEmits(['companyUpdated', 'clearCompany']);

function submitOrUpdate() {
    if (newButtonVisible) {
        // the button's visible so we're updating a record
        var url = `${globalProps.urlBase}/company/${props.company.company_id}`
        var requestOptions = {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(props.company)
        };
    } else {
        var url = `${globalProps.urlBase}/company/`
        var requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(props.company)
        }
    }
    fetch(url, requestOptions)
        .then(response => {
            if (!response.ok) {
                console.error(response.status);
            }
        })
        .then(data => {
            // console.log(data);
        });
    emit('companyUpdated', props.company);
}

function clearForm() {
    emit('clearCompany');
}

onMounted(() => {
    if (props.company && props.company.company_id != undefined) {
        buttonText.value = "Update";
        newButtonVisible = true;
    }
});

</script>

<template>
    <form method="post" id="companyEntryForm">
        <input type="hidden" :value="company.company_id" />
        <div id="company-form-wrapper">
            <div class="form-field form-label">
                <strong>Company:</strong>
            </div>
            <div class="form-field">
                <label for="companyname">Company Name</label><br />
                <input id="companyname" aria-label="Company Name" v-model="company.name" type=" text"
                    placeholder="Company Name" />
            </div>

            <div class="form-field">
                <label for="website">Web site</label><br />
                <input id="website" aria-label="Web Site" v-model="company.website" type=" text"
                    placeholder="Web site" />
            </div>

            <div class="form-field">
                <label for="recruitername">Recruiter Name</label><br />
                <input id="recruitername" aria-label="Recruiter Name" v-model="company.recruiter_name" type=" text"
                    placeholder="Recruiter Name" />
            </div>

            <div class="form-field">
                <label for="recruiteremail">Recruiter Email</label><br />
                <input id="recruiteremail" aria-label="Recruiter email" v-model="company.recruiter_email" type=" text"
                    placeholder="Recruiter Email" />
            </div>

            <div class="form-field" id="companyFormButtonWrapper">
                <button class="companyFormButton" id="submitUpdateButton" type="button" @click.stop="submitOrUpdate">{{
                    buttonText
                }}</button>
                <button class="companyFormButton" id="newCompanyButton" type="button" @click.stop="clearForm"
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