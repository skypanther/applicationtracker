<script setup>
import { onMounted, ref, getCurrentInstance } from 'vue';
import CompanyForm from './components/CompanyForm.vue';
import TableRow from './components/TableRow.vue';
import Footer from './components/Footer.vue';
import { store } from './store.js'
import ApplicationForm from './components/ApplicationForm.vue';

let globalProps = getCurrentInstance().appContext.config.globalProperties;
let jobApps = ref([]);
let jobApp = ref({});
let company = ref({});
let companyName = "";
let jobAppKey = "";
var jobAppTracker = Math.random();

const getJobApplications = () => {
  fetch(`${globalProps.urlBase}/job_app`)
    .then(response => response.json())
    .then(data => {
      jobApps.value = data;
      // console.log(data)
      store.setApplicationsCount(data.length);
    });
  jobAppTracker = Math.random();
  // company.value = {};
  // companyName = "";
}

onMounted(() => {
  getJobApplications();
});

function loadJobApp(jobAppId) {
  fetch(`${globalProps.urlBase}/job_app/${jobAppId}`, {
    headers: {
      'Access-Control-Allow-Origin': '*'
    }
  })
    .then(response => response.json())
    .then(data => {
      console.log('app.vue', 'loadJobApp', data)
      jobApp.value = data;
      jobAppKey = data.job_app_id;
      companyName = data.company_name;
      jobAppTracker = Math.random();
      clearJobApp();
      getJobApplications();
    })
}

function clearCompany() {
  company.value = {};
  companyName = "";
}
function clearJobApp() {
  jobApp.value = {};
  jobAppKey = null;
}
</script>

<template>
  <h1>ApplicationTracker</h1>
  <CompanyForm :company="company" :key="companyName" @company-updated="getJobApplications"
    @clear-company="clearCompany" />
  <ApplicationForm :jobApp="jobApp" :key="jobAppKey" @job-app-updated="loadJobApp" @clear-job-app="clearJobApp" />
  <hr>
  </hr>

  <div>
    <table>
      <thead>
        <tr>
          <th>Job App ID</th>
          <th>Company Name</th>
          <th>Job Title</th>
          <th>Source URL</th>
          <th>Recruiter Name</th>
          <th>Recruiter Email</th>
          <th>Created Date</th>
        </tr>
      </thead>
      <TableRow :key="jobAppTracker" @job-app-selected="loadJobApp" v-for="jobApp in jobApps"
        :companyId="jobApp.company_id" :jobAppId="jobApp.job_app_id" :companyName="jobApp.company_name"
        :website="jobApp.source_url" :jobTitle="jobApp.job_title" :recruiterName="jobApp.recruiter_name"
        :recruiterEmail="jobApp.recruiter_email" :createdAt="jobApp.application_datetime" />
    </table>

  </div>
  <hr />
  <Footer />
</template>

<style scoped></style>
