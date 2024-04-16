<script lang="ts" setup>
import type { CompareDataProduct } from '@/types'

const props = defineProps<{
  product: CompareDataProduct
}>()
</script>

<template>
  <div class="shadow-md hover:border hover:shadow-lg rounded-xl flex items-center gap-2 p-2 lg:p-4">
    <img :src="product.url_thumbnail" :alt="product.name" class="w-20 h-20">

    <div class="flex-1 flex items-center">
      <div>
        <div>{{ product.name }}</div>
      </div>
      <div class="ml-auto">
        <div>{{ product.price }}</div>
      </div>
    </div>

    <div>
      <div
        class="border border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white hover:font-medium rounded px-4 py-2 flex items-center gap-2">
        Đến nơi bán
        <UIcon name="i-ph-arrow-right" class="w-5 h-5" />
      </div>
    </div>
  </div>
</template>
