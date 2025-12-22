<template>
  <div class="min-h-screen relative flex items-center justify-center p-4">
    <!-- Background Image with Overlay -->
    <div class="absolute inset-0 z-0">
      <ImageWithFallback
        src="https://images.unsplash.com/photo-1655722723663-75b47de17a31?w=1600&q=80"
        alt="Travel background"
        class="w-full h-full object-cover"
      />
      <div class="absolute inset-0 bg-gradient-to-br from-blue-500/20 via-white/40 to-blue-400/30 backdrop-blur-sm"></div>
    </div>

    <!-- Sign Up Card -->
    <div class="relative z-10 w-full max-w-md">
      <div class="bg-white rounded-2xl shadow-2xl p-8 sm:p-10">
        <!-- Logo/Icon -->
        <div class="flex justify-center mb-6">
          <div class="w-16 h-16 bg-blue-500 rounded-full flex items-center justify-center">
            <Compass class="w-8 h-8 text-white" />
          </div>
        </div>

        <!-- Title -->
        <h1 class="text-center text-gray-900 mb-8">회원가입</h1>

        <!-- Sign Up Form -->
        <form class="space-y-5" @submit.prevent="handleSubmit">
          <!-- Email Input -->
          <div>
            <label for="email" class="block text-gray-700 mb-2">이메일</label>
            <div class="relative">
              <div class="absolute left-3 top-1/2 -translate-y-1/2">
                <Mail class="w-5 h-5 text-gray-400" />
              </div>
              <input
                id="email"
                v-model="email"
                type="email"
                placeholder="example@email.com"
                class="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                required
              />
            </div>
          </div>

          <!-- Nickname Input -->
          <div>
            <label for="nickname" class="block text-gray-700 mb-2">닉네임</label>
            <div class="relative">
              <div class="absolute left-3 top-1/2 -translate-y-1/2">
                <User class="w-5 h-5 text-gray-400" />
              </div>
              <input
                id="nickname"
                v-model="nickname"
                type="text"
                placeholder="사용하실 닉네임을 입력하세요"
                class="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                required
              />
            </div>
          </div>

          <!-- Password Input -->
          <div>
            <label for="password" class="block text-gray-700 mb-2">비밀번호</label>
            <div class="relative">
              <div class="absolute left-3 top-1/2 -translate-y-1/2">
                <Lock class="w-5 h-5 text-gray-400" />
              </div>
              <input
                id="password"
                v-model="password"
                type="password"
                placeholder="••••••••"
                class="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                required
              />
            </div>
          </div>

          <!-- Password Confirmation Input -->
          <div>
            <label for="passwordConfirm" class="block text-gray-700 mb-2">비밀번호 확인</label>
            <div class="relative">
              <div class="absolute left-3 top-1/2 -translate-y-1/2">
                <Lock class="w-5 h-5 text-gray-400" />
              </div>
              <input
                id="passwordConfirm"
                v-model="passwordConfirm"
                type="password"
                placeholder="••••••••"
                class="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                required
              />
            </div>
          </div>

          <!-- Sign Up Button -->
          <button
            type="submit"
            class="w-full bg-blue-500 hover:bg-blue-600 text-white py-3 rounded-lg transition-colors shadow-md hover:shadow-lg"
          >
            회원가입 완료
          </button>
        </form>

        <!-- Divider -->
        <div class="relative my-6">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-gray-200"></div>
          </div>
          <div class="relative flex justify-center">
            <span class="px-4 bg-white text-gray-500">또는</span>
          </div>
        </div>

        <!-- Login Link -->
        <div class="text-center">
          <p class="text-gray-600">
            이미 계정이 있으신가요?
            <RouterLink to="/login" class="text-blue-500 hover:text-blue-600 transition-colors"> 로그인 하러가기</RouterLink>
          </p>
        </div>
      </div>

      <!-- Additional Info -->
      <p class="text-center mt-6 text-gray-600">Korea Travel과 함께 특별한 여행을 시작하세요 ✈️</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { useRouter } from 'vue-router'
import { Mail, Lock, User, Compass } from 'lucide-vue-next'
import ImageWithFallback from './figma/ImageWithFallback.vue'

const email = ref('')
const password = ref('')
const passwordConfirm = ref('')
const nickname = ref('')
const router = useRouter()

function handleSubmit() {
  if (password.value !== passwordConfirm.value) {
    alert('비밀번호가 일치하지 않습니다.')
    return
  }
  console.log('Sign up attempt:', { email: email.value, password: password.value, nickname: nickname.value })
  router.push('/login')
}
</script>
