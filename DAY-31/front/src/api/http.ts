import axios from 'axios'

/**
 * 관통 프로젝트용 axios 인스턴스
 * - .env에 VITE_API_BASE_URL 설정하면 자동으로 그 값을 사용
 * - 기본값: 로컬 DRF (http://127.0.0.1:8000)
 */
export const http = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? 'http://127.0.0.1:8000',
  withCredentials: true,
})
