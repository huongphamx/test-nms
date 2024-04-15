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
  modules: ["@nuxt/ui"],

  ui: {
    icons: ['ph', 'fluent-mdl2'],
  },

  css: ['~/assets/css/main.css']
})