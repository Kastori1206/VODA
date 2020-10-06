<template>
  <div class="meeting-main">
    <div class="main-box">
      <div class="header-choose">
        <a href="/mypage">My Page</a>
        <a href="/meeting/setting">Setting</a>
      </div>
      <div class="profile">
        <img
          src="https://www.thestatesman.com/wp-content/uploads/2017/08/1493458748-beauty-face-517.jpg"
          alt=""
          width="150"
          height="150"
        />
      </div>
      <div class="meeting-button">
        <a href="/voda/meeting/start"><button>미팅 참여</button></a>
        <a href="/reservate"><button>예약하기</button></a>
        <a href="/voda/customer"><button>손님으로 입장</button></a>
        <a href="http://localhost:8001?test=test"><button>test</button></a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MeetingMain",
};
</script>

<style scoped>
.profile img {
  border-radius: 50%;
}
.meeting-main {
  background-image: linear-gradient(
    to left bottom,
    #c8f7f4,
    #c4f9f1,
    #c2fbed,
    #c2fde7,
    #c3fee0,
    #c3fee0,
    #c4ffe0,
    #c4ffe0,
    #c3ffe7,
    #c3ffee,
    #c5fff4,
    #c8fff9
  );
  width: 100vw;
  height: 100vh;
  position: fixed;
  margin: 0;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  font-family: "Viga", sans-serif;
  color: rgb(255, 255, 255);
  font-size: 20px;
}
.main-box {
  width: 100vh;
  position: absolute;
  top: 47%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>