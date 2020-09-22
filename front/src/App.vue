<template>
  <div id="app">
    <TopHeader />
    <router-view/>
  </div>
</template>
<script>
// import axios from 'axios'
import TopHeader from '@/components/TopHeader.vue';

// const SERVER_URL = 'http://localhost:8000'

export default {
  name: "app",
  components: {
    TopHeader
  },

}
</script>
<style>
body {
  width: 100vh;
  height: 100vh;
}
</style>
