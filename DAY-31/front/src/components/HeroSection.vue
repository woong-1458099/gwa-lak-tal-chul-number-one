<template>
  <div class="relative">
    <!-- Hero Image Banner -->
    <div class="relative h-64 sm:h-80 lg:h-96 overflow-hidden">
      <ImageWithFallback
        src="https://images.unsplash.com/photo-1517154421773-0529f29ea451?w=1600&q=80"
        alt="Korea Travel"
        class="w-full h-full object-cover"
      />
      <div class="absolute inset-0 bg-gradient-to-b from-black/20 via-black/10 to-white"></div>
    </div>

    <!-- Main Content -->
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 -mt-32 relative z-10">
      <div class="text-center mb-8">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-blue-50 rounded-full mb-6">
          <Sparkles class="w-4 h-4 text-blue-500" />
          <span class="text-blue-700">AI 기반 맞춤 여행 추천</span>
        </div>

        <h1 class="text-gray-900 mb-4">어떤 여행을 도와드릴까요?</h1>
      </div>

      <!-- Search Input Area -->
      <div class="bg-white rounded-2xl shadow-xl border border-gray-100 p-4 mb-6">
        <div class="flex items-center gap-3">
          <Search class="w-5 h-5 text-gray-400 flex-shrink-0" />
          <input
            v-model="inputValue"
            type="text"
            placeholder="예: 부산에서 2박 3일 가족 여행 계획 짜줘"
            class="flex-1 outline-none text-gray-900 placeholder:text-gray-400"
          />
          <button class="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-lg transition-colors flex-shrink-0" type="button">
            검색
          </button>
        </div>
      </div>

      <!-- Quick Suggestions -->
      <div class="mb-16">
        <p class="text-gray-600 text-center mb-4">빠른 추천</p>
        <div class="flex flex-wrap justify-center gap-3">
          <button
            v-for="s in quickSuggestions"
            :key="s.id"
            type="button"
            @click="inputValue = s.text"
            class="flex items-center gap-2 px-5 py-3 bg-white hover:bg-blue-50 border border-gray-200 hover:border-blue-300 rounded-full transition-all shadow-sm hover:shadow-md"
          >
            <span>{{ s.icon }}</span>
            <span class="text-gray-700">{{ s.text }}</span>
          </button>
        </div>
      </div>

      <!-- Features Section -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pb-16">
        <div class="text-center p-6 rounded-xl bg-gradient-to-br from-blue-50 to-white">
          <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <span class="text-2xl">🗺️</span>
          </div>
          <h3 class="text-gray-900 mb-2">맞춤 일정</h3>
          <p class="text-gray-600">AI가 분석한 최적의 여행 코스</p>
        </div>

        <div class="text-center p-6 rounded-xl bg-gradient-to-br from-blue-50 to-white">
          <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <span class="text-2xl">⭐</span>
          </div>
          <h3 class="text-gray-900 mb-2">실시간 정보</h3>
          <p class="text-gray-600">최신 명소와 숨은 맛집 추천</p>
        </div>

        <div class="text-center p-6 rounded-xl bg-gradient-to-br from-blue-50 to-white">
          <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <span class="text-2xl">💡</span>
          </div>
          <h3 class="text-gray-900 mb-2">스마트 추천</h3>
          <p class="text-gray-600">취향과 예산에 맞는 여행지</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Search, Sparkles } from 'lucide-vue-next'
import ImageWithFallback from './figma/ImageWithFallback.vue'

const inputValue = ref('')

const quickSuggestions = [
  { id: 1, text: '호캉스 추천', icon: '🏨' },
  { id: 2, text: '효도 여행', icon: '👨‍👩‍👧' },
  { id: 3, text: '맛집 여행', icon: '🍽️' },
] as const
</script>
