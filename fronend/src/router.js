import Vue from 'vue';
import VueRouter from 'vue-router';

import Index from './components/index.vue';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Index
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    // Forces page always to scroll up
    return { x: 0, y: 0 };
  }
});
