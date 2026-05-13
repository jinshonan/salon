// static/js/reserve/main.js
// エントリポイント・ステップ管理

import { goTo } from './stepUI.js';

// ── ステップ遷移 ──────────────────────────────────────────────

function goStep2() {
  if (!validateStep1()) return;
  goTo(1);
}

function goStep3() {
  if (!validateStep2()) return;
  goTo(2);
}

function backStep1() {
  goTo(0);
}

function backStep2() {
  goTo(1);
}

// ── バリデーション ────────────────────────────────────────────

function validateStep1() {
  const selected = document.querySelector('input[name="menu_id"]:checked');
  if (!selected) {
    alert('メニューを選択してください');
    return false;
  }
  return true;
}

function validateStep2() {
  const selected = document.querySelector('input[name="staff_id"]:checked');
  if (!selected) {
    alert('スタッフを選択してください');
    return false;
  }
  return true;
}

// ── イベント登録 ──────────────────────────────────────────────
// HTMLのonclick属性を使わず、ここで一元管理する

document.addEventListener('DOMContentLoaded', () => {

  document.getElementById('btn-go-step2').addEventListener('click', goStep2);
  document.getElementById('btn-go-step3').addEventListener('click', goStep3);
  document.getElementById('btn-back-step1').addEventListener('click', backStep1);
  document.getElementById('btn-back-step2').addEventListener('click', backStep2);

  // 初期表示はステップ1
  goTo(0);
});