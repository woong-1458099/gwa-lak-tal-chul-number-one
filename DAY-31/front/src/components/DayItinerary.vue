<template>
  <div class="bg-white rounded-xl shadow-md border border-orange-100 overflow-hidden hover:shadow-lg transition-shadow">
    <div class="bg-gradient-to-r from-orange-500 to-amber-500 px-6 py-4">
      <div class="flex items-center justify-between">
        <div>
          <p class="text-orange-50">Day {{ day.day }}</p>
          <h3 class="text-white">{{ day.title }}</h3>
        </div>
        <div class="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center">
          <span class="text-white text-xl">{{ day.day }}</span>
        </div>
      </div>
    </div>

    <div class="p-6">
      <p class="text-gray-600 mb-4">{{ day.highlights }}</p>

      <div class="space-y-3">
        <div v-for="(place, index) in day.places" :key="index" class="flex items-center gap-3">
          <div class="flex items-center justify-center w-8 h-8 bg-orange-100 text-orange-600 rounded-full flex-shrink-0">
            {{ index + 1 }}
          </div>
          <div class="flex-1 flex items-center gap-2">
            <MapPin class="w-4 h-4 text-gray-400" />
            <span class="text-gray-700">{{ place }}</span>
          </div>
          <ChevronRight v-if="index < day.places.length - 1" class="w-4 h-4 text-gray-400" />
        </div>
      </div>

      <div class="mt-4 pt-4 border-t border-gray-100">
        <div class="flex items-center gap-2 text-gray-600">
          <Clock class="w-4 h-4" />
          <span>예상 소요 시간: 8-10시간</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { MapPin, Clock, ChevronRight } from 'lucide-vue-next'

export type DayPlan = {
  day: number
  title: string
  places: string[]
  highlights: string
}

defineProps<{
  day: DayPlan
}>()
</script>
