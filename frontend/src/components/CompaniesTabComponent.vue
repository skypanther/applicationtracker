<script setup>
import { onMounted, ref, getCurrentInstance } from 'vue';
import { store } from '../store.js'
import CompanyForm from './CompanyForm.vue';
import CompaniesTableRow from './CompaniesTableRow.vue';
let globalProps = getCurrentInstance().appContext.config.globalProperties;

let companies = ref([]);
let company = ref({});
let companyName = "";
var companyTracker = Math.random();

const getCompanies = () => {
    fetch(`${globalProps.urlBase}/company`)
        .then(response => response.json())
        .then(data => {
            companies.value = data;
            store.setCompaniesCount(data.length);
            companyTracker = Math.random();
        })
        .finally(() => {
            clearCompany();
        });
}

function loadCompany(companyId, isEdited) {
    fetch(`${globalProps.urlBase}/company/${companyId}`)
        .then(response => response.json())
        .then(data => {
            company.value = data;
            companyName = data.name;
            companyTracker = Math.random();
            if (isEdited) {
                clearCompany();
                getCompanies();
            }
        })
}

function clearCompany() {
    company.value = {};
    companyName = null;
}

onMounted(() => {
    getCompanies();
});


</script>

<template>
    <div>
        <CompanyForm :company="company" :key="companyName" @company-updated="getCompanies"
            @clear-company="clearCompany" />

        <table>
            <thead>
                <tr>
                    <th>Company ID</th>
                    <th>Company Name</th>
                    <th>Web site</th>
                    <th>Recruiter Name</th>
                    <th>Recruiter Email</th>
                    <th>Created Date</th>
                </tr>
            </thead>
            <CompaniesTableRow :key="companyTracker" @company-selected="loadCompany" v-for="co in companies"
                :companyId="co.company_id" :companyName="co.name" :website="co.website"
                :recruiterName="co.recruiter_name" :recruiterEmail="co.recruiter_email" :createdAt="co.created_at" />
        </table>

    </div>
</template>

<style scoped></style>