<script lang="ts" setup>
import type { ProductBase } from '@/types'

const { data: productData } = await useAPI<ProductBase>(`/v1/products/1__5382617241__227642622`, { lazy: true })

const page = ref(0)

useHead({
  title: () => `Lịch sử giá ${productData.value?.name}`
})
</script>

<template>
  <div v-if="productData" class="max-w-7xl mx-auto mb-16">
    <UBreadcrumb :links="[{
    icon: 'i-heroicons-home',
    to: '/'
  }, {
    label: 'Máy tính lap top',
  }, {
    label: 'Phụ kiện máy tính',
  }, {
    label: 'Bộ chia cổng'
  }]" class="lg:py-2" />

    <div class="w-full flex items-center lg:items-start flex-col lg:flex-row mb-4 lg:mb-6 px-2 sm:px-0">
      <ProductImages :images="productData.url_images" />
      <div id="info">
        <h1 class="mt-4 lg:mt-0 text-gray-800 lg:text-lg font-semibold">{{ productData.name }}</h1>
        <ModalProductTrackPrice :product-base="productData" class="my-2 lg:my-4" />
        <p class="flex flex-wrap items-center text-gray-600 mb-4">
          Giá từ Shopee

        </p>

        <div class="flex lg:flex-col justify-between flex-col">
          <div
            class="h-full flex-grow flex justify-between lg:justify-start lg:flex-row lg:space-x-10 lg:items-center mb-3 flex-row">
            <div class="flex flex-col lg:flex-row items-center gap-4">
              <div>
                <p class="text-red-600 text-2xl font-bold">{{ productData.price.toLocaleString('de-DE') }} ₫</p>
                <p class="text-sm text-gray-500 line-through">{{
    productData.price_before_discount.toLocaleString('de-DE') }} ₫</p>
              </div>
              <div class="h-fit flex items-center gap-2 bg-green-400 rounded-lg p-1 text-green-900">
                <UIcon :name="productData.price_insight.delta_price < 0 ? 'i-ph-trend-down' : 'i-ph-trend-up'"
                  class="w-4 h-4" />
                <span class="text-xs font-medium">
                  {{ Math.abs(productData.price_insight.delta_price).toLocaleString('de-DE') }} ₫
                </span>
              </div>
            </div>
            <div
              class="h-fit text-white text-sm md:text-base px-4 py-2 bg-orange-500 hover:font-semibold flex items-center gap-2 rounded">
              <span class="">Đến nơi bán</span>
              <UIcon name="i-ph-arrow-right" class="w-5 h-5" />
            </div>
          </div>
        </div>

        <div class="flex items-center text-xs lg:text-sm">
          <div class="px-2 text-amber-400 flex items-center border-r-2">
            <span>{{ productData.rating_avg.toFixed(1) }}</span>
            <AppRating :score="productData.rating_avg" size="lg" />
          </div>
          <div class="px-2 border-r-2">
            <span>{{ productData.rating_count }}</span> <span class="text-gray-500">đánh giá</span>
          </div>
          <div class="px-2">
            <span>{{ productData.historical_sold }}</span> <span class="text-gray-500">lượt bán</span>
          </div>
        </div>
      </div>
    </div>
    <div class="lg:hidden my-2 h-1 bg-gray-200"></div>
    <ProductTabs :product-data="productData" />

    <ProductRelated class="mt-8" />

    <ProductSuggested class="mt-8" />
    <UDivider class="my-8" />
    <BlogRelated />
    <UDivider class="my-8" />
    <ProductRecent />
    <UDivider class="my-8" />
    <ExtensionAds />
  </div>
</template>
