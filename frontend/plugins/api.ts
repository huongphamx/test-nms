export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig()

  const $api = $fetch.create({
    baseURL: config.public.apiBase ?? 'http://localhost:8000/api',
  })

  // Expose to useNuxtApp().$api
  return {
    provide: {
      api: $api
    }
  }
})
