<template>
  <v-card
    class="mx-auto ma-4"
    max-width="344"
    @click="issues"
  >
    <v-card-text>
      <div class="text-h5 mb-0 text--primary">
        <span v-text="project.name"></span>
      </div>
      <div class="text--primary">Type: <span v-text="project.projectTypeKey"></span></div>
      <div class="text--primary">
        Key: <span v-text="project.key"></span>
      </div>
    </v-card-text>
    <v-card-actions>
      <v-list-item class="grow">
        <v-list-item-avatar color="grey darken-3">
          <v-img
            class="elevation-6"
            alt=""
            :src="project.lead.avatarUrls"
          ></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-text="project.lead.displayName"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-card-actions>
  </v-card>

</template>

<script>
export default {
  props: ["project"],
  methods: {
    issues(){
      this.$router.push({path: `project/${this.project.id}/issues`})
    }
  }
}
</script>
