<template>
  <v-expansion-panel>
    <v-expansion-panel-header>
      <v-row
        align="center"
        class="spacer"
        no-gutters
      >
        <v-col
          cols="4"
          sm="2"
          md="1"
        >
          <v-avatar
            size="36px"
          >
            <img
              alt="Avatar"
              :src="issue.reporter.avatarUrls"
            >
          </v-avatar>
        </v-col>

        <v-col
          class="hidden-xs-only"
          sm="4"
          md="2"
        >
          <strong
            v-html="issue.reporter.displayName"
          >
          </strong>
        </v-col>

        <v-col
          class="text-no-wrap"
          cols="4"
          sm="2"
        >
          <v-chip
            :color="`teal lighten-4`"
            class="ml-0 mr-2 black--text"
            label
            small
          >
            {{ issue.issueType }}
          </v-chip>
          <v-chip
            :color="`teal lighten-4`"
            class="ml-0 mr-2 black--text"
            label
            small
          >
            {{ issue.assignes.length }} Assigned
          </v-chip>
        </v-col>
        <v-col>
          <strong
            class="ml-6"
            v-html="issue.summary">
          </strong>
        </v-col>
      </v-row>
    </v-expansion-panel-header>

    <v-expansion-panel-content>
      <v-divider></v-divider>
      <v-card-text
        v-html="getDescription(issue.description)">
      </v-card-text>
      <v-list>
        <span
          class="assigned"
          v-if="issue.assignes.length > 0"
        >assigned:
        </span>
        <v-list-item
          v-for="(item, key) in issue.assignes"
          :key="key"
        >
          <v-list-item-avatar>
            <v-img
              :src="item.avatarUrls"
            >
            </v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title
              v-html="item.displayName"
            >
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
export default {
  props: ["issue"],
  methods: {
    getDescription(desc){
      const defaultValue = "Without Description"
      return desc ? desc : defaultValue
    }
  }
}
</script>

<style scoped>
  .assigned{
    padding: 5px;
    font-weight: bold;
  }
</style>
