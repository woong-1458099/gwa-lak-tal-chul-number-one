<template>
  <div class="flex-1 relative bg-gray-100">
    <!-- Mock Map Background -->
    <div class="absolute inset-0">
      <ImageWithFallback
        src="https://images.unsplash.com/photo-1524661135-423995f22d0b?w=1600&q=80"
        alt="Map view"
        class="w-full h-full object-cover opacity-40"
      />
    </div>

    <!-- Map Overlay Grid (to simulate map-like appearance) -->
    <div class="absolute inset-0 bg-gradient-to-br from-blue-50/50 to-white/50">
      <div
        class="w-full h-full"
        :style="{
          backgroundImage: gridBackground,
          backgroundSize: '50px 50px'
        }"
      ></div>
    </div>

    <!-- Map Controls -->
    <div class="absolute top-4 left-4 z-10 bg-white rounded-lg shadow-lg p-3 space-y-2">
      <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded transition-colors" type="button">+</button>
      <div class="h-px bg-gray-200"></div>
      <button class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded transition-colors" type="button">−</button>
    </div>

    <!-- Current Location Button -->
    <div class="absolute top-4 right-4 z-10">
      <button class="bg-white rounded-lg shadow-lg px-4 py-2 flex items-center gap-2 hover:bg-gray-50 transition-colors" type="button">
        <MapPin class="w-4 h-4 text-blue-500" />
        <span class="text-gray-700">현재 위치</span>
      </button>
    </div>

    <!-- Place Markers -->
    <div class="absolute inset-0 z-5">
      <button
        v-for="(place, index) in places"
        :key="place.id"
        type="button"
        class="absolute transform -translate-x-1/2 -translate-y-full transition-all hover:scale-110 group"
        :class="isSelected(place) ? 'z-20' : 'z-10'"
        :style="markerStyle(index)"
        @click="$emit('placeSelect', place)"
      >
        <!-- Marker Pin -->
        <div :class="['relative', isSelected(place) ? 'animate-bounce' : '']">
          <div
            class="w-10 h-10 rounded-full flex items-center justify-center shadow-lg"
            :class="markerBg(place.category)"
          >
            <span class="text-xl">{{ markerEmoji(place.category) }}</span>
          </div>

          <!-- Marker point -->
          <div
            class="absolute left-1/2 transform -translate-x-1/2 w-0 h-0 border-l-8 border-r-8 border-t-8 border-transparent"
            :class="markerPoint(place.category)"
          ></div>
        </div>

        <!-- Mini tooltip on hover (not for selected place) -->
        <div
          v-if="!isSelected(place)"
          class="absolute left-1/2 transform -translate-x-1/2 -top-16 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none"
        >
          <div class="bg-white rounded-lg shadow-lg px-3 py-2 whitespace-nowrap">
            <p class="text-gray-900">{{ place.name }}</p>
            <p class="text-gray-600">⭐ {{ place.rating }}</p>
          </div>
        </div>
      </button>
    </div>

    <!-- Map Legend -->
    <div class="absolute bottom-4 left-4 z-10 bg-white rounded-lg shadow-lg p-4">
      <p class="text-gray-900 mb-2">범례</p>
      <div class="space-y-1">
        <div class="flex items-center gap-2">
          <div class="w-3 h-3 rounded-full bg-red-500"></div>
          <span class="text-gray-600">맛집</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="w-3 h-3 rounded-full bg-amber-500"></div>
          <span class="text-gray-600">카페</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="w-3 h-3 rounded-full bg-blue-500"></div>
          <span class="text-gray-600">관광지</span>
        </div>
        <div class="flex items-center gap-2">
          <div class="w-3 h-3 rounded-full bg-purple-500"></div>
          <span class="text-gray-600">숙소</span>
        </div>
      </div>
    </div>

    <!-- Results Count -->
    <div class="absolute bottom-4 right-4 z-10 bg-white rounded-lg shadow-lg px-4 py-2">
      <p class="text-gray-700">{{ places.length }}개의 장소</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { MapPin } from 'lucide-vue-next'
import ImageWithFallback from './figma/ImageWithFallback.vue'

export type PlaceCategory = '맛집' | '카페' | '관광지' | '숙소'
export type Place = {
  id: number
  name: string
  category: PlaceCategory
  rating: number
  reviews: number
  distance: number
  image: string
  lat: number
  lng: number
  description: string
}

const props = defineProps<{
  places: Place[]
  selectedPlace: Place | null
}>()

defineEmits<{
  (e: 'placeSelect', place: Place): void
}>()

const positions = [
  { top: '30%', left: '25%' },
  { top: '45%', left: '60%' },
  { top: '60%', left: '35%' },
  { top: '25%', left: '70%' },
  { top: '70%', left: '55%' },
] as const

const gridBackground = computed(() => `
  linear-gradient(rgba(200, 200, 200, 0.1) 1px, transparent 1px),
  linear-gradient(90deg, rgba(200, 200, 200, 0.1) 1px, transparent 1px)
`)

function markerStyle(index: number) {
  const p = positions[index % positions.length]
  return { top: p.top, left: p.left }
}

function isSelected(place: Place) {
  return props.selectedPlace?.id === place.id
}

function markerBg(category: PlaceCategory) {
  if (category === '맛집') return 'bg-red-500'
  if (category === '카페') return 'bg-amber-500'
  if (category === '관광지') return 'bg-blue-500'
  return 'bg-purple-500'
}

function markerPoint(category: PlaceCategory) {
  if (category === '맛집') return 'border-t-red-500'
  if (category === '카페') return 'border-t-amber-500'
  if (category === '관광지') return 'border-t-blue-500'
  return 'border-t-purple-500'
}

function markerEmoji(category: PlaceCategory) {
  if (category === '맛집') return '🍽️'
  if (category === '카페') return '☕'
  if (category === '관광지') return '🏛️'
  return '🏨'
}
</script>
