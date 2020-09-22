<template>
  <div class="signup">
      <div class="signup-input">
        <div class="voda-logo">
          <!-- <img alt="voda logo" src="@/assets/logo_transparent.png" width="300" height="300"> -->
          <h1 class="voda-logo">VODA</h1>
        </div>
        <div class="s-id-input signup-div">
          <label for="username">ID </label>
          <input type="text" v-model="signupData.username" id="username">
        </div>
        <div class="s-email-input signup-div">
          <label for="username">EMAIL </label>
          <input type="text" v-model="signupData.email" id="email">
        </div>
        <div class="s-password1-input signup-div">
          <label for="password1">PASSWORD  </label>
          <input id="password1" v-model="signupData.password1" type="password">
        </div>
        <div class="s-password2-input signup-div">
          <label for="password2">Confirm Password</label>
          <input id="password2" v-model="signupData.password2" type="password">
        </div>
        <div class="signup-button">
          <button @click="signup">Sign up</button> 
        </div>
      </div>

  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'


export default {
  name: 'Signup',
  data() {
    return {
      signupData: {
        username: null,
        email: null,
        password1: null,
        password2: null,
      },
      errorMessage: null,
    }
  },
  methods: {
    // signup() {
    //   this.$emit('submit-signup-data', this.loginData)
    // },
    setCookies(token) {
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },
    signup() {
      console.log('signup@:', this.signupData)
      axios.post(SERVER_URL + '/rest-auth/signup/', this.signupData)
        .then(res => {
          this.setCookies(res.data.key)
          //res.data // {key : 'aasererasdfa'}
          //처리하고 다른 경로로 이동
          this.$router.push('/voda/meeting')
        })
        .catch(err => this.errorMessage = err.response.data)
    },
  }
}

</script>

<style scoped>
.signup {
  background-image: linear-gradient(to right bottom, #96afff, #a6b2ff, #b5b6ff, #c2baff, #cebeff, #d1bdff, #d4bdff, #d7bcff, #d2b6ff, #cdb1ff, #c8abff, #c3a6ff);
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
.signup-input {
  width: 300px;
  position:absolute;
  top:47%; left:50%;
  transform: translate(-50%, -50%);
}

.signup-div {
  display: inline-block;
  width: 100%;
  margin-bottom: 15px;
} 
.signup-div label {
  display: block;
}
.signup-div input {
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
.signup-div input:hover {
  border: 2px solid rgba(145, 108, 245, 0.616);
}
.signup-div input:focus {
  /* input 클릭했을 때 검정 테두리 없애줌 */
  outline: none !important;
  border: 2px solid rgba(145, 108, 245, 0.616);
  box-shadow: 0 0 20px rgba(145, 108, 245, 0.616);
}

.signup-button button {
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
.signup-button button:hover {
  cursor: pointer;
  transform: scale( 1.1 );

  background-color: #b86ffc49;
}
.signup-div button:focus {
  outline: none !important;
  border: 0;
  border: 2px solid rgba(255, 200, 255, 0.616);
  box-shadow: 0 0 20px rgba(255, 200, 255, 0.616);
}

/* .withus-logo {
  width: 100%;
}
.withus-logo img {
  display: block;
  margin: 0 auto;
  width: 80%;
  height: 80%;
} */
.voda-logo {
  width: 100%;
  font-size: 180%;
  text-align: center;
  font-family: 'Cairo', sans-serif;
  opacity: 0.9;
  text-shadow: 2px 3px 0px #f7ecff;
  color: rgb(198, 185, 255);
  /* font: inherit; */
}

</style>