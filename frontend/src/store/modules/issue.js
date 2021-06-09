import axios from "axios";

const state = {
  issues: [],
  issuesStatus: [],
  progressIssues: true,
  progressIssuesByStatus: true,

}

const getters = {
  getIssues: (state) => state.issues,
  getIssuesStatus: (state) => state.issuesStatus,
  getProgressIssues: state => state.progressIssues,
  getProgressIssueByStatus: state => state.progressIssuesByStatus,
  getIssuesByStatus: (state) => (status) => {
    if (state.issues.length > 0) {
      return state.issues.find(x => x._id === status).issues
    }
    return state.issues
  },
}

const actions = {
  async fetchStatuses ({ commit }, project_id) {
    try {
      const url = `http://localhost:5000/api/projects/${project_id}/statuses`
      const response = await axios.get(url)
    } catch (error) {
      console.log(error)
    }
  },
  async fetchIssues ({ commit }, project_id) {
    commit("setIssuesToEmpty")
    commit("setProgressIssueByStatus", true)
    commit("setProgressIssues", true)
    try {
      const url = `http://localhost:5000/api/projects/${project_id}/issues`
      const response = await axios.get(url)
      commit("setProgressIssueByStatus", false)
      commit("setProgressIssues", false)
      commit("setIssueStatus", response.data)
    }catch (error) {
      console.log(error)
    }
  }
}

const mutations = {
  setIssues: (status, payload) => {
    let issues ={}
    for (let status of payload) {
      issues[status.key] = status.issues
    }
    status.issues = issues
  },
  setIssuesToEmpty: (status) => {
    status.issuesStatus = []
  },
  setIssueStatus: (status, payload) => {
    status.issuesStatus = payload.map(x => {
      return {
        value: x._id,
        key: x.key,
        issues: x.issues
      }
    })
  },
  setProgressIssues: (state, status) => {
    state.progressIssues = status
  },
  setProgressIssueByStatus: (state, status) => {
    state.progressIssuesByStatus = status
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
