<template>
  <div class="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-xl transition-all border border-orange-50 group">
    <!-- Image -->
    <div class="relative h-48 overflow-hidden">
      <ImageWithFallback
        :src="place.image"
        :alt="place.name"
        class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
      />

      <!-- Favorite Button -->
      <button
        type="button"
        @click="isFavorite = !isFavorite"
        class="absolute top-3 right-3 w-10 h-10 bg-white/90 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white transition-colors shadow-lg"
      >
        <Heart
          class="w-5 h-5"
          :class="isFavorite ? 'fill-red-500 text-red-500' : 'text-gray-600'"
        />
      </button>

      <!-- Category Badge -->
      <div class="absolute bottom-3 left-3 px-3 py-1 bg-white/90 backdrop-blur-sm rounded-full">
        <span class="text-gray-700">{{ place.category }}</span>
      </div>
    </div>

    <!-- Content -->
    <div class="p-5">
      <h3 class="text-gray-900 mb-2">{{ place.name }}</h3>

      <!-- Rating -->
      <div class="flex items-center gap-1 mb-3">
        <Star class="w-4 h-4 fill-amber-400 text-amber-400" />
        <span class="text-gray-900">{{ place.rating }}</span>
        <span class="text-gray-500">({{ reviewsText }})</span>
      </div>

      <!-- Description -->
      <p class="text-gray-600 mb-4 line-clamp-2">{{ place.description }}</p>

      <!-- Info -->
      <div class="space-y-2 mb-4">
        <div class="flex items-start gap-2 text-gray-600">
          <MapPin class="w-4 h-4 flex-shrink-0 mt-0.5" />
          <span class="line-clamp-1">{{ place.address }}</span>
        </div>
        <div class="flex items-center gap-2 text-gray-600">
          <Clock class="w-4 h-4 flex-shrink-0" />
          <span>예상 소요: {{ place.estimatedTime }}</span>
        </div>
      </div>

      <!-- Action Button -->
      <button
        type="button"
        class="w-full flex items-center justify-center gap-2 py-2 bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white rounded-lg transition-all"
      >
        <span>상세보기</span>
        <ExternalLink class="w-4 h-4" />
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { Star, MapPin, Clock, Heart, ExternalLink } from 'lucide-vue-next'
import ImageWithFallback from './figma/ImageWithFallback.vue'

export type Place = {
  id: number
  name: string
  category: string
  rating: number
  reviews: number
  image: string
  description: string
  address: string
  estimatedTime: string
}

const props = defineProps<{
  place: Place
}>()

const isFavorite = ref(false)
const reviewsText = computed(() => props.place.reviews.toLocaleString())
</script>
