<template>
  <div class="header">
    <a href="/">
      <div calss="home-url">
        <img src="@/assets/side_logo.png" alt="voda 로고" width="150" height="70">
      </div>
    </a>
    <ul class='header-ul' v-if="isLoggedIn">
      <li>
        <router-link to="/voda/mypage/" v-if="isLoggedIn">{{username}}님 환영합니다.</router-link>
      </li>
      <li>
        <router-link to="/accounts/logout/" @click.native="logout" v-if="isLoggedIn">Logout</router-link>
      </li>
    </ul>
    <ul class='header-ul' v-if="!isLoggedIn">
      <li>
        <router-link to="/voda/login/" >Login</router-link>
      </li>
      <li>
        <router-link to="/voda/signup/">Signup</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'


export default {
  name: 'Header',
  data() {
    return {
      isLoggedIn: false,
    }
  },
  methods: {

    logout() {
      const requestHeaders = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      //axios.post(URL, BODY, HEADER) => 순서
      axios.post(SERVER_URL + '/rest-auth/logout/', null, requestHeaders)
      .then(() => {
        //cookie에 있는 token Header에 가져와서 담고 지우기
        console.log('hello', requestHeaders)
        this.$cookies.remove('auth-token')
        this.isLoggedIn = false
        this.$router.push('/')
        
      })
      .catch(err => console.log(err.response.data))
    }
  },
  mounted() {
    this.$nextTick(function() {
      if (this.$cookies.isKey('auth-token')) {
        this.isLoggedIn = true
      } else {
        this.isLoggedIn = false
      }
    }) 
  }
}
</script>


<style scoped>
a {
  text-decoration: none;
  color: white;
}
.header {
  font-family: 'Viga', sans-serif;
  position: fixed;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100vw;
  height: 70px;
  /* top: 0; */
  /* left: 0;  */
  z-index: 2;
  padding: 10px 50px;  
}
.header-ul {
  display: flex;
  margin-right: 130px;
  padding: 0;
  list-style: none;

}
.header-ul li {
  padding: 10px 12px;
}

</style>
