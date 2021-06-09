import axios from "axios";


const state = {
  progressProjects: true,
  projects: [],
  currentProject: []
}

const getters = {
  projectsList: state => state.projects,
  getCurrentProject: state => state.currentProject,
  progressProjects: state => state.progressProjects
}

const actions = {
  async fetchProjects ({ commit }) {
    try {
      const response = await axios.get("http://localhost:5000/api/projects/")
      commit("setProjects", response.data)
      commit("setProgressProjects")
    }catch (error) {
      console.log(error);
    }
  },
  async fetchProjectById ({ commit }, projectId) {
    try {
      const response = await axios.get(`http://localhost:5000/api/projects/${projectId}`)
      commit("setCurrentProject", response.data)
    } catch(error) {
      console.log(error)
    }
  }
}

const mutations = {
  setProjects: (state, projects) => {
    state.projects = projects
  },
  setCurrentProject: (state, project) => {
    state.currentProject = project
  },
  setProgressProjects: (state) => {
    state.progressProjects = false
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
