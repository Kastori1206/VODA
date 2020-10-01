<template>
  <div id="app">
    <TopHeader v-if="$route.name != 'MeetingRoom'" />
    <router-view @submit-login-data="pushLoginData(loginData)"/>
  </div>
</template>
<script>
// import axios from 'axios'
import TopHeader from '@/components/TopHeader.vue';

// const SERVER_URL = 'http://localhost:8000'

export default {
  name: "app",
  // data() {
  //   return {
  //     sendloginData: null,
  //   }
  // },
  components: {
    TopHeader
  },
  // methods: {
  //   pushLoginData(loginData) {
  //     this.sendloginData = loginData
  //     console.log('App', sendloginData)
  //   }
  // }

}
</script>
<style>
body {
  width: 100vh;
  height: 100vh;
}
::selection {
  color: rgb(203, 37, 253);
  background: rgb(255, 255, 255);
}
</style>
