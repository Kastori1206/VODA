<template>
  <div class="mainchoose">
    <div class="three-choose">
      <div class="voda-logo">
        <!-- <img alt="voda logo" src="../assets/logo_transparent.png" width="400" height="400"> -->
      </div>
      <div class="choose-button">
        <div v-if="!islogin">
          <a href="/voda/login"><button>로그인</button></a>
        </div>
        <div>
          <a href="/voda/signup"><button>회원가입</button></a>
        </div>
        <div>
          <a href="/voda/customer"><button>손님으로 사용</button></a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'MainChoose',
  props: {
    isLoggedin: Boolean,
  },
  data() {
    return {
      
      islogin: this.isLoggedin,
    }
  },
  

}
</script>

<style scoped>
.mainchoose {
  background-image: linear-gradient(to right bottom, #d4a3ff, #d098ff, #cc8cff, #c980ff, #c574ff, #ca74ff, #ce75fe, #d375fe, #df83fe, #ea92fe, #f3a1fe, #fbb0ff);
  width: 100vw;
  height: 100vh;
}
.voda-logo {
  width: 100%;
  padding-top: 70px;

}
.voda-logo img {
  margin: 0 auto;
}
.three-choose {
  margin: 0 auto;
  width: 300px;
  position:absolute;
  top:47%; left:50%;
  transform: translate(-50%, -50%);
}
button {
  width: 100%;
  margin-bottom: 20px;  
  padding: 10px;
  border-radius: 5px;
  /* height: 40px; */
  transition: all ease 0.5s;
  border: 1px solid rgba(255, 255, 255, 0.932);
  background-color: rgba(255, 254, 255, 0.082);
  font-family: 'Viga', sans-serif;
  color: white;
  font-size: 20px;
}
button:hover {
  cursor: pointer;
  transform: scale( 1.1 );

  background-color: #b86ffc49;
}
button:focus {
  outline: none !important;
  border: 0;
  border: 2px solid rgba(255, 200, 255, 0.616);
  box-shadow: 0 0 20px rgba(255, 200, 255, 0.616);
}
</style>