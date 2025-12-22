<template>
  <div class="w-96 bg-white border-l border-gray-200 shadow-xl overflow-y-auto flex-shrink-0 animate-slide-in">
    <!-- Header -->
    <div class="relative">
      <button
        type="button"
        @click="$emit('close')"
        class="absolute top-3 right-3 z-10 w-8 h-8 bg-white rounded-full flex items-center justify-center shadow-lg hover:bg-gray-100 transition-colors"
      >
        <X class="w-5 h-5 text-gray-700" />
      </button>

      <!-- Place Image -->
      <div class="h-48 overflow-hidden">
        <ImageWithFallback :src="place.image" :alt="place.name" class="w-full h-full object-cover" />
      </div>
    </div>

    <!-- Content -->
    <div class="p-6">
      <!-- Category Badge -->
      <div class="inline-flex items-center gap-1 px-3 py-1 bg-blue-50 text-blue-700 rounded-full mb-3">
        <span>{{ markerEmoji(place.category) }}</span>
        <span>{{ place.category }}</span>
      </div>

      <!-- Place Name -->
      <h2 class="text-gray-900 mb-2">{{ place.name }}</h2>

      <!-- Rating -->
      <div class="flex items-center gap-4 mb-4">
        <div class="flex items-center gap-1">
          <Star class="w-5 h-5 fill-yellow-400 text-yellow-400" />
          <span class="text-gray-900">{{ place.rating }}</span>
          <span class="text-gray-500">({{ reviewsText }})</span>
        </div>
        <div class="flex items-center gap-1 text-gray-600">
          <MapPin class="w-4 h-4" />
          <span>{{ place.distance }}km</span>
        </div>
      </div>

      <!-- Description -->
      <p class="text-gray-600 mb-6">{{ place.description }}</p>

      <!-- Action Buttons -->
      <div class="grid grid-cols-3 gap-3 mb-4">
        <button
          type="button"
          @click="isFavorite = !isFavorite"
          :class="[
            'flex flex-col items-center gap-1 py-3 rounded-lg border transition-all',
            isFavorite ? 'bg-red-50 border-red-500 text-red-600' : 'bg-white border-gray-200 text-gray-700 hover:bg-gray-50'
          ]"
        >
          <Heart class="w-5 h-5" :class="isFavorite ? 'fill-red-600' : ''" />
          <span>찜</span>
        </button>

        <button type="button" class="flex flex-col items-center gap-1 py-3 rounded-lg border border-gray-200 text-gray-700 hover:bg-gray-50 transition-colors">
          <Share2 class="w-5 h-5" />
          <span>공유</span>
        </button>

        <button type="button" class="flex flex-col items-center gap-1 py-3 rounded-lg border border-gray-200 text-gray-700 hover:bg-gray-50 transition-colors">
          <NavIcon class="w-5 h-5" />
          <span>길찾기</span>
        </button>
      </div>

      <!-- Primary CTA -->
      <button type="button" class="w-full bg-blue-500 hover:bg-blue-600 text-white py-3 rounded-lg transition-colors">
        상세 정보 보기
      </button>

      <!-- Additional Info -->
      <div class="mt-6 pt-6 border-t border-gray-200">
        <h3 class="text-gray-900 mb-3">상세 정보</h3>
        <div class="space-y-2 text-gray-600">
          <p>📍 주소: 서울특별시 중구</p>
          <p>🕒 운영시간: 09:00 - 22:00</p>
          <p>📞 연락처: 02-1234-5678</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { X, Star, MapPin, Heart, Share2, Navigation as NavIcon } from 'lucide-vue-next'
import ImageWithFallback from './figma/ImageWithFallback.vue'
import type { Place, PlaceCategory } from './MapView.vue'

const props = defineProps<{
  place: Place
}>()

defineEmits<{
  (e: 'close'): void
}>()

const isFavorite = ref(false)

const reviewsText = computed(() => props.place.reviews.toLocaleString())

function markerEmoji(category: PlaceCategory) {
  if (category === '맛집') return '🍽️'
  if (category === '카페') return '☕'
  if (category === '관광지') return '🏛️'
  return '🏨'
}
</script>
