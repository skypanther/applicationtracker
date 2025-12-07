import { reactive } from "vue";

export const store = reactive({
  companiesCount: 0,
  applicationsCount: 0,
  setCompaniesCount(val) {
    this.companiesCount = val;
  },
  setApplicationsCount(val) {
    this.applicationsCount = val;
  },
});
