<script lang="ts" setup>
import type { CompareDataProduct } from '@/types'

const props = defineProps<{
  product: CompareDataProduct
}>()
</script>

<template>
  <div class="shadow-md hover:border hover:shadow-lg rounded-xl flex items-center gap-2 p-2 lg:p-4">
    <img :src="product.url_thumbnail" :alt="product.name" class="w-12 h-12 md:w-20 md:h-20">

    <div class="flex-1 line-clamp-2">{{ product.name }}</div>

    <div class="flex flex-col lg:flex-row items-center gap-2">
      <div class="text-red-500 font-medium">{{ product.price.toLocaleString('de-DE') }} ₫</div>
      <div
        class="border border-blue-700 text-blue-700 hover:bg-blue-700 hover:text-white hover:font-medium rounded px-2 md:px-4 py-2 flex items-center gap-2">
        <span class="text-sm md:text-base">Đến nơi bán</span>
        <UIcon name="i-ph-arrow-right" class="w-5 h-5" />
      </div>
    </div>
  </div>
</template>
