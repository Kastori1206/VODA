<template>
  <div class="all-box">
    <div class="meetingroom" :class="{changeWidth: ismargin}">
      <div class="sidebar" :class="{sidewidth:isOpen}">
        <div class="btn-zip">
          <input type="radio" id="chat-btn" name="button" checked="checked">
          <label for="chat-btn" class="btn-item" @click="setchat">채팅</label>
          <input type="radio" id="parti-btn" name="button">
          <label for="parti-btn" class="btn-item"  @click="setparticipant">참가자</label>
          <input type="radio" id="record-btn" name="button">
          <label for="record-btn" class="btn-item"  @click="setrecord">기록</label>
        </div>
        <div class="chosed-box">
          <div class="chat-box" v-if="this.status === 'chat'">
            <Chat/>
          </div>
          <div class="partici-box" v-if="this.status === 'participants'">
            <Participants/>
          </div>
          <div class="record-box" v-if="this.status === 'record'">
            <Record/>
          </div>
        </div>
        <div class="sign-box">
          <div class="sign-lang-video" >수화영상</div>
        </div>
      </div>
      <div class="videoBox">
        <div class="video">
          <div style="padding-bottom: 56.26%; background-color:red;"></div>
          <div style="padding-bottom: 56.26%; background-color:yellow;"></div>
          <div style="padding-bottom: 56.26%; background-color:orange;"></div>
          <div style="padding-bottom: 56.26%; background-color:purple;"></div>
          <!-- <div style="padding-bottom: 56.26%; background-color:blue;"></div> -->
          <!-- <div style="padding-bottom: 56.26%; background-color:red;"></div> -->
          <!-- <div style="padding-bottom: 56.26%; background-color:yellow;"></div> -->
          <!-- <div style="padding-bottom: 56.26%; background-color:orange;"></div> -->
          <!-- <div style="padding-bottom: 56.26%; background-color:purple;"></div> -->
          <!-- <div style="padding-bottom: 56.26%; background-color:blue;"></div> -->
        </div>
      </div> 
    </div>
    <div class='meeting-bottom'>
      <div class="bottom-btn-box">
        <div class="onoff-camera circle-btn">
          <i class="fas fa-camera fa-2x"></i>
          <p class="arrow_box">카메라 on</p>
        </div>
        <div class="onoff-mike circle-btn">
          <i class="fas fa-microphone fa-2x"></i>
          <p class="arrow_box">마이크 on</p>
        </div>
        <div class="onoff-caption circle-btn">
          <i class="fas fa-closed-captioning fa-2x"></i>
          <p class="arrow_box">자막 on</p>
        </div>
        <div class="onoff-sign circle-btn">
          <i class="fas fa-sign-language fa-2x"></i>
          <p class="arrow_box">수화영상 on</p>
        </div>
        <div class="sidebar-btn circle-btn">
          <i @click="sideOpen" class="far fa-eye fa-2x"></i>
          <p class="arrow_box">수화인식 on</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Chat from '@/components/Chat.vue';
import Participants from '@/components/Participants.vue';
import Record from '@/components/Record.vue';

export default {
    name: 'MeetingRoom',
    data() {
      return {
        isOpen: false,
        ismargin: false,
        status: 'chat',
      }
    },
    components: {
      Chat,
      Participants,
      Record
    },
    methods: {
      sideOpen() {
        this.isOpen = !this.isOpen
        if (this.isOpen === true){
          this.ismargin = true
        }
        else {
          this.ismargin = false
        }
        console.log('isOpen', this.isOpen)
      },
      setchat() {
        this.status = 'chat'
      },
      setparticipant() {
        this.status = 'participants'
      },
      setrecord() {
        this.status = 'record'
      }
    }

}
</script>

<style>
.changeWidth {
  margin-right: 300px;
  width: calc(100vw - 300px)
}
.all-box {
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  position: relative;

}
.meetingroom {
  background: rgba(14, 13, 13, 0.904);
  /* width: 100vw; */
  height: calc(100% - 80px);
  /* position: sticky; */
  z-index:-1;
  /* margin: 0; */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  color: rgb(255, 255, 255);
  font-size: 20px;
  /* overflow: hidden; */
}
.videoBox {
  padding: 50px;
  height: 500px;
  display: grid;
}

.video {
  /* width: 80%; */
  /* height: 80%; */
  /* background: burlywood; */
  display: grid;
  grid-gap: 5px;
  grid-template-columns: repeat(auto-fit, minmax(30%, auto));
  grid-template-rows: repeat(auto-fit, minmax(20%, auto));
  justify-content: center;
  white-space: nowrap;
}
.hello div {
  box-sizing: border-box;
}
.sidebar {
  height: calc(100% - 80px);
  width: 0;
  position:fixed;
  z-index:2;
  top: 0;
  right: 0;
  opacity: 0.9;
  overflow: hidden;
}
/* .container {
  display: grid;
  width: 100%;
  height: 600px;
  background: cadetblue;
  text-align: center;
  align-items: center;
} */
.sidewidth {
  width: 300px;
  background: rgba(84, 84, 238, 0.63);
  height: calc(100vh - 80px);
  z-index:3;
}
.sidemargin {
  width: (100vw - 300px);
}


.btn-zip {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr; 
  text-align: center;
  justify-content: center;
}

.btn-zip > input[type="radio"] {
  opacity:0;
  position: fixed;
  width: 0;
}

.btn-zip label {
  display: inline-block;
  background-color: #ddd;
  padding: 10px;
  font-family: sans-serif, Arial;
  font-size: 16px;
  /* border: 2px solid #444; */
  border-radius: 15px 15px 0 0;
}
.btn-zip input[type="radio"]:checked + label {
  background-color:#bfb;
}
.btn-zip input[type="radio"]:focus + label {
  /* background-color:#bfb; */
  /* border: 2px dashed #444; */
}
.btn-zip label:hover {
  cursor: pointer;
  background-color: #dfd;
}

.btn-item {
  display: flex;
  align-items: center;
  justify-content: center;
}

.chosed-box {
  width: 300px;
  height: 50%;
  background: chartreuse;
}
.meeting-bottom {
  width: 100%;
  height: 80px;
  /* padding:20px; */
  background: blueviolet;
  position: fixed;
  bottom: 0;
  left:0;
  z-index:1;
  overflow: hidden;
  display: flex;
  justify-content: center;
}

.bottom-btn-box {
  width: 50%;
  height: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.circle-btn{
  position: relative;
  /* display: block; */
  align-items: center;
  width: 100%;
  /* height: 100%; */
  margin: 15px;
}
.arrow_box {
  z-index:5;
  text-align: center;
  display: none;
  position: absolute;
  width: 100px;
  padding: 8px;
  top: -80%;
  left:-20%;
  -webkit-border-radius: 8px;
  -moz-border-radius: 8px;  
  border-radius: 8px;
  background: rgba(250, 195, 255, 0.685);
  color: #fff;
  font-size: 14px;
  opacity: 0.8;
}

.arrow_box:after {
  position: absolute;
  top: 100%;
  left: 50%;
  width: 0;
  height: 0;
  margin-left: -10px;
  border: solid transparent;
  border-color: rgba(51, 51, 51, 0);
  border-top-color: rgba(250, 195, 255, 0.685);
  border-width: 10px;
  pointer-events: none;
  content: " ";
}

.circle-btn:hover > p.arrow_box {
  display: block;
}
.circle-btn:hover {
  cursor: pointer;
}

.circle-btn i{
  display: block;
  color:white;
  /* padding: 20px; */
  width: 62px;
  height: 62px;
  border-radius: 50%;
  border: 2px solid rgba(255, 255, 255, 0.562);
  justify-content: center;
  align-items: center;
  display: flex;
  
}

</style>