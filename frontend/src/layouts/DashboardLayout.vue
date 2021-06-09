<template>
  <v-app id="inspire">
    <app-bar></app-bar>
    <v-main class="grey lighten-3">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import AppBar from '../components/AppBar.vue'
  export default {
    name: 'DashboardDefault',
    components: {
      AppBar,
    },
  }
</script>

<style lang="sass" scoped>
.page_wrapper
  min-height: calc(100vh - 112px - 48px)
  padding-top: 15px
  .container
    max-width: 1200px
</style>
