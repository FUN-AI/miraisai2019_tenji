// 表示用のJSのファイル
var logHTML = "";

// 表示テキストを更新する（AI_textWindow）
function updateText(text) {
	addLog(text);
	const AI_textWindow = document.getElementById("AI_textWindow");
	AI_textWindow.innerHTML = logHTML;
}

// 選択肢を更新する（AI_select_1, AI_select_2, AI_select_3）
function updateSelect(s1, s2, s3) {
	const AI_select_1 = document.getElementById("AI_select_1");
	const AI_select_2 = document.getElementById("AI_select_2");
	const AI_select_3 = document.getElementById("AI_select_3");
	AI_select_1.innerHTML = s1;
	AI_select_2.innerHTML = s2;
	AI_select_3.innerHTML = s3;
}


// ロード時にエラーメッセージを削除する
document.addEventListener("DOMContentLoaded", function () {
	updateText("起動中...話しかけて下さい...");
	updateSelect("( ✌︎'ω')✌︎", "( ✌︎'ω')✌︎", "( ✌︎'ω')✌︎");
});

// ログの追加
function addLog(text) {
	// 追加
	logHTML = logHTML + "<br>" + text;

	// 多すぎたら削除（100行くらい残す？）
	// 後で書く

	console.log("---"+logHTML);
}
