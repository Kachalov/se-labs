import Vue from 'vue';
import VueResource from 'vue-resource';
import Vuetify from 'vuetify';
import VueLodash from 'vue-lodash';
import store from './store';
import router from './router';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

import App from './components/app.vue';

import 'normalize-css';

Vue.use(VueResource);
Vue.use(BootstrapVue);
Vue.use(Vuetify, {
  iconfont: 'mdi'
});
Vue.use(VueLodash);

const app = new Vue({
  el: '#app',
  store,
  router,
  components: {
    App
  },
  render(h) {
    return <v-app><App></App></v-app>;
  }
});

Vue.config.devtools = true;
