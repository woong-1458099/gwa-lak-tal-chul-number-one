import { defineStore } from 'pinia'
import { ref } from 'vue'
import { http } from '@/api/http'

/**
 * 관통 프로젝트에서 자주 쓰는 인증 스토어(초안)
 * - 백엔드 API에 맞게 endpoint만 바꿔서 쓰면 됨
 */
export const useAuthStore = defineStore('auth', () => {
  const token = ref<string | null>(null)
  const user = ref<any>(null)

  async function login(payload: { email: string; password: string }) {
    // 예시 endpoint (프로젝트 명세에 맞게 수정)
    // const res = await http.post('/accounts/login/', payload)
    // token.value = res.data.key
    // await fetchMe()
    await http.post('/login/', payload)
  }

  async function logout() {
    token.value = null
    user.value = null
    // await http.post('/accounts/logout/')
  }

  async function fetchMe() {
    // const res = await http.get('/accounts/user/')
    // user.value = res.data
  }

  return { token, user, login, logout, fetchMe }
})
