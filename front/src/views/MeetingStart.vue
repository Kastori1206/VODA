<template>
  <div class="meeting-start">
    <div class="room-title">
      <h3>ooo님의 미팅룸</h3>
    </div>
    <!-- video-box 화면 대신임 -->
    <div class="video-box">
      <div class="video-header">
        <div class='nickname-box'>
          <a href="/voda/customer">nickname</a>
        </div>
      </div>
      <div class="video-center">
        <img src="@/assets/profile.png" alt="" width="200" height="200">
      </div>
      <div class="video-bottom">
        <span class="mike-img">
          <img src="@/assets/mike.png" alt="" width="50" height="50">
        </span>
        <span class="film-img">
          <img src="@/assets/film.png" alt="" width="50" height="50">
        </span>
        <span class="meeting-enter-button">
          <a href="/enter/mettingroom"><button class="meeting-enter-link"><h5>참여하기</h5></button></a>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MeetingStart',
}
</script>

<style>
.video-box {
    background: gray;
    width: 800px;
    height: 500px;
    margin: 50px 100px;

}
.nickname-box {
  width: 100px;
  padding: 10px;
  background: white;
  border-radius: 50px;
}
.video-center {
  padding: 100px;
}
.video-center img{
  border: 5px solid black;
  border-radius: 50%;
}
.mike-img img{
  border-radius: 50%;
  border: 1px solid green;
}
.film-img img{
  border-radius: 50%;
  border: 1px solid red;
}

.meeting-enter-link {
  border-radius: 10px;
}
</style>