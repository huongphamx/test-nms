<script lang="ts" setup>
export interface CategoryListResponse {
  status: string
  data: {
    categories: Category[]
  }
}

export interface Category {
  category_base_id: string
  slug: string
  name: string
  url_thumbnail: string
  cat_level: number
  parent_category_id: string | null
  relative_path: string | null
  childs: Category[] | null
}

const isOpen = ref(false)

const { data: categoryListRes, pending } = await useAPI<CategoryListResponse>('/v1/categories/', { lazy: true })

</script>

<template>
  <div>
    <UButton label="DANH MỤC" icon="i-ph-list" color="gray" variant="ghost" size="xl" @click="isOpen = true" />
    <UModal :model-value="isOpen" prevent-close fullscreen>
      <div v-if="categoryListRes" class="flex">
        <div class="w-72 xl:w-96 border-r h-screen overflow-auto scrollbar-hide">
          <div v-for="cat0 in categoryListRes.data.categories" :key="cat0.category_base_id"
            class="px-4 py-2.5 hover:bg-gray-100 flex items-center gap-2">
            <img :src="cat0.url_thumbnail" :alt="cat0.name" class="w-12 h-12 rounded-full">
            <span>{{ cat0.name }}</span>
          </div>
        </div>
        <div class="flex-1 p-4">
          <div class="text-end">
            <UButton icon="i-ph-x" :padded="false" color="gray" variant="ghost" @click="isOpen = false" />
          </div>
        </div>
      </div>
    </UModal>
  </div>
</template>
