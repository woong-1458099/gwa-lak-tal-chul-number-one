<template>
  <div class="h-screen flex flex-col">
    <Navigation />
    <div class="flex-1 flex overflow-hidden">
      <MapSidebar :filters="filters" @updateFilters="filters = $event" />

      <MapView
        :places="filteredPlaces"
        :selectedPlace="selectedPlace"
        @placeSelect="selectedPlace = $event"
      />

      <PlaceInfoCard
        v-if="selectedPlace"
        :place="selectedPlace"
        @close="selectedPlace = null"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import Navigation from './Navigation.vue'
import MapSidebar from './MapSidebar.vue'
import MapView from './MapView.vue'
import PlaceInfoCard from './PlaceInfoCard.vue'
import type { Place } from './MapView.vue'

type Filters = {
  categories: string[]
  minRating: number
  maxDistance: number
}

const selectedPlace = ref<Place | null>(null)
const filters = ref<Filters>({
  categories: [],
  minRating: 0,
  maxDistance: 10,
})

// Mock places data (원본 TSX 데이터 그대로)
const places: Place[] = [
  {
    id: 1,
    name: '광장시장',
    category: '맛집',
    rating: 4.5,
    reviews: 1234,
    distance: 2.3,
    image: 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&q=80',
    lat: 37.5709,
    lng: 126.999,
    description: '전통 시장 맛집의 진수',
  },
  {
    id: 2,
    name: '북촌 한옥마을',
    category: '관광지',
    rating: 4.8,
    reviews: 2567,
    distance: 1.5,
    image: 'https://images.unsplash.com/photo-1549877452-9c387954fbc2?w=400&q=80',
    lat: 37.5825,
    lng: 126.9833,
    description: '전통 한옥의 아름다움',
  },
  {
    id: 3,
    name: '카페 온즈',
    category: '카페',
    rating: 4.6,
    reviews: 892,
    distance: 0.8,
    image: 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=400&q=80',
    lat: 37.5665,
    lng: 126.9784,
    description: '감성 넘치는 루프탑 카페',
  },
  {
    id: 4,
    name: '시그니엘 서울',
    category: '숙소',
    rating: 4.9,
    reviews: 3421,
    distance: 5.2,
    image: 'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400&q=80',
    lat: 37.5126,
    lng: 127.1025,
    description: '프리미엄 럭셔리 호텔',
  },
  {
    id: 5,
    name: '명동 교자',
    category: '맛집',
    rating: 4.4,
    reviews: 1876,
    distance: 3.1,
    image: 'https://images.unsplash.com/photo-1563245372-f21724e3856d?w=400&q=80',
    lat: 37.5617,
    lng: 126.985,
    description: '50년 전통의 칼국수 맛집',
  },
]

const filteredPlaces = computed(() => {
  return places.filter((place) => {
    if (filters.value.categories.length > 0 && !filters.value.categories.includes(place.category)) return false
    if (place.rating < filters.value.minRating) return false
    if (place.distance > filters.value.maxDistance) return false
    return true
  })
})
</script>
