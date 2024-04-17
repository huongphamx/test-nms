<script lang="ts" setup>
import type { Review, ProductBase } from '@/types'

const props = defineProps<{
  productData: ProductBase
}>()

const { data: reviews } = await useAPI<Review[]>(`/v1/products/${props.productData.product_base_id}/reviews`)
</script>

<template>
  <div>
    <ProductReviewsRow v-for="review in reviews" :key="review.review_base_id" :review="review" class="first:pt-0" />
  </div>
</template>
