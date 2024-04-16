<script lang="ts" setup>
import { vi } from 'date-fns/locale'
import type { Review } from '@/types'

const props = defineProps<{
  review: Review
}>()

const platformName = computed(() => {
  switch (props.review.platform_id) {
    case 1:
      return 'Shopee'
    case 2:
      return 'Lazada'
    case 3:
      return 'Tiki'
  }
})
</script>

<template>
  <div class="py-4 border-b">
    <div class="flex gap-2 items-center">
      <img :src="review.user_url_image" alt="" class="w-10 h-10 rounded-full">
      <div>
        <div class="flex items-center gap-1">
          <span class="text-xs text-gray-500">{{ review.user_username }}</span>
          <UIcon name="i-ph-check-circle" class="text-green-500 text-xs" />
          <span class="text-green-500 text-xs font-medium">Đã mua tại {{ platformName }}</span>
        </div>
        <div>
          <AppRating :score="review.rating" size="sm" />
        </div>
      </div>
    </div>
    <div class="my-1 text-sm text-gray-600 max-w-[900px]">{{ review.content }}</div>
    <div v-if="review.images" class="flex gap-2 items-center">
      <img v-for="image in review.images" :src="image" alt="" class="w-16 h-16">
    </div>
    <div class="text-xs text-gray-500">
      <timeago :datetime="new Date(review.created_at_platform * 1000)" :locale="vi" />
    </div>
  </div>
</template>
