import axios from 'axios'

const api = axios.create({
  baseURL: 'https://luz-vida.onrender.com/api', // URL fixa para teste
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('admin_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default api