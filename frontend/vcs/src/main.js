import Vue from 'vue'
import App from './App.vue'


import VuePrismEditor from "vue-prism-editor";
import "vue-prism-editor/dist/VuePrismEditor.css";
Vue.component("prism-editor", VuePrismEditor);

import VueResource from 'vue-resource'
Vue.use(VueResource);

import "prismjs";
import "prismjs/themes/prism-okaidia.css";

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
