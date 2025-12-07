<script setup>
import { onMounted, ref, getCurrentInstance } from 'vue';
import CompanyForm from './components/CompanyForm.vue';
import TableRow from './components/TableRow.vue';
import Footer from './components/Footer.vue';
import { store } from './store.js'

let globalProps = getCurrentInstance().appContext.config.globalProperties;
let jobApps = ref([]);
let company = ref({});
let companyName = "";
var companyListTracker = Math.random();

const getCompanies = () => {
  fetch(`${globalProps.urlBase}/company`)
    .then(response => response.json())
    .then(data => {
      jobApps.value = data;
      store.setCompaniesCount(data.length);
    });
  companyListTracker = Math.random();
  company.value = {};
  companyName = "";
}

onMounted(() => {
  getCompanies();
});

function loadCompany(companyId) {
  fetch(`${globalProps.urlBase}/company/${companyId}`)
    .then(response => response.json())
    .then(data => {
      company.value = data;
      companyName = data.name;
    })
}

function clearCompany() {
  company.value = {};
  companyName = "";
}
</script>

<template>
  <h1>ApplicationTracker</h1>
  <CompanyForm :company="company" :key="companyName" @company-updated="getCompanies" @clear-company="clearCompany" />
  <hr>
  </hr>
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
    <TableRow :key="companyListTracker" @company-selected="loadCompany" v-for="jobApp in jobApps"
      :companyId="jobApp.company_id" :companyName="jobApp.name" :website="jobApp.website"
      :recruiterName="jobApp.recruiter_name" :recruiterEmail="jobApp.recruiter_email" :createdAt="jobApp.created_at" />
  </table>
  <hr />
  <Footer />
</template>

<style scoped></style>
