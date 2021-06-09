<template>
  <div>
    <v-container v-show="!progressProjects">
      <v-row>
        <v-col :cols="12">
          <v-card>
            <v-toolbar flat>
              <v-toolbar-title>Projects</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
            <v-divider></v-divider>
            <v-slide-group
              class="pa-4"
              active-class="success"
              show-arrows
            >
              <v-slide-item
                v-for="(project,key) in projectsList"
                :key="key"
              >
                <v-container
                  class="ma-4"
                >
                  <v-row
                    class="fill-height"
                    align="center"
                    justify="center"
                  >
                    <project-card
                      class="card"
                      :project="project"
                    ></project-card>
                  </v-row>
                </v-container>
              </v-slide-item>
            </v-slide-group>
          </v-card>

        </v-col>
      </v-row>
    </v-container>
    <v-container v-show="progressProjects" style="height: 400px;">
      <v-row
        class="fill-height"
        align-content="center"
        justify="center"
      >
        <v-col
          class="text-subtitle-1 text-center"
          cols="12"
        >
          Getting the projects wait... If it takes a long time, the information is being obtained from Jira.

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
import ProjectCard from '@/components/project/ProjectCard.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
  components: {
    ProjectCard
  },
  computed: {
    ...mapGetters([
      "projectsList",
      "progressProjects"
   ]),
  },
  created(){
    this.fetchProjects()
  },
  data(){
    return{
    }
  },
  methods: {
    ...mapActions([
      "fetchProjects"
    ]),
  }
}
</script>

<style scoped>
  .card-group {
    display: -webkit-flex;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
  }
  .card {
    width: 310px;
    margin-bottom: 8px;
    margin-right: 20px;
  }
  .title-project {
    color: rgba(0,0,0,.6);
    font-weight: 500;
    font-style: italic;
    width: 200px;
  }
  .title-container {
    display: flex;
    justify-content: center;
    padding: 10px 20px;
  }
</style>
