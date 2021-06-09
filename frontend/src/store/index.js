import Vue from 'vue';
import Vuex from 'vuex';
import ProjectsModule from './modules/project'
import IssuesModule from './modules/issue'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    ProjectsModule,
    IssuesModule
  },
});
