// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  app: {
    head: {
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: 'https://lh3.googleusercontent.com/pw/ADCreHfOpzfxaMaVSOZaIX2Btoe38cSog9gJtrKDQC3EmiyzSDEUfJ3tX0LgyOjI58YeKstyQv2RT2M5PQHhIFqN7eSRKOZEcye9S9zy7Tqjhps9PSEgEvBBLoHnFnVeY2FBbHFvVOakhpLxgXlzmxVNFF1N=w1528-h1528-s-no' }
      ]
    }
  },

  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE ?? 'http://localhost:8000',
    }
  },

  modules: ["@nuxt/ui", "@vueuse/nuxt"],

  ui: {
    icons: ['ph', 'fluent-mdl2'],
  },

  css: ['~/assets/css/main.css']
})