/*!
 *
 * WebRTC Lab
 * @author dodortus (codejs.co.kr / dodortus@gmail.com)
 *
 */
$(function () {
  if (typeof webkitSpeechRecognition !== "function") {
    alert("크롬에서만 동작 합니다.");
    return false;
  }

  const FIRST_CHAR = /\S/;
  const TWO_LINE = /\n\n/g;
  const ONE_LINE = /\n/g;

  const recognition = new webkitSpeechRecognition();
  const language = "ko-KR";
  const $audio = document.querySelector("#audio");
  const $btnMic = document.querySelector("#btn-mic");
  const $resultWrap = document.querySelector("#result");
  const $iconMusic = document.querySelector("#icon-music");

  let isRecognizing = false;
  let ignoreEndProcess = false;
  let finalTranscript = "";

  recognition.continuous = true;
  recognition.interimResults = true;

  /**
   * 음성 인식 시작 처리
   */
  recognition.onstart = function () {
    console.log("onstart", arguments);
    isRecognizing = true;
    $btnMic.className = "on";
  };

  /**
   * 음성 인식 종료 처리
   */
  recognition.onend = function () {
    console.log("onend", arguments);
    isRecognizing = false;

    if (ignoreEndProcess) {
      return false;
    }

    // DO end process
    $btnMic.className = "off";
    if (!finalTranscript) {
      console.log("empty finalTranscript");
      return false;
    }
  };

  /**
   * 음성 인식 결과 처리
   */
  recognition.onresult = function (event) {
    console.log("onresult", event);

    let interimTranscript = "";
    if (typeof event.results === "undefined") {
      recognition.onend = null;
      recognition.stop();
      return;
    }

    for (let i = event.resultIndex; i < event.results.length; ++i) {
      const transcript = event.results[i][0].transcript;

      //말이 입력이 완료되면
      if (event.results[i].isFinal) {
        finalTranscript += transcript;
        console.log(transcript);
        var xhr = new XMLHttpRequest();

        xhr.open("POST", encodeURI("http://localhost:8000/api/stt/"), true);
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () {
          if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(xhr.responseText);
          }
        };
        //json으로 변경
        data = new Object();
        data.text = transcript;
        // console.log(JSON.stringify(data));
        xhr.send(JSON.stringify(data));
      } else {
        interimTranscript += transcript;
      }
    }

    // finalTranscript = capitalize(finalTranscript);
    // final_span.innerHTML = linebreak(finalTranscript);
    // interim_span.innerHTML = linebreak(interimTranscript);

    // console.log("finalTranscript", finalTranscript);
    // console.log("interimTranscript", interimTranscript);
  };

  /**
   * 음성 인식 에러 처리
   */
  recognition.onerror = function (event) {
    console.log("onerror", event);

    if (event.error.match(/no-speech|audio-capture|not-allowed/)) {
      ignoreEndProcess = true;
    }

    $btnMic.className = "off";
  };

  /**
   * 음성 인식 트리거
   */
  function start() {
    if (isRecognizing) {
      recognition.stop();
      return;
    }
    recognition.lang = language;
    recognition.start();
    ignoreEndProcess = false;

    finalTranscript = "";
    final_span.innerHTML = "";
    interim_span.innerHTML = "";
  }
  /**
   * 초기 바인딩
   */
  // function initialize() {
  //   // const $btnTTS = document.querySelector("#btn-tts");
  //   // const defaultMsg = "전 음성 인식된 글자를 읽습니다.";

  //   // $btnTTS.addEventListener("click", () => {
  //   //   const text = final_span.innerText || defaultMsg;
  //   //   textToSpeech(text);
  //   // });

  //   // $btnMic.addEventListener("click", start);
  //   start();
  // }

  // initialize();
});
