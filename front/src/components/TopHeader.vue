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
        <p>{{ memberInfo.username }}님 환영합니다.</p>
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
      <li>
        <router-link to="/voda/customer/">Customer</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Header",
  props: {
    isLoggedIn: Boolean,
  },
  data() {
    return {
      memberInfo: {
        id: "",
        email: "",
        username: "",
      },
    };
  },
  methods: {
    logout() {
      this.$emit("submit-logout");
    },
    info() {
      const config = {
        headers: {
          Authorization: `Bearer ${this.$cookies.get("token")}`,
        },
      };
      axios
        .post(
          process.env.VUE_APP_DJANGO_API_SERVER_URL + "api/users/info/",
          null,
          config
        )
        .then((res) => {
          this.memberInfo = res.data;
        })
        .catch(() => {
          // console.log(err);
        });
    },
  },
  mounted() {
    this.info();
  },
};
</script>


<style scoped>
a, p {
  text-decoration: none;
  font-family: "Viga", sans-serif;
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
  display: flex;
  padding: 10px 12px;
  justify-content: center;
  align-items:center;
}
.header-ul li a {
  display: flex;
  align-items:center;
}
</style>
