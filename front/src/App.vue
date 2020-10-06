<template>
  <div id="app">
    <TopHeader
      v-if="$route.name != 'MeetingRoom'"
      :isLoggedIn="isLoggedIn"
      @submit-logout="logout"
    />
    <router-view @submit-login-data="login" :isLoggedIn="isLoggedIn"/>
  </div>
</template>
<script>
import axios from "axios";
import TopHeader from "@/components/TopHeader.vue";

export default {
  name: "app",

  components: {
    TopHeader,
  },
  methods: {
    login(loginData) {
      axios
        .post(
          process.env.VUE_APP_DJANGO_API_SERVER_URL + "api/users/login/",
          loginData
        )
        .then((res) => {
          this.$cookies.set("token", res.data.token); //토큰 날라오는거 설정해줘야함!!
          this.isLoggedIn = true;
          this.$router.push("/voda/meeting");
          alert("로그인 되었습니다.");
        })
        .catch(() => {
          // console.log(err);
          alert(
            "존재하지 않는 계정입니다. 아이디와 비밀번호를 다시 확인해주세요"
          );
        });
    },
    logout() {
      alert("로그아웃 되었습니다.");
      this.$cookies.remove("token");
      this.isLoggedIn = false;
    },
  },
  mounted() {
    this.isLoggedIn = this.$cookies.isKey("token");
  },
  updated() {
    this.isLoggedIn = this.$cookies.isKey("token");
  },
  data() {
    return {
      isLoggedIn: false,
    };
  },
};
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
html {
  scroll-behavior: smooth;
}
</style>
