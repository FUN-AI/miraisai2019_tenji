// メニュー
var menu = null;

/*
// ボタン
document.getElementById("AI_select_1").onclick = function () {
    get_text = document.getElementById("AI_select_1").innerHTML;
    speech_send();
}
document.getElementById("AI_select_2").onclick = function () {
    get_text = document.getElementById("AI_select_2").innerHTML;
    speech_send();
}
document.getElementById("AI_select_3").onclick = function () {
    get_text = document.getElementById("AI_select_3").innerHTML;
    speech_send();
}
*/

// 音声認識の設定
SpeechRecognition = webkitSpeechRecognition || SpeechRecognition;
const recognition = new SpeechRecognition();
recognition.lang = 'ja-JP';
recognition.continuous = true;
var get_text = null;
var face_check = 0;
var start_flag = false;

// 音声認識終わったときの処理
recognition.onresult = (event) => {
	console.log(event.results[0][0].transcript);
	get_text = event.results[0][0].transcript
	// 一々切ってる
	recognition.stop();
	speech_send();
}

// 音声認識のスタート
function listenStart() {
	if (!(start_flag)) {
		recognition.start();
	}
}

recognition.onaudiostart = function () {
	start_flag = true;
}

// 音声合成
function AISpeak(speechText) {
	// 発言作成
	const uttr = new SpeechSynthesisUtterance(speechText)
	// 発言キューに発言を追加
	speechSynthesis.speak(uttr)
	uttr.onend = function () {
		start_flag = false;
	}
}

// 音声をサーバーに送る
function speech_send() {
    if (get_text != null) {
        updateText(get_text);
        const formdata = new FormData();
        formdata.append('text', get_text)

        $.ajax({
            url: 'http://localhost:8080/menu',
            type: 'POST',
            dataType: 'json',
            data: formdata,
            processData: false,
            contentType: false,

            success: function (data) {
                AISpeak(data['say']);
                updateText(data['say']);
                menu = data['menus'];
                console.log(menu);
                if (menu[1] == "しゅうりょう") {
                    get_text == "しゅうりょう"
                    speech_send()
                }
                updateSelect(menu[0], menu[1], menu[2]);
            }
        });
        get_text = null;
    }
}

// -------画像------
// 1秒ごとに画像をサーバーに送信する
setInterval('img_send()', 5000);
// 一次的ビデオ置き場
var video = document.createElement('video');

// ビデオ取得設定
navigator.mediaDevices.getUserMedia({ video: true, audio: false })
	.then(function (stream) {
		video.srcObject = stream;
		video.play();
	});

// ビデオから画像を作成
function makePicture() {
	var canvas = document.createElement('canvas');
	var ctx = canvas.getContext('2d')
	canvas.width = video.videoWidth;
	canvas.height = video.videoHeight;
	ctx.drawImage(video, 0, 0, Math.floor((canvas.height - video.width) / 2), Math.floor((canvas.height - video.width) / 2));
	//ctx.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
	var dataURL = canvas.toDataURL('image/jpeg');
	return dataURL;
}

function img_send() {
	if (video != null) {
		const picture = makePicture();
		var formData = new FormData();
		formData.append('img', picture);

		$.ajax({
			url: 'http://localhost:8080/image',
			type: 'POST',
			data: formData,
			contentType: false,
			processData: false,

			success: function (data) {
				// 顔のチェック
				face_check = data['status'];
				if (face_check == 1) {
					listenStart();
				}
			}
		});

	}
}