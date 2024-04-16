<script lang="ts" setup>
import type { ProductBase } from '@/types'

const props = defineProps<{
  productBase: ProductBase
}>()

const isOpen = ref(false)
</script>

<template>
  <div>
    <p @click="isOpen = true"
      class="lg:w-44 flex items-center text-orange-500 font-medium cursor-pointer lg:hover:text-white lg:hover:bg-orange-500 lg:border lg:border-orange-500 rounded-2xl lg:px-2 py-1">
      <UIcon name="i-ph-bell" class="w-5 h-5" />
      Theo dõi giảm giá
    </p>
    <UModal :model-value="isOpen" prevent-close :ui="{ width: ' sm:max-w-sm' }">
      <div class="p-3">
        <div class="text-end">
          <UButton icon="i-ph-x" color="gray" variant="ghost" :padding="false" @click="isOpen = false" />
        </div>
        <div>
          <div class="w-12 h-12 rounded-full text-orange-600 bg-orange-100 mx-auto flex items-center justify-center">
            <UIcon name="i-ph-bell-simple" class="w-6 h-6" />
          </div>
        </div>
        <div class="my-4 text-center lg:text-lg font-medium">Nhận thông báo khi giảm giá</div>
        <div class="text-center text-sm text-gray-500">
          Bạn có muốn nhận thông báo qua email ngay khi sản phẩm này vừa
          giảm giá ?
        </div>
        <div class="mb-8 p-2 shadow-md rounded flex items-center gap-2">
          <img :src="productBase.url_thumbnail" :alt="productBase.name" class="w-20 h-20">
          <div>
            <div class="text-sm font-medium">{{ productBase.name }}</div>
            <div class="text-red-500 text-sm font-medium">{{ productBase.price }} ₫</div>
          </div>
        </div>
        <div>
          <UInput color="blue" placeholder="Email của bạn" icon="i-ph-envelope-simple" />
          <UButton label="Đăng ký theo dõi giảm giá" color="blue" size="md" block class="mt-2" />
        </div>
      </div>
    </UModal>
  </div>
</template>
