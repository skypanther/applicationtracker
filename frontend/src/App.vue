<script setup>
import { CTabs, CTabList, CTab, CTabContent, CTabPanel } from '@coreui/vue';
import Footer from './components/Footer.vue';
import { session } from './store.js'
import ApplicationsTabComponent from './components/ApplicationsTabComponent.vue';
import CompaniesTabComponent from './components/CompaniesTabComponent.vue';


</script>

<template>
  <div v-if="!session.isLoggedIn()">
    Log in <input type="text" placeholder="User name" v-model="session.username"></input><br />
    <input type="password" v-model="session.password"></input><br />
    <button @click="session.login()">Log In</button>
    <div>Simulated login form, username: admin, password: password</div>
  </div>
  <div v-else>
    <h1>ApplicationTracker</h1>
    <div id="buttonWrapper"><button id="logoutButton" type="button" @click="session.logout()">Log Out</button></div>

    <CTabs activeItemKey="applications">
      <CTabList variant="tabs">
        <CTab itemKey="applications">Applications</CTab>
        <CTab itemKey="companies">Companies</CTab>
        <CTab itemKey="contact">Contact</CTab>
      </CTabList>
      <CTabContent id="tab-wrapper">
        <CTabPanel class="p-3" itemKey="applications">
          <ApplicationsTabComponent />
        </CTabPanel>
        <CTabPanel class="p-3" itemKey="companies">
          <CompaniesTabComponent />
        </CTabPanel>
        <CTabPanel class="p-3" itemKey="contact">
          <div>Coming soon...</div>
        </CTabPanel>
      </CTabContent>
    </CTabs>





    <hr />
    <Footer />
  </div>
</template>

<style scoped></style>
