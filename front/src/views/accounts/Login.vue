<template>
  <div class="login">
    <div class='login-input'>
        <div class="voda-logo">
            <!-- <img alt="withus logo" src="@/assets/handwhite.png" width="250" height="230"> -->
            <h1 class='voda-logo'>LOGIN</h1>
        </div>
        <div class="id-input login-div">
          <label for="username">ID </label>
          <input type="text" v-model="loginData.username" id="username">
        </div>
        <div class="password-input login-div">
          <label for="password">PASSWORD  </label>
          <input id="password" v-model="loginData.password" type="password">
        </div>
        <div class="login-button">
            <!-- <a href="/meeting"><button @click="login">로그인하기</button></a>  -->
            <button @click="login">LOGIN</button> 
        </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'Login',
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      },
      isLoggedIn: false,
    }
  },
  methods: {
    // login() {
    //   this.$emit('submit-login-data', this.loginData)
    // }
  setCookies(token) {
    this.$cookies.set('auth-token', token)
    this.isLoggedIn = true
  },
  login() {
    console.log('login!', this.loginData)
    axios.post(SERVER_URL + '/rest-auth/login/', this.loginData)
      .then(res => {
        this.setCookies(res.data.key)
        //res.data // {key : 'aasererasdfa'}
        //처리하고 다른 경로로 이동
        this.$router.push('/voda/meeting')
        this.$emit('submit-login-data', this.loginData)

      })
      .catch(err => console.log(err.response.data))
    },
  },
  mounted() {
    //cookie에 auth-token이 존재하는지 체크
    //mounted는 index.html에서 <div id="app"></div>에 접근하고 바로인 시점
    //새로 고침 하지 않는 시점

    // this.isLoggedIn = this.$cookies.isKey('auth-token') //? true : false
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
.login {
  background-image: linear-gradient(to left bottom, #a4ccff, #adc9ff, #b7c7ff, #c3c3ff, #cec0ff, #d2c0ff, #d7bfff, #dbbfff, #d9c2ff, #d7c4ff, #d5c7ff, #d3c9ff);
  width: 100vw;
  height: 100vh;
  position: fixed;
  margin: 0;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  font-family: 'Viga', sans-serif;
  color: rgb(255, 255, 255);
  font-size: 20px;
}
.login-input {
  width: 300px;
  position:absolute;
  top:47%; left:50%;
  transform: translate(-50%, -50%);
}

.login-div {
  display: inline-block;
  width: 100%;
  margin-bottom: 20px;
} 
.login-div label {
  display: block;
}
.login-div input {
  width: 250px;
  height: 20px;
  border-radius: 5px;
  border: 2px solid rgba(255, 255, 255, 0.932);
  background: rgba(240, 255, 240, 0.185);
  font-family: 'Viga', sans-serif;
  padding: 10px 20px;
  color: rgba(162, 49, 255, 0.863);
  font-size: 15px;
}
.login-div input:hover {
  border: 2px solid rgba(145, 108, 245, 0.616);
}
.login-div input:focus {
  /* input 클릭했을 때 검정 테두리 없애줌 */
  outline: none !important;
  border: 2px solid rgba(145, 108, 245, 0.616);
  box-shadow: 0 0 20px rgba(145, 108, 245, 0.616);
}

.login-button button {
  justify-content: center;
  width: 295px;
  border-radius: 5px;
  height: 40px;
  transition: all ease 0.5s;
  border: 1px solid rgba(255, 255, 255, 0.932);
  background-color: rgba(255, 254, 255, 0.082);
  font-family: 'Viga', sans-serif;
  color: white;
  font-size: 20px;
}
.login-button button:hover {
  cursor: pointer;
  transform: scale( 1.1 );

  background-color: #b86ffc49;
}
.login-button button:focus {
  outline: none !important;
  border: 0;
  border: 2px solid rgba(203, 134, 235, 0.63);
  box-shadow: 0 0 20px rgba(243, 175, 252, 0.747);
}

.voda-logo {
  width: 100%;
  font-size: 180%;
  text-align: center;
  font-family: 'Cairo', sans-serif;
  opacity: 0.9;
  text-shadow: 2px 3px 0px #f1f1f1;
  color: rgb(210, 170, 255);
  /* font: inherit; */
}

.voda-logo img {
  display: block;
  margin: 0 auto;
}


</style>