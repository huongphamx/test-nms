<script lang="ts" setup>
import type { ProductBase } from '@/types'

const props = defineProps<{
  productData: ProductBase
}>()
const tabs = [
  { id: 'price-compare', icon: 'i-fluent-mdl2-compare', label: 'So sánh giá' },
  { id: 'price-history', icon: 'i-ph-chart-line', label: 'Lịch sử giá' },
  { id: 'description', icon: 'i-ph-info', label: 'Mô tả sản phẩm' },
  { id: 'reviews', icon: 'i-ph-chats-circle', label: 'Đánh giá từ người mua' },
]

const compareSection = ref<HTMLElement>()
const priceHistorySection = ref<HTMLElement>()
const descriptionSection = ref<HTMLElement>()
const reviewsSection = ref<HTMLElement>()

const currentSection = ref('price-compare')
function scrollToSection(id: string) {
  currentSection.value = id
  if (id === 'price-compare') {
    window.scrollTo({
      behavior: 'smooth',
      top: compareSection.value!.getBoundingClientRect().top - document.body.getBoundingClientRect().top - 60
    })
  } else if (id === 'price-history') {
    window.scrollTo({
      behavior: 'smooth',
      top: priceHistorySection.value!.getBoundingClientRect().top - document.body.getBoundingClientRect().top - 60
    })
  } else if (id === 'description') {
    window.scrollTo({
      behavior: 'smooth',
      top: descriptionSection.value!.getBoundingClientRect().top - document.body.getBoundingClientRect().top - 60
    })
  } else if (id === 'reviews') {
    window.scrollTo({
      behavior: 'smooth',
      top: reviewsSection.value!.getBoundingClientRect().top - document.body.getBoundingClientRect().top - 60
    })
  }
}
</script>

<template>
  <div>
    <div class="sticky top-0 z-10 w-full bg-white">
      <ul class="flex lg:gap-1 justify-between lg:justify-normal">
        <li v-for="tab in tabs" :key="tab.id"
          class="w-full lg:w-fit px-2 py-1 lg:py-3 flex flex-col lg:flex-row items-center gap-2 border-b md:border-b-2 cursor-pointer"
          :class="currentSection === tab.id ? 'md:border-orange-500' : 'text-gray-500'"
          @click="scrollToSection(tab.id)">
          <div>
            <UIcon :name="tab.icon" class="w-5 h-5" />
          </div>
          <div class="text-[10px] lg:text-base font-medium text-center">{{ tab.label }}</div>
        </li>
      </ul>
    </div>

    <div class="px-4 py-2 lg:px-0">
      <div id="price-compare" ref="compareSection" class="mt-2 scroll-mt-20">
        <div class="lg:text-lg font-medium">So sánh giá</div>
        <ProductComparePrice />
      </div>
      <div id="price-history" ref="priceHistorySection" class="mt-4 scroll-mt-16">
        <div class="flex justify-between items-center">
          <span class="lg:text-lg font-medium">Lịch sử giá</span>
          <ModalProductTrackPrice :product-base="productData" />
        </div>
        <ProductPriceHistory :product-data="productData" />
      </div>
      <div id="product-description" ref="descriptionSection" class="mt-4 scroll-mt-16">
        <div class="lg:text-lg font-medium mb-4">Mô tả sản phẩm</div>
        <ProductDescription :description="productData.description.replace(/(?:\r\n|\r|\n)/g, '<br>')" />
      </div>
      <div id="product-reviews" ref="reviewsSection" class="mt-4 scroll-mt-16">
        <div class="lg:text-lg font-medium mb-4">Đánh giá từ người mua</div>
        <ProductReviews :product-data="productData" />
      </div>
    </div>
  </div>
</template>
