// static/js/reserve/stepUI.js 
// DOM操作（ステップバー・表示切替）
const STEPS = ['step-1', 'step-2', 'step-3'];

export function goTo(stepIndex) {
  STEPS.forEach((id, i) => {
    document.getElementById(id).classList.toggle('hidden', i !== stepIndex);
  });
  updateStepBar(stepIndex);
}

function updateStepBar(activeIndex) {
  STEPS.forEach((_, i) => {
    const el = document.getElementById(`step-circle-${i + 1}`);
    const isActive = i <= activeIndex;
    el.classList.toggle('bg-pink-500', isActive);
    el.classList.toggle('text-white', isActive);
    el.classList.toggle('bg-gray-200', !isActive);
    el.classList.toggle('text-gray-500', !isActive);
  });
}