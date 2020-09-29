import Vue from "vue";
import VueRouter from "vue-router";
import MainChoose from "../views/MainChoose.vue";
import Login from "../views/accounts/Login.vue";
import Signup from "../views/accounts/Signup.vue";
import Customer from "../views/Customer.vue";
import MeetingMain from "../views/MeetingMain.vue";
import MeetingStart from "../views/MeetingStart.vue";
import MeetingRoom from "../views/MeetingRoom.vue";
import Mypage from "../views/Mypage.vue";
import Setting from "../views/Setting.vue";

Vue.use(VueRouter);
export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "MainChoose",
      component: MainChoose,
    },
    {
      path: "/voda",
      name: "MainChoose",
      component: MainChoose,
    },
    {
      path: "/voda/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/voda/signup",
      name: "Signup",
      component: Signup,
    },
    {
      path: "/voda/customer",
      name: "Customer",
      component: Customer,
    },
    {
      path: "/voda/meeting",
      name: "MeetingMain",
      component: MeetingMain,
    },
    {
      path: "/voda/mypage",
      name: "Mypage",
      component: Mypage,
    },
    {
      path: "/voda/meeting/start",
      name: "MeetingStart",
      component: MeetingStart,
    },
    {
      path: "/voda/meeting/setting",
      name: "Setting",
      component: Setting,
    },
    {
      path: "/voda/meeting/room",
      name: "MeetingRoom",
      component: MeetingRoom,
    },
  ],
});

// const router = new VueRouter({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   routes
// })

// export default router
