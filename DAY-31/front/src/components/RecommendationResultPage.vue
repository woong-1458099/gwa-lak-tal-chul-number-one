<template>
  <div class="min-h-screen bg-gradient-to-br from-orange-50 via-white to-blue-50">
    <Navigation />

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Header Section -->
      <div class="mb-8">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-orange-100 to-amber-100 rounded-full mb-4">
          <Sparkles class="w-4 h-4 text-orange-600" />
          <span class="text-orange-700">AI 맞춤 추천</span>
        </div>

        <h1 class="text-gray-900 mb-3">여행 추천 결과</h1>
        <p class="text-gray-600">부산 2박 3일 가족 여행을 위한 맞춤형 일정을 준비했습니다.</p>
      </div>

      <!-- Action Buttons -->
      <div class="flex flex-wrap gap-3 mb-8">
        <button
          type="button"
          @click="isSaved = !isSaved"
          :class="[
            'flex items-center gap-2 px-6 py-3 rounded-lg transition-all shadow-md hover:shadow-lg',
            isSaved ? 'bg-gradient-to-r from-green-500 to-green-600 text-white' : 'bg-white text-gray-700 hover:bg-gray-50'
          ]"
        >
          <Save class="w-5 h-5" :class="isSaved ? 'fill-white' : ''" />
          <span>{{ isSaved ? '저장됨' : '일정 저장하기' }}</span>
        </button>

        <button type="button" class="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-lg transition-all shadow-md hover:shadow-lg">
          <MapIcon class="w-5 h-5" />
          <span>지도에서 보기</span>
        </button>
      </div>

      <!-- Trip Overview -->
      <div class="bg-white rounded-2xl shadow-lg p-6 mb-8 border border-orange-100">
        <h2 class="text-gray-900 mb-4">여행 개요</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="flex items-start gap-3">
            <div class="w-10 h-10 bg-orange-100 rounded-full flex items-center justify-center flex-shrink-0">
              <Clock class="w-5 h-5 text-orange-600" />
            </div>
            <div>
              <p class="text-gray-900">기간</p>
              <p class="text-gray-600">2박 3일</p>
            </div>
          </div>
          <div class="flex items-start gap-3">
            <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center flex-shrink-0">
              <MapPin class="w-5 h-5 text-blue-600" />
            </div>
            <div>
              <p class="text-gray-900">지역</p>
              <p class="text-gray-600">서울 전역</p>
            </div>
          </div>
          <div class="flex items-start gap-3">
            <div class="w-10 h-10 bg-amber-100 rounded-full flex items-center justify-center flex-shrink-0">
              <Sparkles class="w-5 h-5 text-amber-600" />
            </div>
            <div>
              <p class="text-gray-900">테마</p>
              <p class="text-gray-600">가족 여행</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Day by Day Itinerary -->
      <div class="mb-8">
        <h2 class="text-gray-900 mb-6">일정표</h2>
        <div class="space-y-4">
          <DayItinerary v-for="d in itinerary" :key="d.day" :day="d" />
        </div>
      </div>

      <!-- Recommended Places -->
      <div>
        <h2 class="text-gray-900 mb-6">추천 장소 상세</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <RecommendedPlaceCard v-for="p in recommendedPlaces" :key="p.id" :place="p" />
        </div>
      </div>

      <!-- Tips Section -->
      <div class="mt-8 bg-gradient-to-r from-amber-50 to-orange-50 rounded-2xl p-6 border border-amber-200">
        <h3 class="text-gray-900 mb-3">💡 여행 팁</h3>
        <ul class="space-y-2 text-gray-700">
          <li>• 대중교통 이용 시 T-money 카드를 구매하면 편리합니다.</li>
          <li>• 인기 맛집은 웨이팅이 있을 수 있으니 일찍 방문하세요.</li>
          <li>• 궁궐은 화요일을 제외하고 매일 개방됩니다.</li>
          <li>• 편한 신발을 착용하시면 더 즐거운 여행이 됩니다.</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Navigation from './Navigation.vue'
import DayItinerary, { type DayPlan } from './DayItinerary.vue'
import RecommendedPlaceCard, { type Place } from './RecommendedPlaceCard.vue'
import { Save, Map as MapIcon, Sparkles, Clock, MapPin } from 'lucide-vue-next'

const isSaved = ref(false)

const itinerary: DayPlan[] = [
  {
    day: 1,
    title: '역사와 전통 체험',
    places: ['경복궁', '북촌 한옥마을', '인사동 맛집', '청계천'],
    highlights: '조선시대 궁궐과 전통 한옥을 둘러보며 한국의 역사를 체험하세요.',
  },
  {
    day: 2,
    title: '현대와 쇼핑의 중심',
    places: ['명동', '남산타워', '강남 카페', '코엑스'],
    highlights: '현대적인 서울의 모습과 쇼핑, 맛집을 즐기는 하루입니다.',
  },
  {
    day: 3,
    title: '자연과 힐링',
    places: ['한강공원', '이태원 브런치', '홍대 거리', '여의도 야경'],
    highlights: '자연 속에서 여유를 즐기고 트렌디한 문화를 경험하세요.',
  },
]

const recommendedPlaces: Place[] = [
  {
    id: 1,
    name: '경복궁',
    category: '관광지',
    rating: 4.8,
    reviews: 3521,
    image: 'https://images.unsplash.com/photo-1549877452-9c387954fbc2?w=600&q=80',
    description: '조선왕조의 법궁으로 한국의 역사와 문화를 느낄 수 있는 대표적인 관광지입니다.',
    address: '서울특별시 종로구 사직로 161',
    estimatedTime: '2-3시간',
  },
  {
    id: 2,
    name: '광장시장',
    category: '맛집',
    rating: 4.6,
    reviews: 2134,
    image: 'https://images.unsplash.com/photo-1517154421773-0529f29ea451?w=600&q=80',
    description: '빈대떡, 마약김밥 등 전통 한국 음식을 맛볼 수 있는 유명 재래시장입니다.',
    address: '서울특별시 종로구 창경궁로 88',
    estimatedTime: '1-2시간',
  },
  {
    id: 3,
    name: '북촌 한옥마을',
    category: '관광지',
    rating: 4.7,
    reviews: 2891,
    image: 'https://images.unsplash.com/photo-1583037189850-1921ae7c6c22?w=600&q=80',
    description: '전통 한옥이 보존된 마을로 한국의 아름다운 건축양식을 감상할 수 있습니다.',
    address: '서울특별시 종로구 계동길 37',
    estimatedTime: '1-2시간',
  },
  {
    id: 4,
    name: '카페 온즈',
    category: '카페',
    rating: 4.5,
    reviews: 892,
    image: 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=600&q=80',
    description: '감성적인 인테리어와 맛있는 커피로 유명한 루프탑 카페입니다.',
    address: '서울특별시 마포구 와우산로 94',
    estimatedTime: '1시간',
  },
  {
    id: 5,
    name: '명동 거리',
    category: '쇼핑',
    rating: 4.4,
    reviews: 4231,
    image: 'https://images.unsplash.com/photo-1601024445121-e5b82f020549?w=600&q=80',
    description: '쇼핑과 먹거리가 가득한 서울의 대표적인 관광 명소입니다.',
    address: '서울특별시 중구 명동길',
    estimatedTime: '2-3시간',
  },
  {
    id: 6,
    name: '남산타워',
    category: '관광지',
    rating: 4.6,
    reviews: 5621,
    image: 'https://images.unsplash.com/photo-1583037189850-1921ae7c6c22?w=600&q=80',
    description: '서울의 전경을 한눈에 볼 수 있는 상징적인 랜드마크입니다.',
    address: '서울특별시 용산구 남산공원길 105',
    estimatedTime: '2시간',
  },
]
</script>
