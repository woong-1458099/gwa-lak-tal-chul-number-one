<template>
  <nav class="border-b border-gray-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <div class="flex items-center gap-2">
          <Compass class="w-6 h-6 text-blue-500" />
          <span class="text-gray-900">Korea Travel</span>
        </div>

        <div class="hidden md:flex items-center gap-8">
          <RouterLink to="/home" class="flex items-center gap-2 text-gray-700 hover:text-blue-500 transition-colors">
            <Home class="w-4 h-4" />
            <span>Home</span>
          </RouterLink>
          <RouterLink to="/map" class="flex items-center gap-2 text-gray-700 hover:text-blue-500 transition-colors">
            <MapIcon class="w-4 h-4" />
            <span>지도</span>
          </RouterLink>
          <RouterLink to="/recommend" class="flex items-center gap-2 text-gray-700 hover:text-blue-500 transition-colors">
            <Compass class="w-4 h-4" />
            <span>여행 추천</span>
          </RouterLink>
          <RouterLink to="/login" class="flex items-center gap-2 text-gray-700 hover:text-blue-500 transition-colors">
            <LogIn class="w-4 h-4" />
            <span>로그인</span>
          </RouterLink>
        </div>

        <!-- Mobile menu button (UI only) -->
        <button class="md:hidden p-2 text-gray-700" type="button" aria-label="Open menu">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" :stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { Home, Map as MapIcon, Compass, LogIn } from 'lucide-vue-next'
</script>
