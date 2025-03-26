<script setup>
 import Card from './Card.vue';
 import { RouterLink } from 'vue-router';
</script>

<template>
    <section class="py-4">
      <div class="container-xl lg:container m-auto">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-4 rounded-lg">
          <Card>
            <h2 class="text-2xl font-bold">スタイリスト</h2>
            <p class="mt-2 mb-4">
              スタッフ一覧
            </p>
            <RouterLink
              to="/jobs"
              class="inline-block bg-black text-white rounded-lg px-4 py-2 hover:bg-gray-700"
            >
              詳細を見る
            </RouterLink>
        </Card>
          <Card bg="bg-blue-100">
            <h2 class="text-2xl font-bold">テスト</h2>
            <p class="mt-2 mb-4">
              フォームです
            </p>
            <RouterLink
              to="/jobs/add"
              class="inline-block bg-blue-500 text-white rounded-lg px-4 py-2 hover:bg-blue-600"
            >
              記入する
            </RouterLink>
          </Card>
        </div>
      </div>
    </section>
</template>