<template>
  <div class="meeting-main">
      <div class="header-choose">
        <a href="/mypage">My Page</a>
        <a href="/meeting/setting">Setting</a>
      </div>
      <div class="profile">
        <img src="https://www.thestatesman.com/wp-content/uploads/2017/08/1493458748-beauty-face-517.jpg" alt="" width="150" height="150">
      </div>
      <div class="meeting-button">
        <a href="/meeting/start"><button>미팅 참여</button></a>
        <a href="/reservate"><button>예약하기</button></a>
        <a href="/customer"><button>손님으로 입장</button></a>
      </div>
  </div>
</template>

<script>
export default {
    name: 'MeetingMain',
}
</script>

<style>
.profile img {
    border-radius: 50%;
}
</style>