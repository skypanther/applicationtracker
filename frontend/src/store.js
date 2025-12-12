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

export const session = reactive({
  loggedIn: !!localStorage.getItem("user"),
  user: {},
  username: "",
  password: "",
  async login() {
    // Simulated delay
    await new Promise((resolve) => setTimeout(resolve, 500));

    if (this.username == "admin" && this.password == "password") {
      this.user = { username: "Admin", userId: 1 };
      localStorage.setItem("user", JSON.stringify(this.user));
      this.loggedIn = true;
      this.clearUsernamePassword();
      return true;
    }
  },
  logout() {
    this.user = {};
    localStorage.removeItem("user");
    this.loggedIn = false;
    this.clearUsernamePassword();
  },
  isLoggedIn() {
    return this.loggedIn;
  },
  clearUsernamePassword() {
    this.username = "";
    this.password = "";
  },
});
