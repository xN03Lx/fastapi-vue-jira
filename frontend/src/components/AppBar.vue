<template>
      <v-app-bar
      app
      color="light-blue darken-3"
      dark
      :clipped-left="$vuetify.breakpoint.mdAndUp"
      fixed
    >
      <v-container fluid fill-height>
        <v-avatar
          class="mr-10"
          color="grey darken-1"
          size="42"
        >
          <img src="https://img2.freepng.es/20180526/zpz/kisspng-jira-technology-roadmap-computer-software-workflow-5b0a203ad1eb74.2707047115273902668598.jpg">
        </v-avatar>
        <h2 @click="redirectProject" class="title">JIRA Projects</h2>

        <v-spacer></v-spacer>

        <v-responsive max-width="260">
          <v-text-field
            dense
            flat
            hide-details
            rounded
            solo-inverted
          ></v-text-field>
        </v-responsive>
      </v-container>
    </v-app-bar>
</template>

<script>
export default {
  methods: {
    redirectProject(){
      if(this.$route.name !== '/') {
        this.$router.push("/").catch(()=>{})
      }
    }
  }
}
</script>

<style scoped>
  .title {
    cursor: pointer;
  }
</style>
