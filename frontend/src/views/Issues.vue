<template>
  <div>
    <v-container v-show="!getProgressIssues">
      <v-row style="justify-content: center;">
        <v-col :cols="12">
          <v-card>
            <v-toolbar
              flat
              color="primary"
              dark
            >
              <v-toolbar-title>
                Project Name: {{getCurrentProject.name}}
              </v-toolbar-title>
            </v-toolbar>
            <v-tabs
              vertical
              v-model="tab"
            >
              <v-tab
                 v-for="status in getIssuesStatus"
                :key="status.key"
                v-text="status.value"
              ></v-tab>
              <v-tabs-items v-model="tab">
                <v-tab-item
                  v-for="status in getIssuesStatus"
                  :key="status.key">
                  <keep-alive>
                    <v-card :loading="getProgressIssueByStatus">
                      <v-card-text
                        :id="'issue-list__' + status.value"
                        class="issue-list"
                        :data-status="status.value"
                      >
                        <v-expansion-panels>
                        <template v-for="issue in status.issues">
                            <issue-expansion-panel
                              :issue="issue"
                              :key="issue.id"/>
                        </template>
                        </v-expansion-panels>
                      </v-card-text>
                    </v-card>
                  </keep-alive>
                </v-tab-item>
              </v-tabs-items>
            </v-tabs>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-container
      v-show="getProgressIssues"
      style="height: 400px;"
    >
      <v-row
        class="fill-height"
        align-content="center"
        justify="center"
      >
        <v-col
          class="text-subtitle-1 text-center"
          cols="12"
        >
          Getting Issues, If it takes a long time, it is because the information is being obtained from Jira.
        </v-col>
        <v-col cols="6">
          <v-progress-linear
            color="deep-purple accent-4"
            indeterminate
            rounded
            height="6"
          ></v-progress-linear>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import IssueExpansionPanel from '@/components/issue/IssueExpansionPanel.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
  props: ['idProject'],
  components: { IssueExpansionPanel },
  computed: {
    ...mapGetters([
      "getIssuesStatus",
      "getCurrentProject",
      "getProgressIssues",
      "getIssuesByStatus",
      "getProgressIssueByStatus",
    ]),
  },
  data: () => ({
      tab: null,
    }),
    methods: {
      ...mapActions([
        "fetchIssues",
        "fetchProjectById"
      ]),
      defaultDescription(desc){
        return desc ? desc : "Without Description"
      }
    },
    created(){
      this.fetchProjectById(this.idProject)
      this.fetchIssues(this.idProject)
    },
}
</script>

<style scoped>
  .issue-list__item{
    border-bottom: 1px solid #eee
  }
  .v-card__text{
    padding: 5px !important;
  }

  .issue-list {
    min-height: 500px;
    padding: 0;
  }
  .assigned{
    padding: 5px;
    font-weight: bold;
  }
</style>

