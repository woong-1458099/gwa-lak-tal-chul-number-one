<template>
  <div class="w-80 bg-white border-r border-gray-200 overflow-y-auto flex-shrink-0">
    <div class="p-6">
      <!-- Header -->
      <div class="flex items-center gap-2 mb-6">
        <Filter class="w-5 h-5 text-blue-500" />
        <h2 class="text-gray-900">필터</h2>
      </div>

      <!-- Categories -->
      <div class="mb-6">
        <h3 class="text-gray-900 mb-3">카테고리</h3>
        <div class="space-y-2">
          <button
            v-for="c in categories"
            :key="c.id"
            type="button"
            @click="toggleCategory(c.id)"
            :class="[
              'w-full flex items-center gap-3 px-4 py-3 rounded-lg border transition-all',
              filters.categories.includes(c.id)
                ? 'bg-blue-50 border-blue-500 text-blue-700'
                : 'bg-white border-gray-200 text-gray-700 hover:bg-gray-50'
            ]"
          >
            <span class="text-xl">{{ c.icon }}</span>
            <span>{{ c.label }}</span>
          </button>
        </div>
      </div>

      <!-- Rating Filter -->
      <div class="mb-6">
        <div class="flex items-center gap-2 mb-3">
          <Star class="w-4 h-4 text-gray-700" />
          <h3 class="text-gray-900">평점</h3>
        </div>
        <div class="space-y-2">
          <button
            v-for="rating in [0, 3, 4, 4.5]"
            :key="rating"
            type="button"
            @click="updateFilters({ ...filters, minRating: rating })"
            :class="[
              'w-full flex items-center gap-2 px-4 py-2 rounded-lg border transition-all',
              filters.minRating === rating
                ? 'bg-blue-50 border-blue-500 text-blue-700'
                : 'bg-white border-gray-200 text-gray-700 hover:bg-gray-50'
            ]"
          >
            <Star class="w-4 h-4 fill-yellow-400 text-yellow-400" />
            <span>{{ rating === 0 ? '전체' : `${rating}점 이상` }}</span>
          </button>
        </div>
      </div>

      <!-- Distance Filter -->
      <div class="mb-6">
        <div class="flex items-center gap-2 mb-3">
          <MapPin class="w-4 h-4 text-gray-700" />
          <h3 class="text-gray-900">거리</h3>
        </div>
        <div class="space-y-3">
          <input
            type="range"
            min="1"
            max="20"
            :value="filters.maxDistance"
            @input="onDistanceInput"
            class="w-full accent-blue-500"
          />
          <div class="flex justify-between text-gray-600">
            <span>1km</span>
            <span class="text-blue-500">{{ filters.maxDistance }}km 이내</span>
            <span>20km</span>
          </div>
        </div>
      </div>

      <!-- Reset Button -->
      <button
        type="button"
        @click="reset"
        class="w-full py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors"
      >
        필터 초기화
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Filter, Star, MapPin } from 'lucide-vue-next'

type Filters = {
  categories: string[]
  minRating: number
  maxDistance: number
}

const props = defineProps<{
  filters: Filters
}>()

const emit = defineEmits<{
  (e: 'updateFilters', value: Filters): void
}>()

const categories = [
  { id: '맛집', label: '맛집', icon: '🍽️' },
  { id: '카페', label: '카페', icon: '☕' },
  { id: '관광지', label: '관광지', icon: '🏛️' },
  { id: '숙소', label: '숙소', icon: '🏨' },
] as const

function updateFilters(value: Filters) {
  emit('updateFilters', value)
}

function toggleCategory(category: string) {
  const newCategories = props.filters.categories.includes(category)
    ? props.filters.categories.filter((c) => c !== category)
    : [...props.filters.categories, category]
  updateFilters({ ...props.filters, categories: newCategories })
}

function onDistanceInput(e: Event) {
  const v = Number((e.target as HTMLInputElement).value)
  updateFilters({ ...props.filters, maxDistance: v })
}

function reset() {
  updateFilters({ categories: [], minRating: 0, maxDistance: 10 })
}
</script>
