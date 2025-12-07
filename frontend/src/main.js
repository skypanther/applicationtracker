import "./assets/main.css";

import { createApp } from "vue";
import App from "./App.vue";

const app = createApp(App);
app.config.globalProperties.urlBase = "http://127.0.0.1:8000";

app.mount("#app");
