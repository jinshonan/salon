<script setup>
import { useRoute } from 'vue-router'
import { reactive, ref, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import personsData from '@/persons.json'
import axios from 'axios'

const route = useRoute()
const toast = useToast()

const state = reactive({
  person: null,
  form: {
    course: '',
    time: '',
    name: '',
    phone: ''
  },
  priceMap: {
    カット: 4000,
    カラー: 6000
  },
  isConfirmed: false
})

const totalPrice = ref(0)

onMounted(() => {
  const person = personsData.persons.find(p => p.id === route.params.id)
  if (person) {
    state.person = person
  } else {
    toast.error('スタイリストが見つかりませんでした')
  }
})

function calculateTotal() {
  totalPrice.value = state.priceMap[state.form.course] || 0
}

async function confirmBooking() {
  const { course, time, name, phone } = state.form

  if (!course || !name || !time || !phone) {
    toast.warning('すべての項目を入力してください')
    return
  }

  calculateTotal()
  state.isConfirmed = true

  const newBooking = {
    stylistId: state.person.id,
    customerName: name,
    phoneNumber: phone,
    course,
    time: time,
    price: totalPrice.value
  }

  try {
    const response = await axios.post('http://localhost:8888/bookings', newBooking)
    toast.success('予約が正常に保存されました！')
  } catch (err) {
    console.error(err)
    toast.error('予約の保存に失敗しました')
  }
}
</script>

<template>
  <section v-if="state.person" class="max-w-xl mx-auto mt-10 p-6 bg-white rounded-lg shadow">
    <h1 class="text-2xl font-bold mb-4">{{ state.person.name.kanji }}さんの予約</h1>

    <div class="space-y-4">
      <div>
        <label class="block mb-1 font-medium">コースを選択:</label>
        <select v-model="state.form.course" @change="calculateTotal" class="w-full border px-3 py-2 rounded">
          <option value="" disabled>コースを選んでください</option>
          <option value="カット">カット（¥4000）</option>
          <option value="カラー">カラー（¥6000）</option>
        </select>
      </div>

      <div>
        <label class="block mb-1 font-medium">時間を選択:</label>
        <input v-model="state.form.time" type="datetime-local" class="w-full border px-3 py-2 rounded" />
      </div>

      <div>
        <label class="block mb-1 font-medium">お名前:</label>
        <input v-model="state.form.name" type="text" class="w-full border px-3 py-2 rounded" />
      </div>

      <div>
        <label class="block mb-1 font-medium">電話番号:</label>
        <input v-model="state.form.phone" type="tel" class="w-full border px-3 py-2 rounded" />
      </div>

      <div class="mt-4">
        <button @click="confirmBooking" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          予約の最後確認をする
        </button>
      </div>

      <div v-if="state.isConfirmed" class="mt-6 p-4 border rounded bg-green-50">
        <h2 class="text-lg font-semibold text-green-700 mb-2">予約内容の確認:</h2>
        <ul class="text-gray-700">
          <li>コース: {{ state.form.course }}</li>
          <li>時間: {{ new Date(state.form.time).toLocaleString() }}</li>
          <li>お名前: {{ state.form.name }}</li>
          <li>電話番号: {{ state.form.phone }}</li>
          <li class="mt-2 font-bold">合計金額: ¥{{ totalPrice }}</li>
        </ul>
      </div>
    </div>
  </section>

  <div v-else class="text-center py-10 text-gray-500">
    スタイリストの情報を読み込んでいます...
  </div>
</template>