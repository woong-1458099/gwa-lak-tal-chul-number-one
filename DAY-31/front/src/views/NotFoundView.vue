<template>
  <div class="min-h-screen flex items-center justify-center p-6">
    <div class="max-w-md w-full bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
      <h1 class="text-gray-900 mb-2">페이지를 찾을 수 없어요</h1>
      <p class="text-gray-600 mb-6">주소가 잘못되었거나, 이동된 페이지일 수 있어요.</p>
      <RouterLink
        to="/home"
        class="inline-flex items-center justify-center w-full bg-blue-500 hover:bg-blue-600 text-white py-3 rounded-lg transition-colors"
      >
        홈으로 돌아가기
      </RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>
