<script lang="ts" setup>
interface RelatedBlog {
  url_thumbnail: string
  category_id: number
  lst_category_base_id: string[]
  lst_keyword: string[]
  id: number
  title: string
  excerpt: string
  published_at: string
  slug: string
}

const props = defineProps<{
  blog: RelatedBlog
}>()
</script>

<template>
  <div class="w-64 lg:w-1/3">
    <NuxtLink :to="`/blog/${blog.slug}`">
      <img :src="blog.url_thumbnail" alt="" class="w-full object-cover aspect-[7/4]">
      <p class="text-lg font-medium text-gray-900 line-clamp-2 h-14">{{ blog.title }}</p>
      <p class="mt-3 font-normal text-sm text-gray-500 line-clamp-3 h-16">{{ blog.excerpt }}</p>
      <div class="mt-5 h-10 bg-gray-200 flex items-center justify-center">ĐỌC THÊM</div>
    </NuxtLink>
  </div>
</template>
