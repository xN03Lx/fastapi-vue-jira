import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: () => import('../layouts/DashboardLayout.vue'),
    children: [
      { path: '', component: () => import('../views/Project.vue') },
      {
        path: 'project/:idProject/issues',
        component: () => import('../views/Issues.vue'),
        props: true
      }
    ],
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
