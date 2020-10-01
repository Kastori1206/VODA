<template>
  <div class="header">
    <a href="/">
      <div calss="home-url">
        <img
          src="@/assets/side_logo.png"
          alt="voda 로고"
          width="150"
          height="70"
        />
      </div>
    </a>
    <ul class="header-ul" v-if="isLoggedIn">
      <li>
        <router-link to="/voda/mypage/"
          >{{ username }}님 환영합니다.</router-link
        >
      </li>
      <li @click="logout">
        <router-link to="/voda">Logout</router-link>
      </li>
    </ul>
    <ul class="header-ul" v-if="!isLoggedIn">
      <li>
        <router-link to="/voda/login/">Login</router-link>
      </li>
      <li>
        <router-link to="/voda/signup/">Signup</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Header",
  props: {
    isLoggedIn: Boolean,
  },
  data() {
    return {
      memberInfo: {
        mid: null,
        email: null,
        username: null,
      },
    };
  },
  methods: {
    logout() {
      this.$emit("submit-logout");
    },
  },
};
</script>


<style scoped>
a {
  text-decoration: none;
  color: white;
}
.header {
  font-family: "Viga", sans-serif;
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
